from datetime import datetime
import feedparser

FEEDS = [
    'https://news.ycombinator.com/rss',
    'https://github.blog/feed/'
]

def update_feeds():
    content = f"# Feed Updates ({datetime.now().strftime('%Y-%m-%d %H:%M')})\n\n"
    
    for url in FEEDS:
        try:
            feed = feedparser.parse(url)
            content += f"## {feed.feed.title}\n"
            
            for entry in feed.entries[:5]:  # Always show latest 5
                # Add timestamp if available
                if hasattr(entry, 'published_parsed'):
                    entry_time = datetime(*entry.published_parsed[:6])
                    time_diff = (datetime.now() - entry_time).days
                    time_note = f" ({entry_time.strftime('%Y-%m-%d')})" if time_diff >= 1 else ""
                else:
                    time_note = ""
                
                content += f"- [{entry.title}]({entry.link}){time_note}\n"
            
            content += "\n"
        
        except Exception as e:
            content += f"⚠️ Error fetching {url}: {str(e)}\n\n"
    
    with open("feed.md", "w") as f:
        f.write(content)

if __name__ == "__main__":
    update_feeds()