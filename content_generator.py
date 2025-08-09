import requests
import os
from datetime import datetime

OUTPUT_DIR = "site"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "index.html")

def get_random_wikipedia_article():
    S = requests.Session()
    URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
    try:
        response = S.get(URL, timeout=10)
        data = response.json()
        title = data.get("title", "Unknown")
        extract = data.get("extract", "")
        return title, extract
    except:
        return "Error", "Failed to fetch article."

def generate_html_content(articles):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Yasin'ın İlginç Bilgiler Sitesi</title>
    <style>
        body {{ font-family: Arial, sans-serif; padding: 20px; background: #fafafa; }}
        h1 {{ color: #333; }}
        article {{ background: white; padding: 15px; margin-bottom: 15px; border-radius: 8px; box-shadow: 0 0 8px rgba(0,0,0,0.1); }}
        h2 {{ color: #0077cc; margin-top: 0; }}
    </style>
</head>
<body>
    <h1>Yasin'ın Güncel İlginç Bilgiler Sitesi</h1>
    <p>Son güncelleme: {datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")}</p>
"""
    for title, extract in articles:
        html += f"<article>\n<h2>{title}</h2>\n<p>{extract}</p>\n</article>\n"

    html += """
</body>
</html>
"""
    return html

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    articles = []
    for _ in range(5):
        title, extract = get_random_wikipedia_article()
        articles.append((title, extract))

    html_content = generate_html_content(articles)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Site updated with {len(articles)} articles.")

if __name__ == "__main__":
    main()
