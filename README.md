# Auto Feed Updater

A Python script that aggregates RSS feeds from various sources (Hacker News, GitHub Blog, and ESPN Cricinfo) into a single, beautifully styled HTML page.

## Features

- Fetches RSS feeds from multiple sources
- Handles connection timeouts gracefully
- Displays latest 5 entries from each feed
- Modern, dark-themed UI with hover effects
- Responsive design for all devices
- UTC timestamps for consistency

## Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/Auto-Feed-Updater.git
cd Auto-Feed-Updater
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the script:
```bash
python update_feeds.py
```

The script will generate an `index.html` file that you can open in your browser.

## Customization

You can modify the `FEEDS` list in `update_feeds.py` to add or remove RSS feeds.

## License

MIT License 