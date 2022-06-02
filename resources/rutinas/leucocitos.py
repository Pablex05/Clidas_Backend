from flask import Response, request
from flask_restful import Resource
from database.model import Leucocitos

class LeucocitoApi(Resource):

    def get(self, id):
        try:
            leucocitos = Leucocitos.objects.get(id=id).to_json()
            return Response(leucocitos, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            leucocitos = Leucocitos.objects.get(id=id)
            leucocitos.min = request.json['min']
            leucocitos.max = request.json['max']
            leucocitos.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            leucocitos = Leucocitos.objects.get(id=id)
            leucocitos.delete()
            # Leucocitos.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class LeucocitosApi(Resource):

    def get(self):
        try:
        # traer todo leucocitos
            leucocitos = Leucocitos.objects().to_json()
            return Response(leucocitos, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            leucocitos = Leucocitos(**body).save()
            id = leucocitos.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500