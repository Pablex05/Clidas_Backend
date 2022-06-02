from flask import Response, request
from flask_restful import Resource
from database.model import HematocritosMujer

class HematocritosMujerApi(Resource):

    def get(self, id):
        try:
            hematocritos_mujer = HematocritosMujer.objects.get(id=id).to_json()
            return Response(hematocritos_mujer, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            hematocritos_mujer = HematocritosMujer.objects.get(id=id)
            hematocritos_mujer.min = request.json['min']
            hematocritos_mujer.max = request.json['max']
            hematocritos_mujer.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            hematocritos_mujer = HematocritosMujer.objects.get(id=id)
            hematocritos_mujer.delete()
            # HematocritosMujer.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class HematocritosMujer(Resource):

    def get(self):
        try:
        # traer todo hematocritos_mujer
            hematocritos_mujer = HematocritosMujer.objects().to_json()
            return Response(hematocritos_mujer, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            hematocritos_mujer = HematocritosMujer(**body).save()
            id = hematocritos_mujer.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500