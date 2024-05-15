from ..extensions import db
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from datetime import datetime

# assosiasi tabel
# kuis_responden = db.Table("kuis_responden",
#     db.Column("kuis_id", db.Integer, db.ForeignKey("kuis.id"), primary_key=True),
#     db.Column("responden_id", db.Integer, db.ForeignKey("responden.id"), primary_key=True),
# )

class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    profile = db.relationship("Profile", backref="user", uselist=False)

    def get_id(self):
        return self.id

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)

class Kategori(db.Model):
    __tablename__ = "kategori"
    id = db.Column(db.Integer, primary_key=True)
    kategori = db.Column(db.String(100))
    kuis = db.relationship('Kuis', backref='kategori', lazy=True, cascade='all, delete-orphan')
    date_created = db.Column(db.DateTime, default=datetime.now)
    date_modified = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

class Kuis(db.Model):
    __tablename__ = "kuis"
    id = db.Column(db.Integer, primary_key=True)
    teks = db.Column(db.String(200))
    date_created = db.Column(db.DateTime, default=datetime.now)
    kategori_id = db.Column(db.Integer, db.ForeignKey('kategori.id', ondelete="CASCADE"), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)
    date_modified = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    jawaban = db.relationship("JawabanResponden", backref="kuis", lazy=True)

class Responden(db.Model):
    __tablename__ = "responden"
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(50), nullable=False)
    nip = db.Column(db.String(50), nullable=False)
    jabatan = db.Column(db.String(50), nullable=False)
    asal_instansi = db.Column(db.String(50), nullable=False)
    no_hp = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)
    jawaban = db.relationship('JawabanResponden', backref="responden", lazy=True)

    

class JawabanResponden(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    responden_id = db.Column(db.Integer, db.ForeignKey('responden.id'), nullable=False)
    kuis_id = db.Column(db.Integer, db.ForeignKey('kuis.id'), nullable=False)
    jawaban = db.Column(db.String(50))
    bukti_pelaksanaan = db.Column(db.String(50), default="", nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.now)

    