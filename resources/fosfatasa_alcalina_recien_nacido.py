from flask import Response, request
from flask_restful import Resource
from database.model import FosfatasaAlcalinaRecienNacido

class FosfatasaAlcalinaRecienNacidoApi(Resource):

    def get(self, id):
        try:
            fosfatasa_alcalina_recien_nacido = FosfatasaAlcalinaRecienNacido.objects.get(id=id).to_json()
            return Response(fosfatasa_alcalina_recien_nacido, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            fosfatasa_alcalina_recien_nacido = FosfatasaAlcalinaRecienNacido.objects.get(id=id)
            fosfatasa_alcalina_recien_nacido.min = request.json['min']
            fosfatasa_alcalina_recien_nacido.max = request.json['max']
            fosfatasa_alcalina_recien_nacido.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            fosfatasa_alcalina_recien_nacido = FosfatasaAlcalinaRecienNacido.objects.get(id=id)
            fosfatasa_alcalina_recien_nacido.delete()
            # FosfatasaAlcalinaRecienNacido.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class FosfatasasAlcalinaRecienNacidoApi(Resource):

    def get(self):
        try:
        # traer todo la fosfatasa alcalina recien_nacido
            fosfatasa_alcalina_recien_nacido = FosfatasaAlcalinaRecienNacido.objects().to_json()
            return Response(fosfatasa_alcalina_recien_nacido, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            fosfatasa_alcalina_recien_nacido = FosfatasaAlcalinaRecienNacido(**body).save()
            id = fosfatasa_alcalina_recien_nacido.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500