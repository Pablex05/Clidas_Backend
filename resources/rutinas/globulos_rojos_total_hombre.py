from flask import Response, request
from flask_restful import Resource
from database.model import GlobulosRojosTotalHombre

class GlobuloRojosTotalHombreApi(Resource):

    def get(self, id):
        try:
            globulos_rojos_total_hombre = GlobulosRojosTotalHombre.objects.get(id=id).to_json()
            return Response(globulos_rojos_total_hombre, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            globulos_rojos_total_hombre = GlobulosRojosTotalHombre.objects.get(id=id)
            globulos_rojos_total_hombre.min = request.json['min']
            globulos_rojos_total_hombre.max = request.json['max']
            globulos_rojos_total_hombre.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            globulos_rojos_total_hombre = GlobulosRojosTotalHombre.objects.get(id=id)
            globulos_rojos_total_hombre.delete()
            # GlobulosRojosTotalHombre.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class GlobulosRojosTotalHombreApi(Resource):

    def get(self):
        try:
        # traer todo globulos_rojos_total_hombre
            globulos_rojos_total_hombre = GlobulosRojosTotalHombre.objects().to_json()
            return Response(globulos_rojos_total_hombre, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            globulos_rojos_total_hombre = GlobulosRojosTotalHombre(**body).save()
            id = globulos_rojos_total_hombre.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500