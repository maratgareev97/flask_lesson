from flask import Flask, render_template, request,redirect,url_for,send_file,flash, session, Response,g,session

app = Flask(__name__)

@app.route('/')
def index():
    vvv=0
    return render_template('test_site.html',vvv=vvv)

@app.route('/fio',methods=['POST','GET'])
def fio():
    if request.method=='POST':
        fio = request.form['fio']
        print(fio)
        return redirect('/'+fio)
    else:
        user = request.args.get('fio')+'1111'
        print(user)
    return render_template('test_site.html')

@app.route('/<vvv>')
def index1(vvv):
    return render_template('test_site.html',vvv=vvv)
'''
@app.route('/quest1')
def quest1():
    return render_template('quest1.html')
'''
@app.route('/quest1',methods=['POST','GET'])
def quest1():
    x=0
    if request.method=="POST":
        q1 = request.form.getlist('q1') # правильный ответ
        q2 = request.form.getlist('q2')
        q3 = request.form.getlist('q3')
        q4 = request.form.getlist('q4')
        s=len(q1)+len(q2)+len(q3)+len(q4)
        if len(q1)!=0 and s==1:
            if len(q1[0]):
                x+=1
                print(x)
        return redirect('/quest2_'+str(x))
    return render_template('quest1.html')
'''
@app.route('/quest2_<x>')
def quest2(x):
    return render_template('quest1.html')
'''
@app.route('/quest2_<x>',methods=['POST','GET'])
def quest2_(x):
    x=int(x)
    if request.method=="POST":
        q1 = request.form.getlist('q1')
        q2 = request.form.getlist('q2') # правильный ответ
        q3 = request.form.getlist('q3')
        q4 = request.form.getlist('q4')
        s = len(q1) + len(q2) + len(q3) + len(q4)
        if len(q2) != 0 and s == 1:
            if q2[0]=="1":
                x=x+1
        return redirect('/quest3_'+str(x))
    return render_template('quest2.html',x=x)

@app.route('/quest3_<x>',methods=['POST','GET'])
def quest3_(x):
    x=int(x)
    if request.method=="POST":
        q1 = request.form.getlist('q1')
        q2 = request.form.getlist('q2')
        q3 = request.form.getlist('q3')
        q4 = request.form.getlist('q4') #правильный ответ
        s = len(q1) + len(q2) + len(q3) + len(q4)
        if len(q4) != 0 and s == 1:
            if q4[0]=="1":
                x+=1
        return redirect('/finish_'+str(x))
    return render_template('quest3.html',x=x)

@app.route('/finish_<x>',methods=['POST','GET'])
def finish_(x):
    return render_template('finish.html',x=x)

app.run()