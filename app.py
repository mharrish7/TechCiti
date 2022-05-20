
from flask import Flask, g, jsonify,render_template,request,redirect,session
import sqlite3






def get_U():
    con = sqlite3.connect('US.db')
    cursor = con.cursor()
    cursor.execute('select * from USPW1')
    Users = []
    for i in cursor:
        Users.append(i)
    return Users

app = Flask(__name__)
app.secret_key = "harrish"
#session['user'] = 'nologin'

Users = get_U()

@app.route('/')
def home():
    session['user'] = 'nologin'
    return render_template('index.html')

@app.route('/register')
def reg():
    return render_template('register.html')

@app.route('/log',methods = ['POST'])
def log():
    em = request.form['et']
    pw = request.form['pt']
    Users = get_U()
    if (em,pw) in Users:
        session['user'] = em
        return jsonify({'login': True})
    else:
        return jsonify({'login': False})


@app.route('/reg',methods = ['POST'])
def regs():
    try:
        con = sqlite3.connect('US.db')
        cursor = con.cursor()
        em = request.form['ret']
        pw = request.form['rpt']
        pcw = request.form['rcpt']
        if pcw == pw:
            cursor.execute(f'insert into USPW1 values("{em}","{pw}")')
            con.commit()
            
            return jsonify({'data':True,'info':'registered'})
        else:
            return jsonify({'data':False,'info':'passwords not matching'})
    except:
         return jsonify({'data':False,'info':'error or Username is taken'})

@app.route('/home')
def ho():
    return render_template('home.html',name = session['user'])

app.run(debug=True)
