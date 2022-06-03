from flask import Response, request
from flask_restful import Resource
from database.model import Basofilos

class BasofiloApi(Resource):

    def get(self, id):
        try:
            basofilos = Basofilos.objects.get(id=id).to_json()
            return Response(basofilos, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            basofilos = Basofilos.objects.get(id=id)
            basofilos.min = request.json['min']
            basofilos.max = request.json['max']
            basofilos.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            basofilos = Basofilos.objects.get(id=id)
            basofilos.delete()
            # Basofilos.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class BasofilosApi(Resource):

    def get(self):
        try:
        # traer todo basofilos
            basofilos = Basofilos.objects().to_json()
            return Response(basofilos, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            basofilos = Basofilos(**body).save()
            id = basofilos.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500
    
    