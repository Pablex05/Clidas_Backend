from flask import Response, request
from flask_restful import Resource
from database.model import NeutrofilosSegmentado

class NeutrofiloSegmentadoApi(Resource):

    def get(self, id):
        try:
            neutrofilos_segmentado = NeutrofilosSegmentado.objects.get(id=id).to_json()
            return Response(neutrofilos_segmentado, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            neutrofilos_segmentado = NeutrofilosSegmentado.objects.get(id=id)
            neutrofilos_segmentado.min = request.json['min']
            neutrofilos_segmentado.max = request.json['max']
            neutrofilos_segmentado.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            neutrofilos_segmentado = NeutrofilosSegmentado.objects.get(id=id)
            neutrofilos_segmentado.delete()
            # NeutrofilosSegmentado.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class NeutrofilosSegmentadoApi(Resource):

    def get(self):
        try:
        # traer todo neutrofilos_segmentado
            neutrofilos_segmentado = NeutrofilosSegmentado.objects().to_json()
            return Response(neutrofilos_segmentado, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            neutrofilos_segmentado = NeutrofilosSegmentado(**body).save()
            id = neutrofilos_segmentado.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500