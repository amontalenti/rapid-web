from flask import Flask, render_template, request
from rapid import (top_articles, search_articles, insert_article)
from filters import val_ago

app = Flask(__name__, static_folder="../static", static_url_path="/static")

@app.route('/')
def index():
    articles = top_articles()
    return render_template('index.jinja2.html', 
                           rows=articles,
                           page_links="active")

@app.route('/search/<query>')
def search(query):
    articles = search_articles(query)
    return render_template('index.jinja2.html', 
                           query=query, 
                           articles=articles)

@app.route('/submit/', methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        return do_submit()
    else:
        return render_template('submit.jinja2.html',
                               page_submit="active")

def do_submit():
    form = request.form
    submission = dict(
        title=form["title"],
        link=form["link"]
    )
    article = insert_article(submission)
    return render_template("success.jinja2.html",
                           page_submit="active")

def run_devserver():
    app.run(debug=True)

if __name__ == "__main__":
    run_devserver()
