import json
from pydoc import text
import string
def build_summary(papers: list[dict]) -> str:
    """把摘要内容拼成一个 markdown 字符串并返回。"""
    lines = []
    lines.append("# arXiv 摘要")
    lines.append("")                          # 空行
    lines.append(f"论文总数: {len(papers)}")
    return "\n".join(lines) 

def load_papers(path: str = "papers.json") -> list[dict]:
    """读取 papers.json,返回论文记录组成的列表。"""
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def count_keys(papers: list[dict], key: str) -> dict[str, int]:
    """统计每个值的出现次数,返回一个字典,值是出现次数。"""
    count =  {}
    for paper in papers:
        for k in paper[key]:
            count[k] = count.get(k, 0) + 1
    return count
def top_n(counts: dict[str, int],n:int=10)-> list:
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:n]
def find_by_title(papers: list[dict], title: str) -> list[dict]:
    fitted=[]
    for paper in papers:
        if title in paper["title"]:
            fitted.append(paper)
    return fitted

def main() -> None:
    papers = load_papers()
    print(f"共 {len(papers)} 篇论文")
    author_count = count_keys(papers, "authors")
    top_authors = top_n(author_count)
    print("作者排名前10:",top_authors[:10])
    category_count = count_keys(papers, "categories")
    top_categories_list = top_n(category_count)
    print("类别排名前10:",top_categories_list)
    fitted_papers = find_by_title(papers, "p-adic")
    print(f"标题包含 'p-adic' 的论文有 {len(fitted_papers)} 篇:")
    for p in fitted_papers:
        print(f"{p['title']} ({p['year']}) — {p['url']}") 
    text = build_summary(papers)  
    with open("summary.md", "w", encoding="utf-8") as f:
        f.write(text)
    print("已写入 summary.md")

if __name__ == "__main__":
    main()
