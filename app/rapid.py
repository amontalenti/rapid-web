from urllib2 import urlopen, URLError

def top_articles():
    articles = [
        {"title": "Google", "score": 150, "link": "http://google.com"},
        {"title": "Yahoo", "score": 75, "link": "http://yahoo.com"},
        {"title": "Bing", "score": 50, "link": "http://bing.com"}
    ]
    articles = articles * 3
    return articles

def search_articles(query):
    print "Searching ->", query
    return []

def insert_article(article):
    print "Inserting ->", article
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
