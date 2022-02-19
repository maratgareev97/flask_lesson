import sqlite3
from flask import Flask, render_template, request,redirect,url_for,send_file,flash, session, Response,g,session

app = Flask(__name__)

def createtable():
    connect = sqlite3.connect('base/booook.db')

    cursor = connect.cursor()
    col_text = 'name'
    col_int = 'nomer'

    cursor.execute('CREATE TABLE "table1" (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,{} TEXT(1000), {} INTEGER);'.format(col_text, col_int))

    connect.commit()
    connect.close()

@app.route('/', methods=["POST","GET"])
def index():

    connect = sqlite3.connect('base/booook.db')
    cursor = connect.cursor()


    if request.method == "POST":
        if request.form.get('add'):
            name = request.form['name']
            nomer = request.form['nomer']
            cursor.execute("INSERT INTO 'table1' (name,nomer) VALUES(?,?)", (name, nomer))
            connect.commit()
            connect.close()

        if request.form.get('delete'):

            if request.form.get('pick') != "-1":
                id = request.form['pick'][1:len(request.form['pick'])-1:]
                cursor.execute("DELETE FROM 'table1' WHERE id = ?", (id,))
            else:
                name = request.form['name']
                cursor.execute("DELETE FROM 'table1' WHERE name = ?", (name,))

            connect.commit()
            connect.close()

        if request.form.get('edit'):

            id = request.form['pick'][1:len(request.form['pick']) - 1:]
            name = request.form['name']
            nomer = request.form['nomer']

            if name=="" and nomer!="":
                cursor.execute("UPDATE table1 SET nomer=? WHERE id=?", (nomer, id))
            elif name!="" and nomer=="":
                cursor.execute("UPDATE table1 SET name=? WHERE id=?", (name, id))
            elif name=="" and nomer=="":
                pass
            else:
                cursor.execute("UPDATE table1 SET name=?, nomer=? WHERE id=?", (name, nomer, id))

            connect.commit()
            connect.close()

        return redirect('/')



    cursor.execute("SELECT * FROM 'table1'")
    colu = cursor.fetchall()
    connect.close()
    return render_template('booook.html',colu=colu)


app.run()