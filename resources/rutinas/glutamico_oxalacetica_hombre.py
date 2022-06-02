from flask import Response, request
from flask_restful import Resource
from database.model import GlutamicoOxalaceticaHombre

class GlutamicoOxalaceticaHombreApi(Resource):

    def get(self, id):
        try:
            glutamico_oxalacetica_hombre = GlutamicoOxalaceticaHombre.objects.get(id=id).to_json()
            return Response(glutamico_oxalacetica_hombre, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            glutamico_oxalacetica_hombre = GlutamicoOxalaceticaHombre.objects.get(id=id)
            glutamico_oxalacetica_hombre.min = request.json['min']
            glutamico_oxalacetica_hombre.max = request.json['max']
            glutamico_oxalacetica_hombre.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            glutamico_oxalacetica_hombre = GlutamicoOxalaceticaHombre.objects.get(id=id)
            glutamico_oxalacetica_hombre.delete()
            # GlutamicoOxalaceticaHombre.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class GlutamicosOxalaceticaHombreApi(Resource):

    def get(self):
        try:
        # traer todo la glutamico oxalacetica hombre
            glutamico_oxalacetica_hombre = GlutamicoOxalaceticaHombre.objects().to_json()
            return Response(glutamico_oxalacetica_hombre, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            glutamico_oxalacetica_hombre = GlutamicoOxalaceticaHombre(**body).save()
            id = glutamico_oxalacetica_hombre.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500