from datetime import datetime
import feedparser
import socket

FEEDS = [
    'https://news.ycombinator.com/rss',
    'https://github.blog/feed/',
    'https://www.espncricinfo.com/rss/content/story/feeds/6.xml'  # ESPN Cricinfo
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Feed Updates</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{
            max-width: 800px;
            margin: 20px auto;
            padding: 0 20px;
            font-family: system-ui;
            background-color: #000000;
            color: #ffffff;
        }}
        .container {{
            background-color: #1a1a1a;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }}
        h1 {{ color: #4CAF50; }}
        .feed {{
            margin-bottom: 30px;
            border-left: 3px solid #4CAF50;
            padding-left: 15px;
        }}
        .entry {{
            margin: 15px 0;
            padding: 12px;
            background-color: #262626;
            border-radius: 5px;
            transition: transform 0.2s;
        }}
        .entry:hover {{
            transform: translateX(5px);
        }}
        .timestamp {{
            color: #888;
            font-size: 0.85em;
            display: block;
            margin-top: 5px;
        }}
        a {{
            color: #4CAF50;
            text-decoration: none;
        }}
        a:hover {{
            color: #45a049;
            text-decoration: underline;
        }}
        .error {{
            color: #ff4444;
            background-color: #330000;
            padding: 15px;
            border-radius: 5px;
            margin: 15px 0;
        }}
    </style>
</head>
<body>
    <h1>📰 Sports Feed Updates ({timestamp})</h1>
    <div class="container">
        {content}
    </div>
</body>
</html>
"""


def parse_feed_with_timeout(url, timeout=10):
    """Parse feed with socket-level timeout"""
    original_timeout = socket.getdefaulttimeout()
    socket.setdefaulttimeout(timeout)
    try:
        return feedparser.parse(url)
    finally:
        socket.setdefaulttimeout(original_timeout)

def update_feeds():
    content = ""
    
    for url in FEEDS:
        try:
            # Use our custom timeout-enabled parser
            feed = parse_feed_with_timeout(url)
            
            if feed.bozo:  # Check for feed parsing errors
                raise Exception(f"Feed error: {feed.bozo_exception}")
                
            feed_content = f'<div class="feed"><h2>{feed.feed.title}</h2>'
            
            for entry in feed.entries[:5]:
                time_note = ""
                if hasattr(entry, 'published_parsed'):
                    entry_time = datetime(*entry.published_parsed[:6])
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
        timestamp=datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        content=content
    )
    
    with open("index.html", "w") as f:
        f.write(full_html)

if __name__ == "__main__":
    update_feeds()