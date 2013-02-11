def top_articles():
    articles = [
        {"title": "Google", "score": 150, "link": "http://google.com"},
        {"title": "Yahoo", "score": 75, "link": "http://yahoo.com"},
        {"title": "Bing", "score": 50, "link": "http://bing.com"}
    ]
    articles = articles * 3
    return articles

def search_articles(query):
    return []

def insert_article(article):
    return False
