import requests
import os
from datetime import datetime

POSTS_DIR = "_posts"
if not os.path.exists(POSTS_DIR):
    os.makedirs(POSTS_DIR)

def get_random_wikipedia_article():
    S = requests.Session()
    URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
    try:
        response = S.get(URL, timeout=10)
        data = response.json()
        title = data.get("title", "Unknown").replace("/", "-")
        extract = data.get("extract", "")
        return title, extract
    except:
        return "Error", "Failed to fetch article."

def slugify(text):
    return text.lower().replace(" ", "-")

def create_markdown_file(title, content, date):
    slug = slugify(title)
    filename = f"{date.strftime('%Y-%m-%d')}-{slug}.md"
    filepath = os.path.join(POSTS_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"---\n")
        f.write(f"title: \"{title}\"\n")
        f.write(f"date: {date.strftime('%Y-%m-%d %H:%M:%S %z')}\n")
        f.write(f"layout: post\n")
        f.write(f"---\n\n")
        f.write(content)
    print(f"Created post: {filename}")

def main():
    date = datetime.utcnow()
    for _ in range(3):  # 3 yeni içerik
        title, extract = get_random_wikipedia_article()
        create_markdown_file(title, extract, date)

if __name__ == "__main__":
    main()
