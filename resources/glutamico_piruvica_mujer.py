from flask import Response, request
from flask_restful import Resource
from database.model import GlutamicoPiruvicaMujer

class GlutamicoPiruvicaMujerApi(Resource):

    def get(self, id):
        try:
            glutamico_piruvica_mujer = GlutamicoPiruvicaMujer.objects.get(id=id).to_json()
            return Response(glutamico_piruvica_mujer, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            glutamico_piruvica_mujer = GlutamicoPiruvicaMujer.objects.get(id=id)
            glutamico_piruvica_mujer.min = request.json['min']
            glutamico_piruvica_mujer.max = request.json['max']
            glutamico_piruvica_mujer.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            glutamico_piruvica_mujer = GlutamicoPiruvicaMujer.objects.get(id=id)
            glutamico_piruvica_mujer.delete()
            # GlutamicoPiruvicaMujer.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class GlutamicoPiruvicaMujerApi(Resource):

    def get(self):
        try:
        # traer todo la glutamico piruvica mujer
            glutamico_piruvica_mujer = GlutamicoPiruvicaMujer.objects().to_json()
            return Response(glutamico_piruvica_mujer, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            glutamico_piruvica_mujer = GlutamicoPiruvicaMujer(**body).save()
            id = glutamico_piruvica_mujer.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500