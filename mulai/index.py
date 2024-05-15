import functools
import os
import numpy as np
import pandas as pd

import time

from .kompresi import modulku, tkp

from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, send_file, send_from_directory, make_response)
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

# model
from ..extensions import db, bcrypt
from ..models.kategori import Kategori, Kuis, Responden, JawabanResponden, User, Profile

# api
from flask_restful import Resource, Api

# auth
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user


bp = Blueprint('mulai', __name__, url_prefix='/mulai')

api = Api(bp)

# -------------------------------------------- route api -----------------
class Mulai_kompres(Resource):
    def get(self):
        return {"pesan": "selamat datang"}
    
    def post(self):
        start = time.time()
        file = request.files.get("mydata")
        file_content = np.frombuffer(file.read(), dtype=np.uint8)

        aplikasiku = tkp.Aplikasiku()
        aplikasiku.tahap1(file=file_content, dari_numpy=True)
        aplikasiku.tahap2(simpan_bt=True)

        end = time.time()

        # simpan data bytes ke session
        session["hasil_kompresi"] = aplikasiku.hasil_bt
        # print(len(session["hasil_kompresi"]))

        dataku = {"data1": []}
        informasi = {
            "ukuran_awal": aplikasiku.info.ukuran_sebelum,
            "ukuran_setelah": aplikasiku.info.ukuran_setelah,
            "nilai_cr": aplikasiku.info.nilai_cr,
            "nilai_rc": aplikasiku.info.nilai_rc,
            "nilai_ss": aplikasiku.info.nilai_ss,
            "waktu" : round(end - start, 2)
        }
        
        return jsonify({
            "data": dataku,
            "informasi": informasi,
            "status": "sukses",
            "pesan": "data berhasil di proses"
        })


        # --------------------------end revisi------------------------

        # start = time.time()

        # file = request.files.get("mydata")
        # file_content = np.frombuffer(file.read(), dtype=np.uint8)
        # data1 = modulku.Mydata()
        # data1.baca_data_dari_numpy(file_content)
        # tahapan = modulku.Langkah(data1)
        # tahapan.langka1()
        # tahapan.langka2()

        # end = time.time()

        # session.clear()

        # # simpan data bytes ke session
        # session["hasil_kompresi"] = tahapan.hasil_kompresi_bt
        # print(len(session["hasil_kompresi"]))

        # dataku = {"data1": data1.df.head(10).to_json(orient='records')}
        # informasi = {
        #     "ukuran_awal": tahapan.ukuran_awal,
        #     "ukuran_setelah": tahapan.ukuran_setelah_kompresi,
        #     "nilai_cr": tahapan.cr,
        #     "nilai_rc": tahapan.rc,
        #     "nilai_ss": tahapan.ss,
        #     "waktu" : round(end - start, 2)
        # }
        
        # return jsonify({
        #     "data": dataku,
        #     "informasi": informasi,
        #     "status": "sukses",
        #     "pesan": "data berhasil di proses"
        # })
    
class DownloadFile(Resource):
    def get(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
        # df.to_csv('sample.csv', index=False)
        # return send_file('db.py', as_attachment=True)
        # return {'status': 'berhasil'}

        resp = make_response(df.to_csv())
        resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
        resp.headers["Content-Type"] = "text/csv"
        print("response adalah dibawah ini")
        return resp
    
class Dekompresi_file(Resource):
    def post(self):
        file = request.files.get("my_file")
        file_content = np.frombuffer(file.read(), dtype=np.uint8)

        aplikasiku2 = tkp.Aplikasiku()
        aplikasiku2.tahap3(dari_numpy=True, file=file_content)
        aplikasiku2.tahap4(simpan_bt=True)

        session.pop("hasil_dekompresi", None)
            
        # # simpan data bytes ke session
        session["hasil_dekompresi"] = aplikasiku2.hasil_bt

        # ------------------revisi------------------

        # tahapan_dekompresi = modulku.Tahapan_dekompresi()
        # tahapan_dekompresi.langka3(data_bytes=file)

        # filename = "hasilnya_dekompresi.pdf"
        # data_bytes = tahapan_dekompresi.hasil_dekompresi_bt

        # session.pop("hasil_dekompresi", None)
            
        # # simpan data bytes ke session
        # session["hasil_dekompresi"] = tahapan_dekompresi.hasil_dekompresi_bt

        # return ke alamat lain
        return redirect(url_for('mulai.downloadhasildekompresi'))

        # response = make_response(data_bytes)
        # response.headers['Content-Disposition'] = 'attachment; filename={}'.format(filename)
        
        # print("file data: ")
        # print(data_bytes)

        # return {"pesan": "berhasil"}
        # return send_from_directory(directory, nama_file, as_attachment=True)
        # return response
    
class DownloadHasilKompresi(Resource):
    def get(self):
        filename = "hasil_kompresi.pdf"

        # print("hasil kompresi")
        # print(session["hasil_kompresi"])

        data_bytes = session["hasil_kompresi"]

        response = make_response(data_bytes)
        response.headers['Content-Disposition'] = 'attachment; filename={}'.format(filename)
        
        # print("file data: ")
        # print(data_bytes)

        # return {"pesan": "berhasil"}
        # return send_from_directory(directory, nama_file, as_attachment=True)
        return response

class DownloadHasilDekompresi(Resource):
    def get(self):
        if 'hasil_dekompresi' not in session:
            raise Exception("tidak ada nama di sesion")
        
        filename = "hasil_dekompresi.pdf"

        # print("hasil kompresi")
        # print(session["hasil_kompresi"])

        data_bytes = session["hasil_dekompresi"]

        response = make_response(data_bytes)
        response.headers['Content-Disposition'] = 'attachment; filename={}'.format(filename)
        
        # print("file data: ")
        # print(data_bytes)

        # return {"pesan": "berhasil"}
        # return send_from_directory(directory, nama_file, as_attachment=True)
        return response


class Kategori_api(Resource):
    def get(self):

        kat = Kategori.query.all()
        list_kategori = []
        for i in kat:
            kat_dict = {
                'id': i.id,
                'kategori': i.kategori
            }
            list_kategori.append(kat_dict)

        return jsonify(list_kategori)
    
    def post(self):
        # --- tambah data-----
        kt = request.form['kategori'];
        input_data = Kategori(kategori=kt)
        db.session.add(input_data)
        db.session.commit()

        return {"pesan": "berhasil disimpan"}, 200
    
class Kuis_api(Resource):
    def get(self):

        kat = Kuis.query.all()
        mylist = []
        for i in kat:
            mydict = {
                'id': i.id,
                'teks': i.teks,
                'id_kategori': i.kategori.id,
                'date_created': i.date_created
            }
            mylist.append(mydict)
        
        return jsonify(mylist)
    
    def post(self):
        # --- tambah data-----
        teks = request.form['teks'];
        id_kategori = request.form['kategori'];

        kat = db.get_or_404(Kategori, id_kategori)
        print(f"yang ini: {kat.id}")

        input_data = Kuis(teks=teks, kategori_id=kat.id)
        db.session.add(input_data)
        db.session.commit()

        return {"pesan": "berhasil disimpan"}, 200
    
class Hapus_kategori_api(Resource):
    def get(self, id):
        kategori = db.get_or_404(Kategori, id)
        
        # hapus kategori
        db.session.delete(kategori)
        db.session.commit()

        return {"pesan": "berhasil dihapus"}, 200
    
    def post(self):
        # --- tambah data-----
        # kt = request.form['kategori'];
        # input_data = Kategori(kategori=kt)
        # db.session.add(input_data)
        # db.session.commit()

        return {"pesan": "berhasil disimpan"}, 200
    
class Jawaban_responden(Resource):
    def get(self):
        return {"pesan": "oke"}, 200
    
    # simpan jawaban responden
    def post(self):
        mydata = request.json

        biodata = mydata['biodata']
        jawaban = mydata['jawaban']
        # bukti_ = mydata['bukti_']

        # simpan responden
        responden = Responden.query.filter_by(nama=biodata["nama"], nip=biodata["nip"]).first()
        if responden: # jika sudah ada di database
            print("responden baru")
        else:
            responden = Responden(nama=biodata["nama"], nip=biodata["nip"], jabatan=biodata["jabatan"], asal_instansi=biodata["asal_instansi"], no_hp=biodata["no_hp"], email=biodata["email"])
            db.session.add(responden)
            db.session.commit()
            print("data responden berhasil disimpan")

        arr = []

        print(jawaban)

        for i, v in jawaban.items():
            kuis = db.get_or_404(Kuis, i)
            temp = JawabanResponden.query.filter_by(responden_id=responden.id, kuis_id=kuis.id).first()
            if not temp:
                temp = JawabanResponden(responden_id=responden.id, kuis_id=kuis.id, jawaban=v)
            else:
                temp.jawaban = v

            arr.append(temp)

        # simpan jawaban banyak
        if arr:
            db.session.add_all(arr)
            db.session.commit()
        
        return {"pesan": "mantap"}, 200
    
class Hapus_kuis_api(Resource):
    def get(self, id):
        kuis = db.get_or_404(Kuis, id)
        
        # hapus kuis
        db.session.delete(kuis)
        db.session.commit()

        return {"pesan": "berhasil dihapus"}, 200
    
class Kumpulan_kuis(Resource):
    def get(self):

        kat = Kuis.query.all()
        mylist = []
        for i in kat:
            mydict = {
                'id': i.id,
                'teks': i.teks
                # 'id_kategori': i.kategori.id,
                # 'date_created': i.date_created
            }
            mylist.append(mydict)
        
        return jsonify(mylist)

# ini adalah route untuk api
api.add_resource(Mulai_kompres, '/mulaikompresi')
api.add_resource(DownloadFile, '/downloadfile')
api.add_resource(Dekompresi_file, '/dekompresifile')
api.add_resource(DownloadHasilKompresi, '/downloadhasilkompresi')
api.add_resource(DownloadHasilDekompresi, '/downloadhasildekompresi')

# api staf (admin)
api.add_resource(Kategori_api, '/kategori_api')
api.add_resource(Kuis_api, '/kuis_api')
api.add_resource(Hapus_kategori_api, '/hapus_kategori/<int:id>')
api.add_resource(Hapus_kuis_api, '/hapus_kuis/<int:id>')

# api responden
api.add_resource(Kumpulan_kuis, '/kumpulan_kuis')
api.add_resource(Jawaban_responden, '/jawaban_responden')

# -------------------------------------------- end api -----------------


# -------------------- route pimpinan ----------------- #


# -------------------- route staf (admin) ----------------- #

@bp.route("/staf", methods=["GET"])
def index_staf():
    context = {}
    return render_template("staf/index.html", **context)

@bp.route("/edit_kategori/<int:id>", methods=["GET", "POST"])
def edit_kategori(id):
    if request.method == "GET":
        kategori = db.get_or_404(Kategori, id)

        context = {
            "kategori" :  kategori
        }
        return render_template("staf/edit_kategori.html", **context)

    if request.method == "POST":
        
        # update data kategori
        kategori = db.get_or_404(Kategori, id)
        kategori.kategori = request.form["kategori"]
        db.session.commit()
        
        return redirect(url_for('mulai.halaman_kategori'))

@bp.route("/edit_kuis/<int:id>", methods=["GET", "POST"])
def edit_kuis(id):
    if request.method == "GET":
        kuis = db.get_or_404(Kuis, id)

        context = {
            "kuis" :  kuis
        }
        return render_template("staf/edit_kuis.html", **context)

    if request.method == "POST":
        teks = request.form["teks"]
        id_kategori = request.form["id_kategori"]
        print(f"id-kategori: {id_kategori}")

        kat = db.get_or_404(Kategori, id_kategori)
        
        # update data kategori
        kuis = db.get_or_404(Kuis, id)
        kuis.teks = teks
        kuis.kategori_id = kat.id
        db.session.commit()
        
        return redirect(url_for('mulai.halaman_kuis'))


@bp.route("/kategori", methods=["GET"])
def halaman_kategori():
    context = {}
    return render_template("staf/kategori.html", **context)

@bp.route("/kuis", methods=["GET"])
def halaman_kuis():
    context = {}
    return render_template("staf/kuis.html", **context)

@bp.route("/responden", methods=["GET"])
def halaman_responden():
    context = {}
    return render_template("responden/responden.html", **context)

@bp.route("/pimpinan", methods=["GET"])
def halaman_pimpinan():
    if current_user.is_authenticated:
        pass
    else:
        return redirect(url_for("mulai.halaman_login"))

    jawaban_responden = JawabanResponden.query.all()
    kuis = Kuis.query.all()
    data = []
    for k in kuis:
        for j in k.jawaban:
            data.append({"kategori": k.kategori.kategori, "teks": k.teks, "jawaban": j.jawaban, "responden": j.responden.nama})
            
            # print(f"Responden: {j.responden.nama}")

    laporan = pd.DataFrame(data)
    laporan.sort_values(by=["kategori", "responden"], inplace=True, ascending=True)
    laporan = laporan.to_dict(orient="records")

    context = {
        "laporan": laporan
    }
    return render_template("pimpinan/pimpinan.html", **context)

@bp.route("/login", methods=["GET", "POST"])
def halaman_login():
    if request.method == "GET":
        context = {}
        return render_template("login.html", **context)
    
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter(User.username == username, User.password == password).first()

        if user:
            login_user(user)
            return redirect(url_for("mulai.halaman_pimpinan"))

        context = {}

        return render_template("login.html", **context)

@bp.route("/logout", methods=["GET"])
def halaman_logout():
    logout_user()
    return redirect(url_for("mulai.halaman_login"))

# -------------------- route responden ----------------- #


@bp.route('', methods=["GET", "POST"])
def halaman_mulai():
    if request.method == 'POST':
        print("selamat ini adalah post")
        file = request.files.get("mydata")
        file_content = np.frombuffer(file.read(), dtype=np.uint8)

        data1 = modulku.Mydata()
        data1.baca_data_dari_numpy(file_content)
        tahapan = modulku.Langkah(data1)
        tahapan.langka1()


    nama= "budi"
    context = {
        "nama": nama
    }
    return render_template("mulai/index.html", **context)

