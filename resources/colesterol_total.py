from flask import Response, request
from flask_restful import Resource
from database.model import ColesterolTotal

class ColesterolTotalApi(Resource):

    def get(self, id):
        try:
            colesterol_total = ColesterolTotal.objects.get(id=id).to_json()
            return Response(colesterol_total, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            colesterol_total = ColesterolTotal.objects.get(id=id)
            colesterol_total.min = request.json['min']
            colesterol_total.max = request.json['max']
            colesterol_total.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            colesterol_total = ColesterolTotal.objects.get(id=id)
            colesterol_total.delete()
            # ColesterolTotal.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class ColesterolTotalApi(Resource):

    def get(self):
        try:
        # traer todo la colesterol total
            colesterol_total = ColesterolTotal.objects().to_json()
            return Response(colesterol_total, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            colesterol_total = ColesterolTotal(**body).save()
            id = colesterol_total.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500