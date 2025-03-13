import feedparser
from datetime import datetime

# Example: Fetch RSS feeds
FEEDS = [
    'https://news.ycombinator.com/rss',
    'https://github.blog/feed/'
]

def update_feeds():
    content = "# Latest Updates\n\n"
    for url in FEEDS:
        feed = feedparser.parse(url)
        content += f"## {feed.feed.title}\n"
        for entry in feed.entries[:5]:  # Latest 5 items
            content += f"- [{entry.title}]({entry.link})\n"
        content += "\n"
    
    with open("feed.md", "w") as f:
        f.write(f"Updated at {datetime.now().isoformat()}\n\n{content}")

if __name__ == "__main__":
    update_feeds()