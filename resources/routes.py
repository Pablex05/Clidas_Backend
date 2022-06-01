from .examen_fisico_densidad import ExamenFisicoDensidadApi, ExamenesFisicosDensidadApi

def initialize_routes(api):
    api.add_resource(ExamenFisicoDensidadApi, '/Clidas/api/examen-fisico-densidad/<id>')
    api.add_resource(ExamenesFisicosDensidadApi, '/Clidas/api/examenes-fisico-densidad')