from app import db
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


class calgot(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nama_lengkap = Column(String(64))
    nama_panggilan = Column(String(64))
    jenis_kelamin = Column(String(10))
    nomor_wa = Column(String(15))
    email = Column(String(64))
    alamat = Column(String(128))
    kampus = Column(String(64))
    jurusan = Column(String(20))
    foto = Column(String(64), default="tidak_ada.jpg")
    alasan = Column(String(120))
    timestamp = Column(DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"<Calgot {self.nama_panggilan}"

