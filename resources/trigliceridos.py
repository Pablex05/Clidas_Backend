from flask import Response, request
from flask_restful import Resource
from database.model import Trigliceridos

class TrigliceridoApi(Resource):

    def get(self, id):
        try:
            trigliceridos = Trigliceridos.objects.get(id=id).to_json()
            return Response(trigliceridos, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            trigliceridos = Trigliceridos.objects.get(id=id)
            trigliceridos.min = request.json['min']
            trigliceridos.max = request.json['max']
            trigliceridos.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            trigliceridos = Trigliceridos.objects.get(id=id)
            trigliceridos.delete()
            # Trigliceridos.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class TrigliceridosApi(Resource):

    def get(self):
        try:
        # traer todo trigliceridos
            trigliceridos = Trigliceridos.objects().to_json()
            return Response(trigliceridos, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            trigliceridos = Trigliceridos(**body).save()
            id = trigliceridos.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500