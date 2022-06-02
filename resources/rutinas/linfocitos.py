from flask import Response, request
from flask_restful import Resource
from database.model import Linfocitos

class LinfocitoApi(Resource):

    def get(self, id):
        try:
            linfocitos = Linfocitos.objects.get(id=id).to_json()
            return Response(linfocitos, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            linfocitos = Linfocitos.objects.get(id=id)
            linfocitos.min = request.json['min']
            linfocitos.max = request.json['max']
            linfocitos.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            linfocitos = Linfocitos.objects.get(id=id)
            linfocitos.delete()
            # Linfocitos.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class LinfocitosApi(Resource):

    def get(self):
        try:
        # traer todo linfocitos
            linfocitos = Linfocitos.objects().to_json()
            return Response(linfocitos, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            linfocitos = Linfocitos(**body).save()
            id = linfocitos.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500