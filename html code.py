import requests
import feedparser

rss_url = "https://feeds.feedburner.com/ndtvnews-top-stories"
response = requests.get(rss_url)
feed = feedparser.parse(response.content)

print("📰 Top NDTV Stories (via RSS):\n")
for entry in feed.entries[:5]:
    title = entry.title
    link = entry.link
    print(f"- {title}")
    print(f"  {link}\n")
