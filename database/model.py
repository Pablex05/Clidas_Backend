from .db import db

# ============================================================
# ================== Examen Fisico Orina =====================
class ExamenFisicoDensidad(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)

class ExamenFisicoReaccion(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)

class ExamenFisicoAspecto(db.Document):
    aspecto = db.StringField(required=True)
    color = db.StringField(required=True)
# ============================================================
# ================ Examen Microscopico Orina =================
class ExamenMicroscopicoEpitelial(db.Document):
    observacion = db.StringField(required=True)

class ExamenMicroscopicoLeucocitos(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)

class ExamenMicroscopicoHematies(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)

class ExamenMicroscopicoCilindros(db.Document):
    observacion = db.StringField(required=True)

class ExamenMicroscopicoMucus(db.Document):
    observacion = db.StringField(required=True)

class ExamenMicroscopicoCristales(db.Document):
    observacion = db.StringField(required=True)

class ExamenMicroscopicoGermenes(db.Document):
    observacion = db.StringField(required=True)
# ============================================================
# ================== Examen Quimico Sanguineo ================
class BilirrubinaTotal(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)

class BilirrubinaDirecta(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)

class BilirrubinaIndirecta(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)
# ============================================================
class FosfatasaAlcalinaRecienNacido(db.Document): # 0 a 14 dias
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)

class FosfatasaAlcalinaBebe(db.Document): # 15 dias a 11 meses
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)

class FosfatasaAlcalinaNinio(db.Document):  # 1 a 9 años
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)

class FosfatasaAlcalinaAdulto(db.Document): # mayor de 9 años
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)
# ============================================================
class GlutamicoPiruvicaHombre(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)

class GlutamicoPiruvicaMujer(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)
# ============================================================
class GlutamicoOxalaceticaHombre(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)

class GlutamicoOxalaceticaMujer(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)
# ============================================================
class Trigliceridos(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)
# ============================================================
class ColesterolTotal(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)

class HdlHombre(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)

class HdlMujer(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)

class Ldl(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)
# ============================================================
class Creatinina(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)
    material = db.StringField(required=True)
    metodo = db.StringField(required=True)
# ============================================================
class Urea(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)
    material = db.StringField(required=True)
    metodo = db.StringField(required=True)
# ============================================================
class Glucosa(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)
    material = db.StringField(required=True)
    metodo = db.StringField(required=True)
# ============================================================
# ================= Examen Hematologico ======================
# ===================== Serie Roja ===========================
class GlobulosRojosTotalMujer(db.Document):
    min = db.IntegerField(required=True)
    max = db.IntegerField(required=True)

class GlobulosRojosTotalHombre(db.Document):
    min = db.IntegerField(required=True)
    max = db.IntegerField(required=True)
# ============================================================
class HematocritosHombre(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)

class HematocritosMujer(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)
# ============================================================
class HemoglobinaGHombre(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)

class HemoglobinaGMujer(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)
# ============================================================
class SerieRojaAspecto(db.Document):
    morfologia = db.StringField(required=True)
    color = db.StringField(required=True)
# ============================================================
# ==================== Serie Blanca ==========================
class Leucocitos(db.Document):
    min = db.IntegerField(required=True)
    max = db.IntegerField(required=True)

class NeutrofilosCayado(db.Document):
    min = db.IntegerField(required=True)
    max = db.IntegerField(required=True)

class NeutrofilosSegmentado(db.Document):
    min = db.IntegerField(required=True)
    max = db.IntegerField(required=True)

class Eosinofilos(db.Document):
    min = db.IntegerField(required=True)
    max = db.IntegerField(required=True)

class Basofilos(db.Document):
    min = db.IntegerField(required=True)
    max = db.IntegerField(required=True)

class Linfocitos(db.Document):
    min = db.IntegerField(required=True)
    max = db.IntegerField(required=True)

class Monocitos(db.Document):
    min = db.IntegerField(required=True)
    max = db.IntegerField(required=True)
