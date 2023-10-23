from flask import render_template, url_for, jsonify, request

from app import app, db
from app.models import calgot
from app.forms import CalgotForm

import os

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/newDaftar', methods=['GET','POST'])
def newDaftar():
	form = CalgotForm()
	return render_template('daftar2.html', form=form)


@app.route('/pendaftar')
def pendaftar():
	return render_template('pendaftar.html')

@app.route('/daftar')
def daftar():
	return render_template('daftar2.html')



@app.route('/api/getData', methods=['GET'])
def getData():
	daftar_calgot = calgot.query.all()
	# for isi in daftar_calgot:
	# 	print(isi.id)
	data_jsom = []
	for baris in daftar_calgot:
		data_jsom.append({
			'id':baris.id,
			'nama_lengkap':baris.nama_lengkap,
			'nama_panggilan':baris.nama_panggilan,
			'jenis_kelamin':baris.jenis_kelamin,
			'nomor_wa':baris.nomor_wa,
			'email':baris.email,
			'alamat':baris.alamat,
			'kampus':baris.kampus,
			'jurusan':baris.jurusan,
			'foto':baris.foto[11:],
			'tanggal':baris.timestamp,
			'alasan':baris.alasan
		})
	return jsonify(data_jsom)


@app.route('/api/postData', methods=['GET','POST'])
def postData():
	nama_lengkap = request.form.get('nama_lengkap')
	try:
		photo = request.files['photo']
		nama_lengkap = nama_lengkap.replace(' ','_').replace(',','').replace('.','')
		photo_path = os.path.join("app/static/foto_calgot", nama_lengkap+'.jpg')
		photo.save(photo_path)
		add_calgot = calgot(
			nama_lengkap=request.form.get('nama_lengkap'),
			nama_panggilan=request.form.get('nama_panggilan'),
			jenis_kelamin=request.form.get('jenis_kelamin'),
			email=request.form.get('email'),
			nomor_wa=request.form.get('nomor_wa'),
			alamat=request.form.get('alamat'),
			kampus=request.form.get('kampus'),
			jurusan=request.form.get('jurusan'),
			foto=photo_path,
			alasan=request.form.get('alasan')
		)
		db.session.add(add_calgot)
		db.session.commit()
		print(f"Calgot {nama_lengkap} berhasil di daftar")
		return {'status': 'success'}
	except:
		return {'status': 'error'}

	
	

	# db.session.add(add_calgot)
	# db.session.commit()
	# print(nama_lengkap)
	# print(nama_lengkap)
	# data = request.get_json()
	# respon = {'pesan':f'Data Telah diterima, data:{data}'}
	# print(data)
	# print(data.keys())