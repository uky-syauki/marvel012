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


@app.route('/api/postData', methods=['POST'])
def postData():
	nama_lengkap = request.form.get('nama_lengkap')
	add_calgot = calgot(
		nama_lengkap=request.form.get('nama_lengkap'),
		nama_panggilan=request.form.get('nama_panggilan'),
		jenis_kelamin=request.form.get('jenis_kelamin'),
		email=request.form.get('email'),
		nomor_wa=request.form.get('nomor_wa'),
		alamat=request.form.get('alamat'),
		kampus=request.form.get('kampus'),
		alasan=request.form.get('alasan')
	)
	db.session.add(add_calgot)
	db.session.commit()
	# print(nama_lengkap)
	# data = request.get_json()
	# respon = {'pesan':f'Data Telah diterima, data:{data}'}
	# print(data)
	# print(data.keys())
	return {'status': 'success'}