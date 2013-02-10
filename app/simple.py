from flask import render_template, Flask
app = Flask(__name__)

def top_articles():
    articles = [
        {"title": "Google", "score": 150, "link": "http://google.com"},
        {"title": "Yahoo", "score": 75, "link": "http://yahoo.com"},
        {"title": "Bing", "score": 50, "link": "http://bing.com"}
    ]
    return articles

@app.route('/')
def index():
    articles = top_articles()
    return render_template("index.jinja2.html", rows=articles)

if __name__ == "__main__":
    app.run(debug=True)
