from flask import Response, request
from flask_restful import Resource
from database.model import Plaquetas

class PlaquetaApi(Resource):

    def get(self, id):
        try:
            plaquetas = Plaquetas.objects.get(id=id).to_json()
            return Response(plaquetas, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            plaquetas = Plaquetas.objects.get(id=id)
            plaquetas.min = request.json['min']
            plaquetas.max = request.json['max']
            plaquetas.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            plaquetas = Plaquetas.objects.get(id=id)
            plaquetas.delete()
            # Plaquetas.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class PlaquetasApi(Resource):

    def get(self):
        try:
        # traer todo plaquetas
            plaquetas = Plaquetas.objects().to_json()
            return Response(plaquetas, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            plaquetas = Plaquetas(**body).save()
            id = plaquetas.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500