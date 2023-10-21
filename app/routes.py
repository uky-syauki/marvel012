from flask import render_template, url_for, jsonify, request

from app import app, db
from app.models import calgot

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/api/getData', methods=['GET'])
def getData():
	data = {'nama':"Ahmad Syauki"}
	return jsonify(data)


@app.route('/api/postData', methods=['POST','GET'])
def postData():
	nama_lengkap = request.form.get('nama_lengkap')
	print(nama_lengkap)
	# data = request.get_json()
	# respon = {'pesan':f'Data Telah diterima, data:{data}'}
	# print(data)
	# print(data.keys())
	return {'status': 'success'}