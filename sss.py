from flask import Flask, render_template, request, redirect, url_for, send_file, flash, session, Response, g, session

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        n = int(request.form["name1"])
        color = request.form["name2"]
    s = 0
    i = 1
    while n > 0:
        ost = n % 10
        n = n // 10
        if ost % 2 == 0:
            s = s + ost
            i = i + 1
    return render_template('index.html', s=s/(i-1), color=color)

app.run()