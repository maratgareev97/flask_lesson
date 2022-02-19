#!pip install flask-ngrok # установка приложения ngrock

from flask import Flask,render_template,request
#from flask_ngrok import run_with_ngrok

app=Flask(__name__)
#run_with_ngrok(app)


@app.route('/')
def urav():
    return render_template('urav.html')

@app.route('/otvet',methods=['POST'])
def urav1():
    if request.method == 'POST':
        a = int(request.form['a'])
        b = int(request.form['b'])
        print(a,b)
        if a!=0:
            x=b/a
            print(x)
        else:
            x='Нет корней'
            print('нет корней')
    return render_template('urav.html',x=x)

app.run()