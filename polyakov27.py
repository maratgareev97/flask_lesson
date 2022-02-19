from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def test():
    return render_template('polykov27.html')

@app.route('/otvet', methods=["POST", "GET"])
def test1():
    if request.method == 'POST':
        a = int(request.form['a'])
    if request.method == 'POST':
        b = int(request.form['b'])
    t = a
    x = 0
    p=10**7
    for t in range(a,b+1):
        c = t%2
        d = t%4
        if c==d and (t%13==0 or t%14==0 or t%15==0):
            x+=1
            if t<p:
                p = t
    print(x, p)
 #   s = x + ", " + int(p)
    return render_template('polykov27.html', s=str(x) + ", " + str(p))

app.run()