from urllib2 import urlopen, URLError
import datetime as dt

def top_articles():
    now = dt.datetime.now()
    def ago(days=0, seconds=0):
        return now - dt.timedelta(days=days, seconds=seconds)
    articles = [
        {"title": "Google", "score": 150, "link": "http://google.com", "date": ago(seconds=60)},
        {"title": "Yahoo", "score": 75, "link": "http://yahoo.com", "date": ago(days=3)},
        {"title": "Bing", "score": 50, "link": "http://bing.com", "date": ago(days=14)},
        {"title": "NYTimes", "score": 25, "link": "http://nytimes.com", "date": ago(days=1)},
        {"title": "Fox News", "score": 15, "link": "http://foxnews.com", "date": ago(seconds=60*60)},
        {"title": "The Atlantic", "score": 5, "link": "http://theatlantic.com", "date": ago(days=24)},
    ]
    return articles

def search_articles(query):
    print "Searching ->", query
    return []

def insert_article(article):
    print "Inserting ->", article
    return True

def track_click(url):
    print "Tracking ->", url
    return True

def validate_submission(params):
    errors = {}
    def err(id, msg):
        errors[id] = msg
    title = params["title"]
    title = title.strip()
    if len(title) < 2:
        err("title", "title must be > 2 characters")
    if len(title) > 150:
        err("title", "title may not be > 150 characters")
    link = params["link"]
    link = link.strip()
    try:
        opened = urlopen(link)
        link = opened.geturl()
    except (URLError, ValueError):
        err("link", "link could not be reached")
    if len(errors) > 0:
        return (False, errors)
    else:
        return (True, errors)
