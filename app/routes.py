from flask import render_template, url_for, jsonify

from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/api/getData', methods=['GET'])
def getData():
	data = {'nama':"Ahmad Syauki"}
	return jsonify(data)