from flask import Response, request
from flask_restful import Resource
from database.model import GlutamicoPiruvicaHombre

class GlutamicoPiruvicaHombreApi(Resource):

    def get(self, id):
        try:
            glutamico_piruvica_hombre = GlutamicoPiruvicaHombre.objects.get(id=id).to_json()
            return Response(glutamico_piruvica_hombre, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            glutamico_piruvica_hombre = GlutamicoPiruvicaHombre.objects.get(id=id)
            glutamico_piruvica_hombre.min = request.json['min']
            glutamico_piruvica_hombre.max = request.json['max']
            glutamico_piruvica_hombre.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            glutamico_piruvica_hombre = GlutamicoPiruvicaHombre.objects.get(id=id)
            glutamico_piruvica_hombre.delete()
            # GlutamicoPiruvicaHombre.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class GlutamicosPiruvicaHombreApi(Resource):

    def get(self):
        try:
        # traer todo la glutamico piruvica hombre
            glutamico_piruvica_hombre = GlutamicoPiruvicaHombre.objects().to_json()
            return Response(glutamico_piruvica_hombre, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            glutamico_piruvica_hombre = GlutamicoPiruvicaHombre(**body).save()
            id = glutamico_piruvica_hombre.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500