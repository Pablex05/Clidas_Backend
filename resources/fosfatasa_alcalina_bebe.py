from flask import Response, request
from flask_restful import Resource
from database.model import FosfatasaAlcalinaBebe

class FosfatasaAlcalinaBebeApi(Resource):

    def get(self, id):
        try:
            fosfatasa_alcalina_bebe = FosfatasaAlcalinaBebe.objects.get(id=id).to_json()
            return Response(fosfatasa_alcalina_bebe, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            fosfatasa_alcalina_bebe = FosfatasaAlcalinaBebe.objects.get(id=id)
            fosfatasa_alcalina_bebe.min = request.json['min']
            fosfatasa_alcalina_bebe.max = request.json['max']
            fosfatasa_alcalina_bebe.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            fosfatasa_alcalina_bebe = FosfatasaAlcalinaBebe.objects.get(id=id)
            fosfatasa_alcalina_bebe.delete()
            # FosfatasaAlcalinaBebe.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class FosfatasaAlcalinaBebeApi(Resource):

    def get(self):
        try:
        # traer todo la fosfatasa alcalina bebe
            fosfatasa_alcalina_bebe = FosfatasaAlcalinaBebe.objects().to_json()
            return Response(fosfatasa_alcalina_bebe, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            fosfatasa_alcalina_bebe = FosfatasaAlcalinaBebe(**body).save()
            id = fosfatasa_alcalina_bebe.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500