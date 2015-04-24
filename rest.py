from flask.ext.restful import Api, Resource
from cpa_abs import db, Usuario
class Usuario(Resource):
	def get(self):
		usuario = Usuario.query.all()