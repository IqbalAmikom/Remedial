from flask import *
from mysql import connector

app = Flask(__name__)

#open connection
db = connector.connect(
    host    = 'localhost',
    user    = 'root',
    passwd  = '',
    database= 'db_sample_api_0563'
)
@app.route('/admin')
def admin():
    cursor = db.cursor()
    cursor.execute('select * from tbl_students_0563')
    result = cursor.fetchall()
    cursor.close()
    return render_template('admin.html', hasil = result)

@app.route('/')
def main():
    cursor = db.cursor()
    cursor.execute('select * from tbl_students_0563')
    result = cursor.fetchall()
    cursor.close()
    return render_template('main.html', hasil = result)
    
@app.route('/tambah/')
def tambah_data():
    return render_template('tambah.html')

@app.route('/proses_tambah/', methods=['POST'])
def proses_tambah():
    nim = request.form['nim']
    nama = request.form['nama']
    jk = request.form['jk']
    jurusan = request.form['prodi']
    daerah = request.form['daerah']
    cur = db.cursor()
    cur.execute('INSERT INTO tbl_students_0563 (nim, nama, jk, prodi, asal) VALUES (%s, %s, %s, %s, %s)', (nim, nama, jk, jurusan, daerah))
    db.commit()
    return redirect(url_for('admin'))

@app.route('/edit/<id>', methods=['GET'])
def ubah_data(id):
    cur = db.cursor()
    cur.execute('select * from tbl_students_0563 where id=%s', (id,))
    res = cur.fetchall()
    cur.close()
    return render_template('edit.html', hasil=res)

@app.route('/editing_data/', methods=['POST'])
def proses_ubah():
    idid = request.form['id0']
    formid = request.form['id']
    nim = request.form['nim']
    nama = request.form['nama']
    jk = request.form['jk']
    prodi = request.form['prodi']
    asal = request.form['daerah']
    cur = db.cursor()
    sql = "UPDATE tbl_students_0563 SET id=%s, nim=%s, nama=%s, jk=%s, prodi=%s, asal=%s WHERE id=%s"
    value = (formid, nim, nama, jk, prodi, asal, idid)
    cur.execute(sql, value)
    db.commit()
    return redirect(url_for('admin'))

@app.route('/hapus/<id>', methods=['GET'])
def hapus_data(id):
    cur = db.cursor()
    cur.execute('DELETE from tbl_students_0563 where id=%s', (id,))
    db.commit()
    return redirect(url_for('admin'))
if __name__ == '__main__':
    app.run()