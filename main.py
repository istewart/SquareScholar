from flask import render_template
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

from article_lister2 import get_articles
from histograms import get_histos

@app.route('/')
def home():
	term = request.args.get('term')
	if not term:
		term = 'hippocampus'

	return render_template('index.html', articles=get_articles(term))

@app.route('/topics')
def topics():
	term = request.args.get('term')
	if not term:
		term = 'hippocampus'

	return jsonify(get_histos(term))
