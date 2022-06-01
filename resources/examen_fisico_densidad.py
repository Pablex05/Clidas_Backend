from flask import Response, request
from flask_restful import Resource
from database.model import ExamenFisicoDensidad

class ExamenFisicoDensidadApi(Resource):

    def get(self, id):
        examen_fisico_densidad = ExamenFisicoDensidad.objects.get(id=id).to_json()
        return Response(examen_fisico_densidad, mimetype="application/json", status=200)

    def put(self, id):  
        try:
            examen_fisico_densidad = ExamenFisicoDensidad.objects.get(id=id)
            examen_fisico_densidad.min = request.json['min']
            examen_fisico_densidad.max = request.json['max']
            examen_fisico_densidad.save()
            return 'update OK!', 200
        except:
            return 'update error!', 500

    def delete(self, id):
        ExamenFisicoDensidad.objects.get(id=id).delete()
        return 'delete OK!', 200

class ExamenesFisicosDensidadApi(Resource):

    def get(self):
        # traer todo el examen fisico densidad
        examen_fisico_densidad = ExamenFisicoDensidad.objects().to_json()
        return Response(examen_fisico_densidad, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        examen_fisico_densidad = ExamenFisicoDensidad(**body).save()
        id = examen_fisico_densidad.id
        return {'id': str(id)}, 200
    
    
