from flask import Response, request
from flask_restful import Resource
from database.model import FosfatasaAlcalinaAdulto

class FosfatasaAlcalinaAdultoApi(Resource):

    def get(self, id):
        try:
            fosfatasa_alcalina_adulto = FosfatasaAlcalinaAdulto.objects.get(id=id).to_json()
            return Response(fosfatasa_alcalina_adulto, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            fosfatasa_alcalina_adulto = FosfatasaAlcalinaAdulto.objects.get(id=id)
            fosfatasa_alcalina_adulto.min = request.json['min']
            fosfatasa_alcalina_adulto.max = request.json['max']
            fosfatasa_alcalina_adulto.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            fosfatasa_alcalina_adulto = FosfatasaAlcalinaAdulto.objects.get(id=id)
            fosfatasa_alcalina_adulto.delete()
            # FosfatasaAlcalinaAdulto.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class FosfatasasAlcalinaAdultoApi(Resource):

    def get(self):
        try:
        # traer todo la fosfatasa alcalina adulto
            fosfatasa_alcalina_adulto = FosfatasaAlcalinaAdulto.objects().to_json()
            return Response(fosfatasa_alcalina_adulto, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            fosfatasa_alcalina_adulto = FosfatasaAlcalinaAdulto(**body).save()
            id = fosfatasa_alcalina_adulto.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500