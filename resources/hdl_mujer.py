from flask import Response, request
from flask_restful import Resource
from database.model import HdlMujer

class HdlMujerApi(Resource):

    def get(self, id):
        try:
            hdl_mujer = HdlMujer.objects.get(id=id).to_json()
            return Response(hdl_mujer, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            hdl_mujer = HdlMujer.objects.get(id=id)
            hdl_mujer.min = request.json['min']
            hdl_mujer.max = request.json['max']
            hdl_mujer.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            hdl_mujer = HdlMujer.objects.get(id=id)
            hdl_mujer.delete()
            # HdlMujer.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class HdlMujer(Resource):

    def get(self):
        try:
        # traer todo hdl_mujer
            hdl_mujer = HdlMujer.objects().to_json()
            return Response(hdl_mujer, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            hdl_mujer = HdlMujer(**body).save()
            id = hdl_mujer.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500