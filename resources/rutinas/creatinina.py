from flask import Response, request
from flask_restful import Resource
from database.model import Creatinina

class CreatininaApi(Resource):

    def get(self, id):
        try:
            creatinina = Creatinina.objects.get(id=id).to_json()
            return Response(creatinina, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            creatinina = Creatinina.objects.get(id=id)
            creatinina.min = request.json['min']
            creatinina.max = request.json['max']
            creatinina.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            creatinina = Creatinina.objects.get(id=id)
            creatinina.delete()
            # Creatinina.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class CreatininasApi(Resource):

    def get(self):
        try:
        # traer todo creatinina
            creatinina = Creatinina.objects().to_json()
            return Response(creatinina, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            creatinina = Creatinina(**body).save()
            id = creatinina.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500