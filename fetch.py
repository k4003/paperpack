"""把选定主题的 arXiv 论文拉下来,存成本地 JSON 文件。

这只是项目 #1 的"数据获取器"。你接下来要自己写的,是读 papers.json
做统计/筛选的那个"处理脚本"。
"""

import json
from pathlib import Path

import arxiv

# ── 改这一行就能换主题 ──────────────────────────
QUERY = "cat:math.NT AND abs:p-adic"          # 见上面的语法示例
MAX_RESULTS = 50
OUTPUT = Path("papers.json")
# ──────────────────────────────────────────────


def fetch_papers(query: str, max_results: int) -> list[dict]:
    """搜 arXiv,返回简化过的论文记录列表。"""
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
    )
    client = arxiv.Client(page_size=50, delay_seconds=5.0, num_retries=5)

    papers: list[dict] = []
    for result in client.results(search):
        papers.append({
            "title": result.title,
            "authors": [a.name for a in result.authors],
            "year": result.published.year,
            "published": result.published.date().isoformat(),
            "primary_category": result.primary_category,
            "categories": result.categories,
            "arxiv_id": result.get_short_id(),
            "url": result.entry_id,
        })
    return papers


def main() -> None:
    print(f"Fetching up to {MAX_RESULTS} papers for: {QUERY!r} ...")
    papers = fetch_papers(QUERY, MAX_RESULTS)
    OUTPUT.write_text(
        json.dumps(papers, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Saved {len(papers)} papers -> {OUTPUT.resolve()}")


if __name__ == "__main__":
    main()