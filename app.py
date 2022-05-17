from flask import Flask, jsonify,render_template,request,redirect

app = Flask(__name__)

Users = [['h1@gmail.com','h1'],['h2@gmail.com','h2']]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def reg():
    return render_template('register.html')

@app.route('/log',methods = ['POST'])
def log():
    em = request.form['et']
    pw = request.form['pt']
    if [em,pw] in Users:
        return jsonify({'login': True})
    else:
        return jsonify({'login': False})

@app.route('/home')
def ho():
    return render_template('home.html')

app.run(debug=True)