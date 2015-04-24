from flask import Flask, render_template, redirect, request, url_for, flash, make_response
from flask.ext.restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import hashlib
app = Flask(__name__)
app.secret_key = 'nydf0^3bxnlrt_rx03l$!#14q8dbr=q%))2a-2t@07_0n%%*m$'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:aa121292@localhost/db'

db = SQLAlchemy(app)
api = Api(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password

    def __repr__(self):
        return '<Usuario %r>' % self.usuario


@app.route('/', methods=['GET', 'POST'])
def index():

	if request.method == 'POST':
		m = hashlib.md5()
		m.update(request.form['password'].encode('utf-8'))
		m = m.hexdigest()
		print('login:')
		print(request.form['email'])
		print(m)
		usuario = Usuario.query.filter_by(usuario=request.form['email']).first()
		print(usuario)

		if m == usuario.password:
			print('el pass es correcto')
			data={'m': m, 'password': request.form['password']}
			return render_template('success.html', data=data)
		else:
			data={'m': m, 'password': request.form['password']}
			flash('password encriptado:{}, password sin encriptar:{}'.format(m, request.form['password']))
	return render_template('index.html')

@app.route('/sign_up', methods=['GET','POST'])
def sign_up():
	if request.method == 'POST':
		m = hashlib.md5()
		m.update(request.form['password'].encode('utf-8'))
		m = m.hexdigest()
		print('sign up: ')
		print(request.form['email'])
		print(m)
		usuario = Usuario(request.form['email'], m)
		db.session.add(usuario)
		db.session.commit()
		data={'m': m, 'password': request.form['password']}
		return render_template('success.html', data=data)
	return render_template('sign_up.html')

@app.route('/log')
def log():

	pass

if __name__ == '__main__':
    app.run(debug=True)