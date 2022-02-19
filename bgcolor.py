from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=["POST","GET"])
def index():
    if request.method == 'POST':
        if request.form.get("color_body"):
            color1=request.form['color_str']
            print("Вы отправили цвет ",color1)
            return render_template('bgcolor.html',color1=color1)
        if request.form.get("color_font"):
            color1=request.form['color_str']
            print("Вы отправили цвет ",color1)
            return render_template('bgcolor.html',color2=color1)
    return render_template('bgcolor.html')
app.run()
