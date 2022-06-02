from flask import Response, request
from flask_restful import Resource
from database.model import HdlHombre

class HdlHombreApi(Resource):

    def get(self, id):
        try:
            hdl_hombre = HdlHombre.objects.get(id=id).to_json()
            return Response(hdl_hombre, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            hdl_hombre = HdlHombre.objects.get(id=id)
            hdl_hombre.min = request.json['min']
            hdl_hombre.max = request.json['max']
            hdl_hombre.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            hdl_hombre = HdlHombre.objects.get(id=id)
            hdl_hombre.delete()
            # HdlHombre.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class HdlHombre(Resource):

    def get(self):
        try:
        # traer todo hdl_hombre
            hdl_hombre = HdlHombre.objects().to_json()
            return Response(hdl_hombre, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            hdl_hombre = HdlHombre(**body).save()
            id = hdl_hombre.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500