from flask import render_template, url_for, jsonify, request

from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/api/getData', methods=['GET'])
def getData():
	data = {'nama':"Ahmad Syauki"}
	return jsonify(data)


@app.route('/api/postData', methods=['POST'])
def postData():
	data = request.get_json()
	respon = {'pesan':'Data Telah diterima'}
	return jsonify(respon)