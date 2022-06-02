from flask import Response, request
from flask_restful import Resource
from database.model import HematocritosHombre

class HematocritosHombreApi(Resource):

    def get(self, id):
        try:
            hematocritos_hombre = HematocritosHombre.objects.get(id=id).to_json()
            return Response(hematocritos_hombre, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            hematocritos_hombre = HematocritosHombre.objects.get(id=id)
            hematocritos_hombre.min = request.json['min']
            hematocritos_hombre.max = request.json['max']
            hematocritos_hombre.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            hematocritos_hombre = HematocritosHombre.objects.get(id=id)
            hematocritos_hombre.delete()
            # HematocritosHombre.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class HematocritosHombre(Resource):

    def get(self):
        try:
        # traer todo hematocritos_hombre
            hematocritos_hombre = HematocritosHombre.objects().to_json()
            return Response(hematocritos_hombre, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            hematocritos_hombre = HematocritosHombre(**body).save()
            id = hematocritos_hombre.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500