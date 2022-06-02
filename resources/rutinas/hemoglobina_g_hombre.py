from flask import Response, request
from flask_restful import Resource
from database.model import HemoglobinaGHombre

class HemoglobinaGHombreApi(Resource):

    def get(self, id):
        try:
            hemoglobina_g_hombre = HemoglobinaGHombre.objects.get(id=id).to_json()
            return Response(hemoglobina_g_hombre, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            hemoglobina_g_hombre = HemoglobinaGHombre.objects.get(id=id)
            hemoglobina_g_hombre.min = request.json['min']
            hemoglobina_g_hombre.max = request.json['max']
            hemoglobina_g_hombre.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            hemoglobina_g_hombre = HemoglobinaGHombre.objects.get(id=id)
            hemoglobina_g_hombre.delete()
            # HemoglobinaGHombre.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class HemoglobinasGHombreApi(Resource):

    def get(self):
        try:
        # traer todo hemoglobina_g_hombre
            hemoglobina_g_hombre = HemoglobinaGHombre.objects().to_json()
            return Response(hemoglobina_g_hombre, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            hemoglobina_g_hombre = HemoglobinaGHombre(**body).save()
            id = hemoglobina_g_hombre.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500