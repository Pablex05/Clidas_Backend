from flask import Response, jsonify, request
from flask_restful import Resource
from database.model import *

class ConfiguracionesRutinasApi(Resource):
    def get(self):
        try:
            return jsonify({
                "examen_fisico_densidad": ExamenFisicoDensidad.objects.to_json(),
                #"examen_microscopico_epitelial": ExamenMicroscopicoEpitelial.objects.to_json(),
                "examen_microscopico_leucocitos": ExamenMicroscopicoLeucocitos.objects.to_json(),
                "examen_microscopico_hematies": ExamenMicroscopicoHematies.objects.to_json(),
                #"examen_microscopico_cilindros": ExamenMicroscopicoCilindros.objects.to_json(),
                #"examen_microscopico_mucus": ExamenMicroscopicoMucus.objects.to_json(),
                #"examen_microscopico_cristales": ExamenMicroscopicoCristales.objects.to_json(),
                #"examen_microscopico_germenes": ExamenMicroscopicoGermenes.objects.to_json(),
                "examen_fisico_reaccion": ExamenFisicoReaccion.objects.to_json(),
                #"examen_fisico_aspecto": ExamenFisicoAspecto.objects.to_json(),
                "bilirrubina_total": BilirrubinaTotal.objects.to_json(),
                "bilirrubina_directa": BilirrubinaDirecta.objects.to_json(),
                "bilirrubina_indirecta": BilirrubinaIndirecta.objects.to_json(),
                "fosfatasa_alcalina_recien_nacido": FosfatasaAlcalinaRecienNacido.objects.to_json(),
                "fosfatasa_alcalina_bebe": FosfatasaAlcalinaBebe.objects.to_json(),
                "fosfatasa_alcalina_ninio": FosfatasaAlcalinaNinio.objects.to_json(),
                "fosfatasa_alcalina_adulto": FosfatasaAlcalinaAdulto.objects.to_json(),
                "glutamico_piruvica_hombre": GlutamicoPiruvicaHombre.objects.to_json(),
                "glutamico_piruvica_mujer": GlutamicoPiruvicaMujer.objects.to_json(),
                "glutamico_oxalacetica_hombre": GlutamicoOxalaceticaHombre.objects.to_json(),
                "glutamico_oxalacetica_mujer": GlutamicoOxalaceticaMujer.objects.to_json(),
                "trigliceridos": Trigliceridos.objects.to_json(),
                "colesterol_total": ColesterolTotal.objects.to_json(),
                "hdl_hombre": HdlHombre.objects.to_json(),
                "hdl_mujer": HdlMujer.objects.to_json(),
                "ldl": Ldl.objects.to_json(),
                "creatinina": Creatinina.objects.to_json(),
                "urea": Urea.objects.to_json(),
                "glucosa": Glucosa.objects.to_json(),
                "globulos_rojos_total_mujer": GlobulosRojosTotalMujer.objects.to_json(),
                "globulos_rojos_total_hombre": GlobulosRojosTotalHombre.objects.to_json(),
                "hematocritos_hombre": HematocritosHombre.objects.to_json(),
                "hematocritos_mujer": HematocritosMujer.objects.to_json(),
                "hemoglobina_g_hombre": HemoglobinaGHombre.objects.to_json(),
                "hemoglobina_g_mujer": HemoglobinaGMujer.objects.to_json(),
                #"serie_roja_aspecto": SerieRojaAspecto.objects.to_json(),
                "leucocitos": Leucocitos.objects.to_json(),
                "neutrofilos_cayado": NeutrofilosCayado.objects.to_json(),
                "neutrofilos_segmentado": NeutrofilosSegmentado.objects.to_json(),
                #"eosinofilos": Eosinofilos.objects.to_json(),
                "basofilos": Basofilos.objects.to_json(),
                "linfocitos": Linfocitos.objects.to_json(),
                "monocitos": Monocitos.objects.to_json(),
                "plaquetas": Plaquetas.objects.to_json()
            })
        except:
            return Response(status=404)
    def post(self):
        try:
            data = request.get_json()
            if data["examen_fisico_densidad"]:
                ExamenFisicoDensidad.objects.create(**data["examen_fisico_densidad"])
            if data["examen_fisico_reaccion"]:
                ExamenFisicoReaccion.objects.create(**data["examen_fisico_reaccion"])
            #if data["examen_microscopico_epitelial"]:
            #    ExamenMicroscopicoEpitelial.objects.create(**data["examen_microscopico_epitelial"])
            if data["examen_microscopico_leucocitos"]:
                ExamenMicroscopicoLeucocitos.objects.create(**data["examen_microscopico_leucocitos"])
            if data["examen_microscopico_hematies"]:
                ExamenMicroscopicoHematies.objects.create(**data["examen_microscopico_hematies"])
            #if data["examen_microscopico_cilindros"]:
            #    ExamenMicroscopicoCilindros.objects.create(**data["examen_microscopico_cilindros"])
            #if data["examen_microscopico_mucus"]:
            #    ExamenMicroscopicoMucus.objects.create(**data["examen_microscopico_mucus"])
            #if data["examen_microscopico_cristales"]:
            #    ExamenMicroscopicoCristales.objects.create(**data["examen_microscopico_cristales"])
            #if data["examen_microscopico_germenes"]:
            #    ExamenMicroscopicoGermenes.objects.create(**data["examen_microscopico_germenes"])
            #if data["examen_fisico_aspecto"]:
            #    ExamenFisicoAspecto.objects.create(**data["examen_fisico_aspecto"])
            if data["bilirrubina_total"]:
                BilirrubinaTotal.objects.create(**data["bilirrubina_total"])
            if data["bilirrubina_directa"]:
                BilirrubinaDirecta.objects.create(**data["bilirrubina_directa"])
            if data["bilirrubina_indirecta"]:
                BilirrubinaIndirecta.objects.create(**data["bilirrubina_indirecta"])
            if data["fosfatasa_alcalina_recien_nacido"]:
                FosfatasaAlcalinaRecienNacido.objects.create(**data["fosfatasa_alcalina_recien_nacido"])
            if data["fosfatasa_alcalina_bebe"]:
                FosfatasaAlcalinaBebe.objects.create(**data["fosfatasa_alcalina_bebe"])
            if data["fosfatasa_alcalina_ninio"]:
                FosfatasaAlcalinaNinio.objects.create(**data["fosfatasa_alcalina_ninio"])
            if data["fosfatasa_alcalina_adulto"]:
                FosfatasaAlcalinaAdulto.objects.create(**data["fosfatasa_alcalina_adulto"])
            if data["glutamico_piruvica_hombre"]:
                GlutamicoPiruvicaHombre.objects.create(**data["glutamico_piruvica_hombre"])
            if data["glutamico_piruvica_mujer"]:
                GlutamicoPiruvicaMujer.objects.create(**data["glutamico_piruvica_mujer"])
            if data["glutamico_oxalacetica_hombre"]:
                GlutamicoOxalaceticaHombre.objects.create(**data["glutamico_oxalacetica_hombre"])
            if data["glutamico_oxalacetica_mujer"]:
                GlutamicoOxalaceticaMujer.objects.create(**data["glutamico_oxalacetica_mujer"])
            if data["trigliceridos"]:
                Trigliceridos.objects.create(**data["trigliceridos"])
            if data["colesterol_total"]:
                ColesterolTotal.objects.create(**data["colesterol_total"])
            if data["hdl_hombre"]:
                HdlHombre.objects.create(**data["hdl_hombre"])
            if data["hdl_mujer"]:
                HdlMujer.objects.create(**data["hdl_mujer"])
            if data["ldl"]:
                Ldl.objects.create(**data["ldl"])
            if data["creatinina"]:
                Creatinina.objects.create(**data["creatinina"])
            if data["urea"]:
                Urea.objects.create(**data["urea"])
            if data["glucosa"]:
                Glucosa.objects.create(**data["glucosa"])
            if data["globulos_rojos_total_hombre"]:
                GlobulosRojosTotalHombre.objects.create(**data["globulos_rojos_total_hombre"])
            if data["globulos_rojos_total_mujer"]:
                GlobulosRojosTotalMujer.objects.create(**data["globulos_rojos_total_mujer"])
            if data["hematocritos_hombre"]:
                HematocritosHombre.objects.create(**data["hematocritos_hombre"])
            if data["hematocritos_mujer"]:
                HematocritosMujer.objects.create(**data["hematocritos_mujer"])
            if data["hemoglobina_g_hombre"]:
                HemoglobinaGHombre.objects.create(**data["hemoglobina_g_hombre"])
            if data["hemoglobina_g_mujer"]:
                HemoglobinaGMujer.objects.create(**data["hemoglobina_g_mujer"])
            if data["leucocitos"]:
                Leucocitos.objects.create(**data["leucocitos"])
            if data["neutrofilos_cayado"]:
                NeutrofilosCayado.objects.create(**data["neutrofilos_cayado"])
            if data["neutrofilos_segmentado"]:
                NeutrofilosSegmentado.objects.create(**data["neutrofilos_segmentado"])
            #if data["eosinofilos"]:
            #    Eosinofilos.objects.create(**data["eosinofilos"])
            if data["basofilos"]:
                Basofilos.objects.create(**data["basofilos"])
            if data["monocitos"]:
                Monocitos.objects.create(**data["monocitos"])
            if data["linfocitos"]:
                Linfocitos.objects.create(**data["linfocitos"])
            if data["plaquetas"]:
                Plaquetas.objects.create(**data["plaquetas"])
            #if data["serie_roja_aspecto"]:
            #    SerieRojaAspecto.objects.create(**data["serie_roja_aspecto"])
            
            return Response(status=200)
        except:
            return Response(status=404)







class ConfiguracionRutinasApi(Resource):
    def get(self, id):
        try:
            conf_rutinas = {
                "examen_fisico_densidad": ExamenFisicoDensidad.objects.get(id=id).to_json(),
                "examen_microscopico_epitelial": ExamenMicroscopicoEpitelial.objects.get(id=id).to_json(),
                "examen_microscopico_leucocitos": ExamenMicroscopicoLeucocitos.objects.get(id=id).to_json(),
                "examen_microscopico_hematies": ExamenMicroscopicoHematies.objects.get(id=id).to_json(),
                #"examen_microscopico_cilindros": ExamenMicroscopicoCilindros.objects.get(id=id).to_json(),
                #"examen_microscopico_mucus": ExamenMicroscopicoMucus.objects.get(id=id).to_json(),
                #"examen_microscopico_cristales": ExamenMicroscopicoCristales.objects.get(id=id).to_json(),
                #"examen_microscopico_germenes": ExamenMicroscopicoGermenes.objects.get(id=id).to_json(),
                "examen_fisico_reaccion": ExamenFisicoReaccion.objects.get(id=id).to_json(),
                #"examen_fisico_aspecto": ExamenFisicoAspecto.objects.get(id=id).to_json(),
                "bilirrubina_total": BilirrubinaTotal.objects.get(id=id).to_json(),
                "bilirrubina_directa": BilirrubinaDirecta.objects.get(id=id).to_json(),
                "bilirrubina_indirecta": BilirrubinaIndirecta.objects.get(id=id).to_json(),
                "fosfatasa_alcalina_recien_nacido": FosfatasaAlcalinaRecienNacido.objects.get(id=id).to_json(),
                "fosfatasa_alcalina_bebe": FosfatasaAlcalinaBebe.objects.get(id=id).to_json(),
                "fosfatasa_alcalina_ninio": FosfatasaAlcalinaNinio.objects.get(id=id).to_json(),
                "fosfatasa_alcalina_adulto": FosfatasaAlcalinaAdulto.objects.get(id=id).to_json(),
                "glutamico_piruvica_hombre": GlutamicoPiruvicaHombre.objects.get(id=id).to_json(),
                "glutamico_piruvica_mujer": GlutamicoPiruvicaMujer.objects.get(id=id).to_json(),
                "glutamico_oxalacetica_hombre": GlutamicoOxalaceticaHombre.objects.get(id=id).to_json(),
                "glutamico_oxalacetica_mujer": GlutamicoOxalaceticaMujer.objects.get(id=id).to_json(),
                "trigliceridos": Trigliceridos.objects.get(id=id).to_json(),
                "colesterol_total": ColesterolTotal.objects.get(id=id).to_json(),
                "hdl_hombre": HdlHombre.objects.get(id=id).to_json(),
                "hdl_mujer": HdlMujer.objects.get(id=id).to_json(),
                "ldl": Ldl.objects.get(id=id).to_json(),
                "creatinina": Creatinina.objects.get(id=id).to_json(),
                "urea": Urea.objects.get(id=id).to_json(),
                "glucosa": Glucosa.objects.get(id=id).to_json(),
                "globulos_rojos_total_mujer": GlobulosRojosTotalMujer.objects.get(id=id).to_json(),
                "globulos_rojos_total_hombre": GlobulosRojosTotalHombre.objects.get(id=id).to_json(),
                "hematocritos_hombre": HematocritosHombre.objects.get(id=id).to_json(),
                "hematocritos_mujer": HematocritosMujer.objects.get(id=id).to_json(),
                "hemoglobina_g_hombre": HemoglobinaGHombre.objects.get(id=id).to_json(),
                "hemoglobina_g_mujer": HemoglobinaGMujer.objects.get(id=id).to_json(),
                "serie_roja_aspecto": SerieRojaAspecto.objects.get(id=id).to_json(),
                "leucocitos": Leucocitos.objects.get(id=id).to_json(),
                "neutrofilos_cayado": NeutrofilosCayado.objects.get(id=id).to_json(),
                "neutrofilos_segmentado": NeutrofilosSegmentado.objects.get(id=id).to_json(),
                "eosinofilos": Eosinofilos.objects.get(id=id).to_json(),
                "basofilos": Basofilos.objects.get(id=id).to_json(),
                "linfocitos": Linfocitos.objects.get(id=id).to_json(),
                "monocitos": Monocitos.objects.get(id=id).to_json(),
                "plaquetas": Plaquetas.objects.get(id=id).to_json()
            }
            return Response(conf_rutinas, mimetype='application/json', status=200)
        except:
            return 'get not found!', 404

    
