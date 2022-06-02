from flask import Response, request
from flask_restful import Resource
from database.model import ExamenFisicoReaccion

class ExamenFisicoReaccionApi(Resource):

    def get(self, id):
        try:
            examen_fisico_reaccion = ExamenFisicoReaccion.objects.get(id=id).to_json()
            return Response(examen_fisico_reaccion, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def put(self, id):  
        try:
            examen_fisico_reaccion = ExamenFisicoReaccion.objects.get(id=id)
            examen_fisico_reaccion.min = request.json['min']
            examen_fisico_reaccion.max = request.json['max']
            examen_fisico_reaccion.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        try:
            examen_fisico_reaccion = ExamenFisicoReaccion.objects.get(id=id)
            examen_fisico_reaccion.delete()
            # ExamenFisicoReaccion.objects.get(id=id).delete()
            return 'delete OK!', 200
        except:
            return 'delete error!', 500

class ExamenesFisicosReaccionApi(Resource):

    def get(self):
        try:
        # traer todo el examen fisico Reaccion
            examen_fisico_reaccion = ExamenFisicoReaccion.objects().to_json()
            return Response(examen_fisico_reaccion, mimetype="application/json", status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            examen_fisico_reaccion = ExamenFisicoReaccion(**body).save()
            id = examen_fisico_reaccion.id
            return {'id': str(id)}, 200
        except:
            return 'post error!', 500