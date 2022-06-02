from flask import Response, request
from flask_restful import Resource
from database.model import Monocitos

class MonocitosApi(Resource):

    def get(self, id):
        try:
            monocitos = Monocitos.objects.get(id=id).to_json()
            return Response(monocitos, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            monocitos = Monocitos.objects.get(id=id)
            monocitos.min = request.json['min']
            monocitos.max = request.json['max']
            monocitos.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            monocitos = Monocitos.objects.get(id=id)
            monocitos.delete()
            # Monocitos.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class MonocitoApi(Resource):

    def get(self):
        try:
        # traer todo monocitos
            monocitos = Monocitos.objects().to_json()
            return Response(monocitos, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            monocitos = Monocitos(**body).save()
            id = monocitos.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500