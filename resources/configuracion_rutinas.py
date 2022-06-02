from flask import Response, request
from flask_restful import Resource
from database.model import *

class ConfiguracionesRutinasApi(Resource):
    def get(self, id):
        try:
            conf_rutinas = {
                'examen_fisico_densidad': ExamenFisicoDensidad.objects.get(id=id).to_json(),
                'examen_microscopico_epitelial': ExamenMicroscopicoEpitelial.objects.get(id=id).to_json(),
                'examen_microscopico_leucocitos': ExamenMicroscopicoLeucocitos.objects.get(id=id).to_json(),
                'examen_microscopico_hematies': ExamenMicroscopicoHematies.objects.get(id=id).to_json(),
                #'examen_microscopico_cilindros': ExamenMicroscopicoCilindros.objects.get(id=id).to_json(),
                #'examen_microscopico_mucus': ExamenMicroscopicoMucus.objects.get(id=id).to_json(),
                #'examen_microscopico_cristales': ExamenMicroscopicoCristales.objects.get(id=id).to_json(),
                #'examen_microscopico_germenes': ExamenMicroscopicoGermenes.objects.get(id=id).to_json(),
                'examen_fisico_reaccion': ExamenFisicoReaccion.objects.get(id=id).to_json(),
                #'examen_fisico_aspecto': ExamenFisicoAspecto.objects.get(id=id).to_json(),
                'bilirrubina_total': BilirrubinaTotal.objects.get(id=id).to_json(),
                'bilirrubina_directa': BilirrubinaDirecta.objects.get(id=id).to_json(),
                'bilirrubina_indirecta': BilirrubinaIndirecta.objects.get(id=id).to_json(),
                'fosfatasa_alcalina_recien_nacido': FosfatasaAlcalinaRecienNacido.objects.get(id=id).to_json(),
                'fosfatasa_alcalina_bebe': FosfatasaAlcalinaBebe.objects.get(id=id).to_json(),
                'fosfatasa_alcalina_ninio': FosfatasaAlcalinaNinio.objects.get(id=id).to_json(),
                'fosfatasa_alcalina_adulto': FosfatasaAlcalinaAdulto.objects.get(id=id).to_json(),
                'glutamico_piruvica_hombre': GlutamicoPiruvicaHombre.objects.get(id=id).to_json(),
                'glutamico_piruvica_mujer': GlutamicoPiruvicaMujer.objects.get(id=id).to_json(),
                'glutamico_oxalacetica_hombre': GlutamicoOxalaceticaHombre.objects.get(id=id).to_json(),
                'glutamico_oxalacetica_mujer': GlutamicoOxalaceticaMujer.objects.get(id=id).to_json(),
                'trigliceridos': Trigliceridos.objects.get(id=id).to_json(),
                'colesterol_total': ColesterolTotal.objects.get(id=id).to_json(),
                'hdl_hombre': HdlHombre.objects.get(id=id).to_json(),
                'hdl_mujer': HdlMujer.objects.get(id=id).to_json(),
                'ldl': Ldl.objects.get(id=id).to_json(),
                'creatinina': Creatinina.objects.get(id=id).to_json(),
                'urea': Urea.objects.get(id=id).to_json(),
                'glucosa': Glucosa.objects.get(id=id).to_json(),
                'globulos_rojos_total_mujer': GlobulosRojosTotalMujer.objects.get(id=id).to_json(),
                'globulos_rojos_total_hombre': GlobulosRojosTotalHombre.objects.get(id=id).to_json(),
                'hematocritos_hombre': HematocritosHombre.objects.get(id=id).to_json(),
                'hematocritos_mujer': HematocritosMujer.objects.get(id=id).to_json(),
                'hemoglobina_g_hombre': HemoglobinaGHombre.objects.get(id=id).to_json(),
                'hemoglobina_g_mujer': HemoglobinaGMujer.objects.get(id=id).to_json(),
                'serie_roja_aspecto': SerieRojaAspecto.objects.get(id=id).to_json(),
                'leucocitos': Leucocitos.objects.get(id=id).to_json(),
                'neutrofilos_cayado': NeutrofilosCayado.objects.get(id=id).to_json(),
                'neutrofilos_segmentado': NeutrofilosSegmentado.objects.get(id=id).to_json(),
                'eosinofilos': Eosinofilos.objects.get(id=id).to_json(),
                'basofilos': Basofilos.objects.get(id=id).to_json(),
                'linfocitos': Linfocitos.objects.get(id=id).to_json(),
                'monocitos': Monocitos.objects.get(id=id).to_json(),
                'plaquetas': Plaquetas.objects.get(id=id).to_json()
            }
            return Response(conf_rutinas, mimetype='application/json', status=200)
        except:
            return Response(status=404)

    def put(self, id):
        try:
            ExamenFisicoDensidad.objects.filter(id=id).update(**request.json)
            ExamenMicroscopicoEpitelial.objects.filter(id=id).update(**request.json)
            ExamenMicroscopicoLeucocitos.objects.filter(id=id).update(**request.json)
            ExamenMicroscopicoHematies.objects.filter(id=id).update(**request.json)
            #ExamenMicroscopicoCilindros.objects.filter(id=id).update(**request.json)
            #ExamenMicroscopicoMucus.objects.filter(id=id).update(**request.json)
            #ExamenMicroscopicoCristales.objects.filter(id=id).update(**request.json)
            #ExamenMicroscopicoGermenes.objects.filter(id=id).update(**request.json)
            ExamenFisicoReaccion.objects.filter(id=id).update(**request.json)
            #ExamenFisicoAspecto.objects.filter(id=id).update(**request.json)
            BilirrubinaTotal.objects.filter(id=id).update(**request.json)
            BilirrubinaDirecta.objects.filter(id=id).update(**request.json)
            BilirrubinaIndirecta.objects.filter(id=id).update(**request.json)
            FosfatasaAlcalinaRecienNacido.objects.filter(id=id).update(**request.json)
            FosfatasaAlcalinaBebe.objects.filter(id=id).update(**request.json)
            FosfatasaAlcalinaNinio.objects.filter(id=id).update(**request.json)
            FosfatasaAlcalinaAdulto.objects.filter(id=id).update(**request.json)
            GlutamicoPiruvicaHombre.objects.filter(id=id).update(**request.json)
            GlutamicoPiruvicaMujer.objects.filter(id=id).update(**request.json)
            GlutamicoOxalaceticaHombre.objects.filter(id=id).update(**request.json)
            GlutamicoOxalaceticaMujer.objects.filter(id=id).update(**request.json)
            Trigliceridos.objects.filter(id=id).update(**request.json)
            ColesterolTotal.objects.filter(id=id).update(**request.json)
            HdlHombre.objects.filter(id=id).update(**request.json)
            HdlMujer.objects.filter(id=id).update(**request.json)
            Ldl.objects.filter(id=id).update(**request.json)
            Creatinina.objects.filter(id=id).update(**request.json)
            Urea.objects.filter(id=id).update(**request.json)
            Glucosa.objects.filter(id=id).update(**request.json)
            GlobulosRojosTotalMujer.objects.filter(id=id).update(**request.json)
            GlobulosRojosTotalHombre.objects.filter(id=id).update(**request.json)
            HematocritosHombre.objects.filter(id=id).update(**request.json)
            HematocritosMujer.objects.filter(id=id).update(**request.json)
            HemoglobinaGHombre.objects.filter(id=id).update(**request.json)
            HemoglobinaGMujer.objects.filter(id=id).update(**request.json)
            SerieRojaAspecto.objects.filter(id=id).update(**request.json)
            Leucocitos.objects.filter(id=id).update(**request.json)
            NeutrofilosCayado.objects.filter(id=id).update(**request.json)
            NeutrofilosSegmentado.objects.filter(id=id).update(**request.json)
            Eosinofilos.objects.filter(id=id).update(**request.json)
            Basofilos.objects.filter(id=id).update(**request.json)
            Linfocitos.objects.filter(id=id).update(**request.json)
            Monocitos.objects.filter(id=id).update(**request.json)
            Plaquetas.objects.filter(id=id).update(**request.json)
            return Response(status=200)
        except:
            return Response(status=404)


    def delete(self, id):
        try:
            ExamenFisicoDensidad.objects.filter(id=id).delete()
            ExamenMicroscopicoEpitelial.objects.filter(id=id).delete()
            ExamenMicroscopicoLeucocitos.objects.filter(id=id).delete()
            ExamenMicroscopicoHematies.objects.filter(id=id).delete()
            #ExamenMicroscopicoCilindros.objects.filter(id=id).delete()
            #ExamenMicroscopicoMucus.objects.filter(id=id).delete()
            #ExamenMicroscopicoCristales.objects.filter(id=id).delete()
            #ExamenMicroscopicoGermenes.objects.filter(id=id).delete()
            ExamenFisicoReaccion.objects.filter(id=id).delete()
            #ExamenFisicoAspecto.objects.filter(id=id).delete()
            BilirrubinaTotal.objects.filter(id=id).delete()
            BilirrubinaDirecta.objects.filter(id=id).delete()
            BilirrubinaIndirecta.objects.filter(id=id).delete()
            FosfatasaAlcalinaRecienNacido.objects.filter(id=id).delete()
            FosfatasaAlcalinaBebe.objects.filter(id=id).delete()
            FosfatasaAlcalinaNinio.objects.filter(id=id).delete()
            FosfatasaAlcalinaAdulto.objects.filter(id=id).delete()
            GlutamicoPiruvicaHombre.objects.filter(id=id).delete()
            GlutamicoPiruvicaMujer.objects.filter(id=id).delete()
            GlutamicoOxalaceticaHombre.objects.filter(id=id).delete()
            GlutamicoOxalaceticaMujer.objects.filter(id=id).delete()
            Trigliceridos.objects.filter(id=id).delete()
            ColesterolTotal.objects.filter(id=id).delete()
            HdlHombre.objects.filter(id=id).delete()
            HdlMujer.objects.filter(id=id).delete()
            Ldl.objects.filter(id=id).delete()
            Creatinina.objects.filter(id=id).delete()
            Urea.objects.filter(id=id).delete()
            Glucosa.objects.filter(id=id).delete()
            GlobulosRojosTotalMujer.objects.filter(id=id).delete()
            GlobulosRojosTotalHombre.objects.filter(id=id).delete()
            HematocritosHombre.objects.filter(id=id).delete()
            HematocritosMujer.objects.filter(id=id).delete()
            HemoglobinaGHombre.objects.filter(id=id).delete()
            HemoglobinaGMujer.objects.filter(id=id).delete()
            SerieRojaAspecto.objects.filter(id=id).delete()
            Leucocitos.objects.filter(id=id).delete()
            NeutrofilosCayado.objects.filter(id=id).delete()
            NeutrofilosSegmentado.objects.filter(id=id).delete()
            Eosinofilos.objects.filter(id=id).delete()
            Basofilos.objects.filter(id=id).delete()
            Linfocitos.objects.filter(id=id).delete()
            Monocitos.objects.filter(id=id).delete()
            Plaquetas.objects.filter(id=id).delete()
            return Response(status=200)
        except:
            return Response(status=404)

class ConfiguracionRutinasApi(Resource):
    def get(self, id):
        try:
            conf_rutinas = {
                'examen_fisico_densidad': ExamenFisicoDensidad.objects.get(id=id).to_json(),
                'examen_microscopico_epitelial': ExamenMicroscopicoEpitelial.objects.get(id=id).to_json(),
                'examen_microscopico_leucocitos': ExamenMicroscopicoLeucocitos.objects.get(id=id).to_json(),
                'examen_microscopico_hematies': ExamenMicroscopicoHematies.objects.get(id=id).to_json(),
                #'examen_microscopico_cilindros': ExamenMicroscopicoCilindros.objects.get(id=id).to_json(),
                #'examen_microscopico_mucus': ExamenMicroscopicoMucus.objects.get(id=id).to_json(),
                #'examen_microscopico_cristales': ExamenMicroscopicoCristales.objects.get(id=id).to_json(),
                #'examen_microscopico_germenes': ExamenMicroscopicoGermenes.objects.get(id=id).to_json(),
                'examen_fisico_reaccion': ExamenFisicoReaccion.objects.get(id=id).to_json(),
                #'examen_fisico_aspecto': ExamenFisicoAspecto.objects.get(id=id).to_json(),
                'bilirrubina_total': BilirrubinaTotal.objects.get(id=id).to_json(),
                'bilirrubina_directa': BilirrubinaDirecta.objects.get(id=id).to_json(),
                'bilirrubina_indirecta': BilirrubinaIndirecta.objects.get(id=id).to_json(),
                'fosfatasa_alcalina_recien_nacido': FosfatasaAlcalinaRecienNacido.objects.get(id=id).to_json(),
                'fosfatasa_alcalina_bebe': FosfatasaAlcalinaBebe.objects.get(id=id).to_json(),
                'fosfatasa_alcalina_ninio': FosfatasaAlcalinaNinio.objects.get(id=id).to_json(),
                'fosfatasa_alcalina_adulto': FosfatasaAlcalinaAdulto.objects.get(id=id).to_json(),
                'glutamico_piruvica_hombre': GlutamicoPiruvicaHombre.objects.get(id=id).to_json(),
                'glutamico_piruvica_mujer': GlutamicoPiruvicaMujer.objects.get(id=id).to_json(),
                'glutamico_oxalacetica_hombre': GlutamicoOxalaceticaHombre.objects.get(id=id).to_json(),
                'glutamico_oxalacetica_mujer': GlutamicoOxalaceticaMujer.objects.get(id=id).to_json(),
                'trigliceridos': Trigliceridos.objects.get(id=id).to_json(),
                'colesterol_total': ColesterolTotal.objects.get(id=id).to_json(),
                'hdl_hombre': HdlHombre.objects.get(id=id).to_json(),
                'hdl_mujer': HdlMujer.objects.get(id=id).to_json(),
                'ldl': Ldl.objects.get(id=id).to_json(),
                'creatinina': Creatinina.objects.get(id=id).to_json(),
                'urea': Urea.objects.get(id=id).to_json(),
                'glucosa': Glucosa.objects.get(id=id).to_json(),
                'globulos_rojos_total_mujer': GlobulosRojosTotalMujer.objects.get(id=id).to_json(),
                'globulos_rojos_total_hombre': GlobulosRojosTotalHombre.objects.get(id=id).to_json(),
                'hematocritos_hombre': HematocritosHombre.objects.get(id=id).to_json(),
                'hematocritos_mujer': HematocritosMujer.objects.get(id=id).to_json(),
                'hemoglobina_g_hombre': HemoglobinaGHombre.objects.get(id=id).to_json(),
                'hemoglobina_g_mujer': HemoglobinaGMujer.objects.get(id=id).to_json(),
                'serie_roja_aspecto': SerieRojaAspecto.objects.get(id=id).to_json(),
                'leucocitos': Leucocitos.objects.get(id=id).to_json(),
                'neutrofilos_cayado': NeutrofilosCayado.objects.get(id=id).to_json(),
                'neutrofilos_segmentado': NeutrofilosSegmentado.objects.get(id=id).to_json(),
                'eosinofilos': Eosinofilos.objects.get(id=id).to_json(),
                'basofilos': Basofilos.objects.get(id=id).to_json(),
                'linfocitos': Linfocitos.objects.get(id=id).to_json(),
                'monocitos': Monocitos.objects.get(id=id).to_json(),
                'plaquetas': Plaquetas.objects.get(id=id).to_json()
            }
            return Response(conf_rutinas, mimetype='application/json', status=200)
        except:
            return 'get not found!', 404

    def post(self):
        try:
            body = request.get_json()
            if body is None:
                return 'No data', 400
            
            

            return {'id': str(id)}, 200
        except:
            return 'post error!', 500