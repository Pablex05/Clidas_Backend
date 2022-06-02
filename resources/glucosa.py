from flask import Response, request
from flask_restful import Resource
from database.model import Glucosa

class GlucosaApi(Resource):

    def get(self, id):
        try:
            glucosa = Glucosa.objects.get(id=id).to_json()
            return Response(glucosa, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            glucosa = Glucosa.objects.get(id=id)
            glucosa.min = request.json['min']
            glucosa.max = request.json['max']
            glucosa.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            glucosa = Glucosa.objects.get(id=id)
            glucosa.delete()
            # Glucosa.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class Glucosa(Resource):

    def get(self):
        try:
        # traer todo glucosa
            glucosa = Glucosa.objects().to_json()
            return Response(glucosa, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            glucosa = Glucosa(**body).save()
            id = glucosa.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500