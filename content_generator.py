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
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>CuriousWorld - Fascinating Science & Facts</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #74ebd5 0%, #ACB6E5 100%);
            color: #333;
        }}
        header {{
            background-color: rgba(255, 255, 255, 0.85);
            padding: 20px 40px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            text-align: center;
            font-size: 1.8rem;
            font-weight: 700;
            color: #2c3e50;
        }}
        main {{
            max-width: 900px;
            margin: 30px auto;
            background: white;
            border-radius: 12px;
            padding: 25px 40px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.12);
        }}
        article {{
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 1px solid #eee;
        }}
        h2 {{
            color: #2980b9;
            margin-bottom: 8px;
        }}
        p {{
            font-size: 1rem;
            line-height: 1.5;
            color: #555;
        }}
        footer {{
            text-align: center;
            padding: 15px;
            font-size: 0.9rem;
            color: #777;
            margin-top: 40px;
        }}
        @media (max-width: 600px) {{
            main {{
                padding: 20px 15px;
                margin: 20px 10px;
            }}
        }}
    </style>
</head>
<body>
    <header>CuriousWorld - Fascinating Science & Facts</header>
    <main>
        <p><em>Last updated: {datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")}</em></p>
"""
    for title, extract in articles:
        html += f"""<article>
            <h2>{title}</h2>
            <p>{extract}</p>
        </article>
"""

    html += """
    </main>
    <footer>
        &copy; 2025 CuriousWorld. All rights reserved.
    </footer>
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
