from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/www', methods=['POST'])
def index1():
    if request.method == 'POST':
        a = request.form['skala']
    return render_template('index.html',vaso=a)

app.run()
