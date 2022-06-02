from flask import Response, request
from flask_restful import Resource
from database.model import Ldl

class LdlApi(Resource):

    def get(self, id):
        try:
            ldl = Ldl.objects.get(id=id).to_json()
            return Response(ldl, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            ldl = Ldl.objects.get(id=id)
            ldl.min = request.json['min']
            ldl.max = request.json['max']
            ldl.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            ldl = Ldl.objects.get(id=id)
            ldl.delete()
            # Ldl.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class Ldl(Resource):

    def get(self):
        try:
        # traer todo ldl
            ldl = Ldl.objects().to_json()
            return Response(ldl, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            ldl = Ldl(**body).save()
            id = ldl.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500