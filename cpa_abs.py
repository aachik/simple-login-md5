from flask import Flask, render_template, redirect, request, url_for, flash, make_response
from flask.ext.restful import Api, Resource
import hashlib
app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		m = hashlib.md5()
		m.update(request.form['password'].encode('utf-8'))
		m = m.hexdigest()
		print(request.form['email'])
		print(m)

		data={'m': m, 'password': request.form['password']}
		return render_template('success.html', data=data)
	return render_template('index.html')


@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)