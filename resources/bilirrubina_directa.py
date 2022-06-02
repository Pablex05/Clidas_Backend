from flask import Response, request
from flask_restful import Resource
from database.model import BilirrubinaDirecta

class BilirrubinaDirectaApi(Resource):

    def get(self, id):
        try:
            bilirrubina_directa = BilirrubinaDirecta.objects.get(id=id).to_json()
            return Response(bilirrubina_directa, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            bilirrubina_directa = BilirrubinaDirecta.objects.get(id=id)
            bilirrubina_directa.min = request.json['min']
            bilirrubina_directa.max = request.json['max']
            bilirrubina_directa.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            bilirrubina_directa = BilirrubinaDirecta.objects.get(id=id)
            bilirrubina_directa.delete()
            # BilirrubinaDirecta.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class BilirrubinasDirectaApi(Resource):

    def get(self):
        try:
        # traer todo la bilirrubina indirecta
            bilirrubina_directa = BilirrubinaDirecta.objects().to_json()
            return Response(bilirrubina_directa, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            bilirrubina_directa = BilirrubinaDirecta(**body).save()
            id = bilirrubina_directa.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500