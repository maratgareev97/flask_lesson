import sqlite3
from flask import Flask, render_template, request,redirect,url_for,send_file,flash, session, Response,g,session

app = Flask(__name__)

def create_base():
    connect = sqlite3.connect('base/lesson1.db')
    return connect

def create_table():
    #create_base()
    name='table_first'
    cursor = create_base().cursor()
    try:
        cursor.execute('CREATE TABLE {}(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"text" TEXT(1000), "number" INTEGER);'.format(name))
        create_base().commit()
        print('Таблица создана')
    except:
        print("Таблица уже создана")


@app.route('/',methods=['POST','GET'])
def index():
    connection= create_base()
    print('База создана')
    create_table()
    cursor = create_base().cursor()
    name_table='table_first'
    cursor.execute("SELECT * FROM {}".format(name_table))
    rows = cursor.fetchall()
    print(rows)

    if request.method == "POST":
        if request.form.get('choose'):
            display_type = request.form.get("display_type", None)
            print(display_type)
        if request.form.get('add'):

            #connection = create_base()

            cursor = connection.cursor()

            print('ADD')
            text='5555555'
            number=444
            #cursor.execute("INSERT INTO table_first (id,'text','number') VALUES(NULL, ?, ?)", (text,number))
            cursor.execute("INSERT INTO table_first (text,number) VALUES('477', 12);")
            connection.commit()
    create_base().close()
    return render_template('base.html',rows=rows)

app.run()