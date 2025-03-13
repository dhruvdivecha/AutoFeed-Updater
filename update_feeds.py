from datetime import datetime
import feedparser

FEEDS = [
    'https://news.ycombinator.com/rss',
    'https://github.blog/feed/'
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Feed Updates</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{ max-width: 800px; margin: 20px auto; padding: 0 20px; font-family: system-ui; }}
        h1 {{ color: #2c3e50; }}
        .feed {{ margin-bottom: 30px; }}
        .entry {{ margin: 10px 0; }}
        .timestamp {{ color: #7f8c8d; font-size: 0.9em; }}
        a {{ color: #2980b9; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>📰 Feed Updates ({timestamp})</h1>
    {content}
</body>
</html>
"""

def update_feeds():
    content = ""
    
    for url in FEEDS:
        try:
            feed = feedparser.parse(url, request_timeout=10)
            
            if feed.bozo:
                raise Exception(f"Feed error: {feed.bozo_exception}")
                
            feed_content = f'<div class="feed"><h2>{feed.feed.title}</h2>'
            
            for entry in feed.entries[:5]:
                time_note = ""
                if hasattr(entry, 'published_parsed'):
                    entry_time = datetime(*entry.published_parsed[:6])
                    time_diff = (datetime.now() - entry_time).days
                    time_note = f'<span class="timestamp">{entry_time.strftime("%Y-%m-%d %H:%M")}</span>'
                
                feed_content += f'''
                <div class="entry">
                    <a href="{entry.link}" target="_blank">{entry.title}</a>
                    {time_note}
                </div>
                '''
            
            content += feed_content + '</div>'
        
        except Exception as e:
            content += f'<div class="error">⚠️ Error fetching {url}: {str(e)}</div>'
    
    full_html = HTML_TEMPLATE.format(
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M"),
        content=content
    )
    
    with open("index.html", "w") as f:
        f.write(full_html)

if __name__ == "__main__":
    update_feeds()