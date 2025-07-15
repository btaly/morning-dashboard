import feedparser, random, html

# RSS feeds you want
feeds = {
    "The Verge": "https://www.theverge.com/rss/index.xml",
    "Techmeme": "https://www.techmeme.com/feed.xml",
    "Business Insider": "https://www.businessinsider.com/rss",
    "Fortune": "https://fortune.com/feed"
}

stoic_quotes = [
    "You have power over your mind — not outside events. Realize this, and you will find strength. — Marcus Aurelius",
    "It is not death that a man should fear, but never beginning to live. — Marcus Aurelius",
    "We suffer more often in imagination than in reality. — Seneca",
    "He who is brave is free. — Seneca",
    "How long are you going to wait before you demand the best for yourself? — Epictetus",
    "Man conquers the world by conquering himself. — Zeno of Citium"
]

def build_dashboard() -> str:
    parts = []

    # --- HTML HEAD / STYLES ---
    parts.append("""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><title>Morning Dashboard</title>
<style>
body{margin:0;font-family:Arial,sans-serif;background:#121212;color:#f0f0f0;}
header{background:#1e1e1e;padding:20px;text-align:center;font-size:2rem;border-bottom:1px solid #333;}
section{padding:20px;display:grid;grid-template-columns:1fr;gap:20px;}
.card{background:#1e1e1e;border:1px solid #333;border-radius:8px;padding:15px;}
.card h2{margin-top:0;border-bottom:1px solid #333;padding-bottom:8px;}
ul{padding-left:1rem;}li{margin-bottom:8px;}
a{color:#00bcd4;text-decoration:none;}a:hover{text-decoration:underline;}
.quick-links{display:flex;flex-wrap:wrap;gap:10px;margin-top:10px;}
.quick-links a{background:#2c2c2c;padding:10px 15px;border-radius:6px;text-decoration:none;color:#f0f0f0;border:1px solid #333;}
.quick-links a:hover{background:#3d3d3d;}
</style></head><body>
<header>☀️ Morning Dashboard</header><section>
""")

    # --- Stoic quote ---
    quote = html.escape(random.choice(stoic_quotes))
    parts.append(f'<div class="card"><h2>Daily Stoic Quote</h2>'
                 f'<blockquote style="font-style:italic;font-size:1.1rem;">{quote}</blockquote></div>')

    # --- Weather card ---
    parts.append('<div class="card"><h2>Guyton, GA Weather</h2>'
                 '<p><a href="https://www.wunderground.com/weather/us/ga/guyton" target="_blank">'
                 'View full weather report</a></p></div>')

    # --- News feeds ---
    for name, url in feeds.items():
        d = feedparser.parse(url)
        items = ''.join(
            f'<li><a href="{html.escape(e.link)}" target="_blank">{html.escape(e.title)}</a></li>'
            for e in d.entries[:5]
        )
        parts.append(f'<div class="card"><h2>{html.escape(name)} - Headlines</h2><ul>{items}</ul></div>')

    # --- Quick links ---
    parts.append("""<div class="card"><h2>Quick Links</h2><div class="quick-links">
<a href="https://www.theverge.com" target="_blank">The Verge</a>
<a href="https://www.techmeme.com" target="_blank">Techmeme</a>
<a href="https://www.businessinsider.com" target="_blank">Business Insider</a>
<a href="https://fortune.com" target="_blank">Fortune</a>
<a href="https://www.wunderground.com/weather/us/ga/guyton" target="_blank">Weather</a>
</div></div>""")

    # --- close HTML ---
    parts.append('</section></body></html>')
    return ''.join(parts)

if __name__ == "__main__":
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(build_dashboard())
