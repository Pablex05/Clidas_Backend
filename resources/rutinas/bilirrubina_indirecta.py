from flask import Response, request
from flask_restful import Resource
from database.model import BilirrubinaIndirecta

class BilirrubinaIndirectaApi(Resource):

    def get(self, id):
        try:
            bilirrubina_indirecta = BilirrubinaIndirecta.objects.get(id=id).to_json()
            return Response(bilirrubina_indirecta, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            bilirrubina_indirecta = BilirrubinaIndirecta.objects.get(id=id)
            bilirrubina_indirecta.min = request.json['min']
            bilirrubina_indirecta.max = request.json['max']
            bilirrubina_indirecta.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            bilirrubina_indirecta = BilirrubinaIndirecta.objects.get(id=id)
            bilirrubina_indirecta.delete()
            # BilirrubinaIndirecta.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class BilirrubinasIndirectaApi(Resource):

    def get(self):
        try:
        # traer todo la bilirrubina indirecta
            bilirrubina_indirecta = BilirrubinaIndirecta.objects().to_json()
            return Response(bilirrubina_indirecta, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            bilirrubina_indirecta = BilirrubinaIndirecta(**body).save()
            id = bilirrubina_indirecta.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500