from flask import render_template
from flask import Flask
app = Flask(__name__)

from article_lister2 import get_articles

@app.route('/')
def home(articles=None):
    return render_template('index.html', articles=get_articles('hippocampus'))
