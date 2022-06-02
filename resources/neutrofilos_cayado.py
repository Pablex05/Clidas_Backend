from flask import Response, request
from flask_restful import Resource
from database.model import NeutrofilosCayado

class NeutrofiloCayadoApi(Resource):

    def get(self, id):
        try:
            neutrofilos_cayado = NeutrofilosCayado.objects.get(id=id).to_json()
            return Response(neutrofilos_cayado, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            neutrofilos_cayado = NeutrofilosCayado.objects.get(id=id)
            neutrofilos_cayado.min = request.json['min']
            neutrofilos_cayado.max = request.json['max']
            neutrofilos_cayado.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            neutrofilos_cayado = NeutrofilosCayado.objects.get(id=id)
            neutrofilos_cayado.delete()
            # NeutrofilosCayado.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class NeutrofilosCayadoApi(Resource):

    def get(self):
        try:
        # traer todo neutrofilos_cayado
            neutrofilos_cayado = NeutrofilosCayado.objects().to_json()
            return Response(neutrofilos_cayado, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            neutrofilos_cayado = NeutrofilosCayado(**body).save()
            id = neutrofilos_cayado.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500