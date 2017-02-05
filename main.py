from flask import render_template
from flask import Flask
from flask import jsonify

app = Flask(__name__)

from article_lister2 import get_articles
from histograms import get_histos

@app.route('/')
def home():
    return render_template('index.html', articles=get_articles('hippocampus'))

@app.route('/topics')
def topics():
    # print(get_histos('hippocampus'))
    return jsonify(get_histos('hippocampus'))
