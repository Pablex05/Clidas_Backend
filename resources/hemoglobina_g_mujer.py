from flask import Response, request
from flask_restful import Resource
from database.model import HemoglobinaGMujer

class HemoglobinaGMujerApi(Resource):

    def get(self, id):
        try:
            hemoglobina_g_mujer = HemoglobinaGMujer.objects.get(id=id).to_json()
            return Response(hemoglobina_g_mujer, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            hemoglobina_g_mujer = HemoglobinaGMujer.objects.get(id=id)
            hemoglobina_g_mujer.min = request.json['min']
            hemoglobina_g_mujer.max = request.json['max']
            hemoglobina_g_mujer.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            hemoglobina_g_mujer = HemoglobinaGMujer.objects.get(id=id)
            hemoglobina_g_mujer.delete()
            # HemoglobinaGMujer.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class HemoglobinaGMujer(Resource):

    def get(self):
        try:
        # traer todo hemoglobina_g_mujer
            hemoglobina_g_mujer = HemoglobinaGMujer.objects().to_json()
            return Response(hemoglobina_g_mujer, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            hemoglobina_g_mujer = HemoglobinaGMujer(**body).save()
            id = hemoglobina_g_mujer.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500