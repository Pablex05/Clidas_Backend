from flask import Response, request
from flask_restful import Resource
from database.model import GlobulosRojosTotalMujer

class GlobulosRojosTotalMujerApi(Resource):

    def get(self, id):
        try:
            globulos_rojos_total_mujer = GlobulosRojosTotalMujer.objects.get(id=id).to_json()
            return Response(globulos_rojos_total_mujer, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            globulos_rojos_total_mujer = GlobulosRojosTotalMujer.objects.get(id=id)
            globulos_rojos_total_mujer.min = request.json['min']
            globulos_rojos_total_mujer.max = request.json['max']
            globulos_rojos_total_mujer.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            globulos_rojos_total_mujer = GlobulosRojosTotalMujer.objects.get(id=id)
            globulos_rojos_total_mujer.delete()
            # GlobulosRojosTotalMujer.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class GlobulosRojosTotalMujer(Resource):

    def get(self):
        try:
        # traer todo globulos_rojos_total_mujer
            globulos_rojos_total_mujer = GlobulosRojosTotalMujer.objects().to_json()
            return Response(globulos_rojos_total_mujer, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            globulos_rojos_total_mujer = GlobulosRojosTotalMujer(**body).save()
            id = globulos_rojos_total_mujer.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500