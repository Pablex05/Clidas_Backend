from flask import Response, request
from flask_restful import Resource
from database.model import ExamenMicroscopicoLeucocitos

class ExamenMicroscopicoLeucocitosApi(Resource):

    def get(self, id):
        try:
            examen_microscopico_leucocitos = ExamenMicroscopicoLeucocitos.objects.get(id=id).to_json()
            return Response(examen_microscopico_leucocitos, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            examen_microscopico_leucocitos = ExamenMicroscopicoLeucocitos.objects.get(id=id)
            examen_microscopico_leucocitos.min = request.json['min']
            examen_microscopico_leucocitos.max = request.json['max']
            examen_microscopico_leucocitos.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            examen_microscopico_leucocitos = ExamenMicroscopicoLeucocitos.objects.get(id=id)
            examen_microscopico_leucocitos.delete()
            # ExamenMicroscopicoLeucocitos.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class ExamenesMicroscopicosLeucocitosApi(Resource):

    def get(self):
        try:
        # traer todo el examen microscopico Leucocitos
            examen_microscopico_leucocitos = ExamenMicroscopicoLeucocitos.objects().to_json()
            return Response(examen_microscopico_leucocitos, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            examen_microscopico_leucocitos = ExamenMicroscopicoLeucocitos(**body).save()
            id = examen_microscopico_leucocitos.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500