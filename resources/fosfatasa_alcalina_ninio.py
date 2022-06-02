from flask import Response, request
from flask_restful import Resource
from database.model import FosfatasaAlcalinaNinio

class FosfatasaAlcalinaNinioApi(Resource):

    def get(self, id):
        try:
            fosfatasa_alcalina_ninio = FosfatasaAlcalinaNinio.objects.get(id=id).to_json()
            return Response(fosfatasa_alcalina_ninio, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            fosfatasa_alcalina_ninio = FosfatasaAlcalinaNinio.objects.get(id=id)
            fosfatasa_alcalina_ninio.min = request.json['min']
            fosfatasa_alcalina_ninio.max = request.json['max']
            fosfatasa_alcalina_ninio.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            fosfatasa_alcalina_ninio = FosfatasaAlcalinaNinio.objects.get(id=id)
            fosfatasa_alcalina_ninio.delete()
            # FosfatasaAlcalinaNinio.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class FosfatasaAlcalinaNinioApi(Resource):

    def get(self):
        try:
        # traer todo la fosfatasa alcalina ninio
            fosfatasa_alcalina_ninio = FosfatasaAlcalinaNinio.objects().to_json()
            return Response(fosfatasa_alcalina_ninio, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            fosfatasa_alcalina_ninio = FosfatasaAlcalinaNinio(**body).save()
            id = fosfatasa_alcalina_ninio.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500