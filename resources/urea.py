from flask import Response, request
from flask_restful import Resource
from database.model import Urea

class UreaApi(Resource):

    def get(self, id):
        try:
            urea = Urea.objects.get(id=id).to_json()
            return Response(urea, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            urea = Urea.objects.get(id=id)
            urea.min = request.json['min']
            urea.max = request.json['max']
            urea.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            urea = Urea.objects.get(id=id)
            urea.delete()
            # Urea.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class UreasApi(Resource):

    def get(self):
        try:
        # traer todo urea
            urea = Urea.objects().to_json()
            return Response(urea, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            urea = Urea(**body).save()
            id = urea.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500