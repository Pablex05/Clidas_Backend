from flask import Response, request
from flask_restful import Resource
from database.model import GlutamicoOxalaceticaMujer

class GlutamicoOxalaceticaMujerApi(Resource):

    def get(self, id):
        try:
            glutamico_oxalacetica_mujer = GlutamicoOxalaceticaMujer.objects.get(id=id).to_json()
            return Response(glutamico_oxalacetica_mujer, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            glutamico_oxalacetica_mujer = GlutamicoOxalaceticaMujer.objects.get(id=id)
            glutamico_oxalacetica_mujer.min = request.json['min']
            glutamico_oxalacetica_mujer.max = request.json['max']
            glutamico_oxalacetica_mujer.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            glutamico_oxalacetica_mujer = GlutamicoOxalaceticaMujer.objects.get(id=id)
            glutamico_oxalacetica_mujer.delete()
            # GlutamicoOxalaceticaMujer.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class GlutamicoOxalaceticaMujerApi(Resource):

    def get(self):
        try:
        # traer todo la glutamico oxalacetica mujer
            glutamico_oxalacetica_mujer = GlutamicoOxalaceticaMujer.objects().to_json()
            return Response(glutamico_oxalacetica_mujer, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            glutamico_oxalacetica_mujer = GlutamicoOxalaceticaMujer(**body).save()
            id = glutamico_oxalacetica_mujer.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500