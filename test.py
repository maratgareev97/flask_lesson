from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def test():
    return render_template('test.html')


@app.route('/www', methods=["POST", "GET"])
def test1():
    if request.method == 'POST':
        a = request.form['a']
        if request.form.get('a'):
            s=a+"1"
        if request.form.get('b'):
            s=a+"2"
        #return redirect(a)
    return render_template('test.html',s=s)


@app.route('/<vvv>')
def index(vvv):
    return render_template('test.html', vvv=vvv)


app.run()
