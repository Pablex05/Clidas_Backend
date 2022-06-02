from flask import Response, request
from flask_restful import Resource
from database.model import BilirrubinaTotal

class BilirrubinaTotalApi(Resource):

    def get(self, id):
        try:
            bilirrubina_total = BilirrubinaTotal.objects.get(id=id).to_json()
            return Response(bilirrubina_total, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            bilirrubina_total = BilirrubinaTotal.objects.get(id=id)
            bilirrubina_total.min = request.json['min']
            bilirrubina_total.max = request.json['max']
            bilirrubina_total.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            bilirrubina_total = BilirrubinaTotal.objects.get(id=id)
            bilirrubina_total.delete()
            # BilirrubinaTotal.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class BilirrubinasTotalApi(Resource):

    def get(self):
        try:
        # traer todo la bilirrubina total
            bilirrubina_total = BilirrubinaTotal.objects().to_json()
            return Response(bilirrubina_total, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            bilirrubina_total = BilirrubinaTotal(**body).save()
            id = bilirrubina_total.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500