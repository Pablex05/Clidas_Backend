from flask import Response, request
from flask_restful import Resource
from database.model import ExamenMicroscopicoHematies

class ExamenMicroscopicoHematiesApi(Resource):

    def get(self, id):
        try:
            examen_microscopico_hematies = ExamenMicroscopicoHematies.objects.get(id=id).to_json()
            return Response(examen_microscopico_hematies, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            examen_microscopico_hematies = ExamenMicroscopicoHematies.objects.get(id=id)
            examen_microscopico_hematies.min = request.json['min']
            examen_microscopico_hematies.max = request.json['max']
            examen_microscopico_hematies.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            examen_microscopico_hematies = ExamenMicroscopicoHematies.objects.get(id=id)
            examen_microscopico_hematies.delete()
            # ExamenMicroscopicoHematies.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class ExamenesMicroscopicosHematiesApi(Resource):

    def get(self):
        try:
        # traer todo el examen microscopico Hematies
            examen_microscopico_hematies = ExamenMicroscopicoHematies.objects().to_json()
            return Response(examen_microscopico_hematies, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            examen_microscopico_hematies = ExamenMicroscopicoHematies(**body).save()
            id = examen_microscopico_hematies.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500