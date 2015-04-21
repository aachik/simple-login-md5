from flask import Flask, render_template, redirect, request, url_for, flash, make_response
from flask.ext.restful import Api, Resource
import hashlib
app = Flask(__name__)


app.secret_key = 'nydf0^3bxnlrt_rx03l$!#14q8dbr=q%))2a-2t@07_0n%%*m$'

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		m = hashlib.md5()
		m.update(request.form['password'].encode('utf-8'))
		m = m.hexdigest()
		print(request.form['email'])
		print(m)
		if request.form['password'] == 'aa121292':
			data={'m': m, 'password': request.form['password']}
			return render_template('success.html', data=data)
		else:
			data={'m': m, 'password': request.form['password']}
			flash('password encriptado:{}, password sin encriptar:{}'.format(m, request.form['password']))
	return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)