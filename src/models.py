from flask import jsonify
from app import db


class Analisis(db.Model):
    __tablename__ = 'analisis'
    id = db.Column(db.Integer, primary_key=True)
    analisis_hematologico_id = db.Column(db.Integer, db.ForeignKey('analisis_hematologico.id'))
    analisis_quimico_sanguinea_id = db.Column(db.Integer, db.ForeignKey('analisis_quimico_sanguinea.id'))
    analisis_orina_id = db.Column(db.Integer, db.ForeignKey('analisis_orina.id'))
    analisis_hematologico = db.relationship('AnalisisHematologico', back_populates='analisis')
    analisis_quimico_sanguinea = db.relationship('AnalisisQuimicoSanguinea', back_populates='analisis')
    analisis_orina = db.relationship('AnalisisOrina', back_populates='analisis')

    def __init__(self, analisis_hematologico_id, analisis_quimico_sanguinea_id, analisis_orina_id):
        self.analisis_hematologico_id = analisis_hematologico_id
        self.analisis_quimico_sanguinea_id = analisis_quimico_sanguinea_id
        self.analisis_orina_id = analisis_orina_id

    def __repr__(self):
        return '<Analisis %r>' % self.id
    
    def serialize(self):
        return {
            'id': self.id,
            'analisis_hematologico_id': self.analisis_hematologico_id,
            'analisis_quimico_sanguinea_id': self.analisis_quimico_sanguinea_id,
            'analisis_orina_id': self.analisis_orina_id
        }
    
    # convert objet in json
    def to_json(self):
        return {
            'id': self.id,
            'analisis_hematologico_id': self.analisis_hematologico_id,
            'analisis_quimico_sanguinea_id': self.analisis_quimico_sanguinea_id,
            'analisis_orina_id': self.analisis_orina_id
        }
    
    # convert json in objet
    @staticmethod
    def from_json(json_analisis):
        return Analisis(
            analisis_hematologico_id=json_analisis.get('analisis_hematologico_id'),
            analisis_quimico_sanguinea_id=json_analisis.get('analisis_quimico_sanguinea_id'),
            analisis_orina_id=json_analisis.get('analisis_orina_id')
        )

class AnalisisHematologico(db.Model):
    __tablename__ = 'analisis_hematologico'
    id = db.Column(db.Integer, primary_key=True) 
    # plaquetas
    plaquetas_total = db.Column(db.Float, nullable=False)
    # Serie Blanca
    # leucocitos
    leucocitos_total = db.Column(db.Float, nullable=False)
    # neutrofilos
    neutrofilos_cayados = db.Column(db.Float, nullable=False)
    neutrofilos_segmentados = db.Column(db.Float, nullable=False)
    # eosinofilos
    eosinofilos_total = db.Column(db.Float, nullable=False)
    # basofilos
    basofilos_total = db.Column(db.Float, nullable=False)
    # monocitos
    monocitos_total = db.Column(db.Float, nullable=False)
    # serie roja
    # globulos rojos
    globulos_rojos_total = db.Column(db.Float, nullable=False)
    # hematocritos cantidad
    hematocritos_cantidad = db.Column(db.Float, nullable=False)
    # hematocritos g
    hematocritos_g = db.Column(db.Float, nullable=False)
    # morfologia_color
    morfologia_color = db.Column(db.String(80), nullable=False)

    # relatioship with Analisis
    analisis = db.relationship('Analisis', back_populates='analisis_hematologico')

    def __init__(self, plaquetas_total, leucocitos_total, neutrofilos_cayados, neutrofilos_segmentados, eosinofilos_total, basofilos_total, monocitos_total, globulos_rojos_total, hematocritos_cantidad, hematocritos_g, morfologia_color):
        self.plaquetas_total = plaquetas_total
        self.leucocitos_total = leucocitos_total
        self.neutrofilos_cayados = neutrofilos_cayados
        self.neutrofilos_segmentados = neutrofilos_segmentados
        self.eosinofilos_total = eosinofilos_total
        self.basofilos_total = basofilos_total
        self.monocitos_total = monocitos_total
        self.globulos_rojos_total = globulos_rojos_total
        self.hematocritos_cantidad = hematocritos_cantidad
        self.hematocritos_g = hematocritos_g
        self.morfologia_color = morfologia_color

    def __repr__(self):
        return '<AnalisisHematologico %r>' % self.id
    
    def serialize(self):
        return {
            'id': self.id,
            'plaquetas_total': self.plaquetas_total,
            'leucocitos_total': self.leucocitos_total,
            'neutrofilos_cayados': self.neutrofilos_cayados,
            'neutrofilos_segmentados': self.neutrofilos_segmentados,
            'eosinofilos_total': self.eosinofilos_total,
            'basofilos_total': self.basofilos_total,
            'monocitos_total': self.monocitos_total,
            'globulos_rojos_total': self.globulos_rojos_total,
            'hematocritos_cantidad': self.hematocritos_cantidad,
            'hematocritos_g': self.hematocritos_g,
            'morfologia_color': self.morfologia_color
        }
    
    # convert objet in json
    def to_json(self):
        return {
            'id': self.id,
            'plaquetas_total': self.plaquetas_total,
            'leucocitos_total': self.leucocitos_total,
            'neutrofilos_cayados': self.neutrofilos_cayados,
            'neutrofilos_segmentados': self.neutrofilos_segmentados,
            'eosinofilos_total': self.eosinofilos_total,
            'basofilos_total': self.basofilos_total,
            'monocitos_total': self.monocitos_total,
            'globulos_rojos_total': self.globulos_rojos_total,
            'hematocritos_cantidad': self.hematocritos_cantidad,
            'hematocritos_g': self.hematocritos_g,
            'morfologia_color': self.morfologia_color
        }
    
    # convert json in objet
    @staticmethod
    def from_json(json_analisis):
        return AnalisisHematologico(
            plaquetas_total=json_analisis.get('plaquetas_total'),
            leucocitos_total=json_analisis.get('leucocitos_total'),
            neutrofilos_cayados=json_analisis.get('neutrofilos_cayados'),
            neutrofilos_segmentados=json_analisis.get('neutrofilos_segmentados'),
            eosinofilos_total=json_analisis.get('eosinofilos_total'),
            basofilos_total=json_analisis.get('basofilos_total'),
            monocitos_total=json_analisis.get('monocitos_total'),
            globulos_rojos_total=json_analisis.get('globulos_rojos_total'),
            hematocritos_cantidad=json_analisis.get('hematocritos_cantidad'),
            hematocritos_g=json_analisis.get('hematocritos_g'),
            morfologia_color=json_analisis.get('morfologia_color')
        )

class AnalisisQuimicoSanguinea(db.Model):
    __tablename__ = 'analisis_quimico_sanguinea'
    id = db.Column(db.Integer, primary_key=True)
    # bilirrubina
    bilirrubina_total = db.Column(db.Float, nullable=False)
    bilirrubina_directa = db.Column(db.Float, nullable=False)
    bilirrubina_indirecta = db.Column(db.Float, nullable=False)
    # colesterol
    colesterol_total = db.Column(db.Float, nullable=False)
    # creatinina
    creatinina_total = db.Column(db.Float, nullable=False)
    creatinina_material = db.Column(db.String(80), nullable=False)
    creatinina_metodo = db.Column(db.String(80), nullable=False)
    # fosfatasa_alcalina
    fosfatasa_alcalina_total = db.Column(db.Float, nullable=False)
    fosfatasa_alcalina_directa = db.Column(db.Float, nullable=False)
    fosfatasa_alcalina_indirecta = db.Column(db.Float, nullable=False)
    # glucosa
    glucosa_total = db.Column(db.Float, nullable=False)
    glucosa_material = db.Column(db.String(80), nullable=False)
    glucosa_metodo = db.Column(db.String(80), nullable=False)
    # transaminasa glutamico-oxalacetica
    transaminasa_glutamico_oxalacetica_total = db.Column(db.Float, nullable=False)
    # glutamico piruvica
    glutamico_piruvica_total = db.Column(db.Float, nullable=False)
    # lipoproteinas de alta densidad
    lipoproteinas_alta_densidad_total = db.Column(db.Float, nullable=False)
    # lipoproteinas de baja densidad
    lipoproteinas_baja_densidad_total = db.Column(db.Float, nullable=False)
    
    #relationship with Analisis
    analisis_id = db.relationship('Analisis', back_populates='analisis_quimico_sanguinea')

    def __init__(self, bilirrubina_total, bilirrubina_directa, bilirrubina_indirecta, colesterol_total, creatinina_total, creatinina_material, creatinina_metodo, fosfatasa_alcalina_total, fosfatasa_alcalina_directa, fosfatasa_alcalina_indirecta, glucosa_total, glucosa_material, glucosa_metodo, transaminasa_glutamico_oxalacetica_total, glutamico_piruvica_total, lipoproteinas_alta_densidad_total, lipoproteinas_baja_densidad_total):
        self.bilirrubina_total = bilirrubina_total
        self.bilirrubina_directa = bilirrubina_directa
        self.bilirrubina_indirecta = bilirrubina_indirecta
        self.colesterol_total = colesterol_total
        self.creatinina_total = creatinina_total
        self.creatinina_material = creatinina_material
        self.creatinina_metodo = creatinina_metodo
        self.fosfatasa_alcalina_total = fosfatasa_alcalina_total
        self.fosfatasa_alcalina_directa = fosfatasa_alcalina_directa
        self.fosfatasa_alcalina_indirecta = fosfatasa_alcalina_indirecta
        self.glucosa_total = glucosa_total
        self.glucosa_material = glucosa_material
        self.glucosa_metodo = glucosa_metodo
        self.transaminasa_glutamico_oxalacetica_total = transaminasa_glutamico_oxalacetica_total
        self.glutamico_piruvica_total = glutamico_piruvica_total
        self.lipoproteinas_alta_densidad_total = lipoproteinas_alta_densidad_total
        self.lipoproteinas_baja_densidad_total = lipoproteinas_baja_densidad_total

    def __repr__(self):
        return '<Hemoglobina %r>' % self.id

    def serialize(self):
        return {
            'bilirrubina_total': self.bilirrubina_total,
            'bilirrubina_directa': self.bilirrubina_directa,
            'bilirrubina_indirecta': self.bilirrubina_indirecta,
            'colesterol_total': self.colesterol_total,
            'creatinina_total': self.creatinina_total,
            'creatinina_material': self.creatinina_material,
            'creatinina_metodo': self.creatinina_metodo,
            'fosfatasa_alcalina_total': self.fosfatasa_alcalina_total,
            'fosfatasa_alcalina_directa': self.fosfatasa_alcalina_directa,
            'fosfatasa_alcalina_indirecta': self.fosfatasa_alcalina_indirecta,
            'glucosa_total': self.glucosa_total,
            'glucosa_material': self.glucosa_material,
            'glucosa_metodo': self.glucosa_metodo,
            'transaminasa_glutamico_oxalacetica_total': self.transaminasa_glutamico_oxalacetica_total,
            'glutamico_piruvica_total': self.glutamico_piruvica_total,
            'lipoproteinas_alta_densidad_total': self.lipoproteinas_alta_densidad_total,
            'lipoproteinas_baja_densidad_total': self.lipoproteinas_baja_densidad_total
        }
    
    # convert object in json
    def json(self):
        return {
            'bilirrubina_total': self.bilirrubina_total,
            'bilirrubina_directa': self.bilirrubina_directa,
            'bilirrubina_indirecta': self.bilirrubina_indirecta,
            'colesterol_total': self.colesterol_total,
            'creatinina_total': self.creatinina_total,
            'creatinina_material': self.creatinina_material,
            'creatinina_metodo': self.creatinina_metodo,
            'fosfatasa_alcalina_total': self.fosfatasa_alcalina_total,
            'fosfatasa_alcalina_directa': self.fosfatasa_alcalina_directa,
            'fosfatasa_alcalina_indirecta': self.fosfatasa_alcalina_indirecta,
            'glucosa_total': self.glucosa_total,
            'glucosa_material': self.glucosa_material,
            'glucosa_metodo': self.glucosa_metodo,
            'transaminasa_glutamico_oxalacetica_total': self.transaminasa_glutamico_oxalacetica_total,
            'glutamico_piruvica_total': self.glutamico_piruvica_total,
            'lipoproteinas_alta_densidad_total': self.lipoproteinas_alta_densidad_total,
            'lipoproteinas_baja_densidad_total': self.lipoproteinas_baja_densidad_total
        }
    
    # convert object in json
    def from_json(json_analisis):
        return AnalisisQuimicoSanguinea(
            bilirrubina_total=json_analisis.get('bilirrubina_total'),
            bilirrubina_directa=json_analisis.get('bilirrubina_directa'),
            bilirrubina_indirecta=json_analisis.get('bilirrubina_indirecta'),
            colesterol_total=json_analisis.get('colesterol_total'),
            creatinina_total=json_analisis.get('creatinina_total'),
            creatinina_material=json_analisis.get('creatinina_material'),
            creatinina_metodo=json_analisis.get('creatinina_metodo'),
            fosfatasa_alcalina_total=json_analisis.get('fosfatasa_alcalina_total'),
            fosfatasa_alcalina_directa=json_analisis.get('fosfatasa_alcalina_directa'),
            fosfatasa_alcalina_indirecta=json_analisis.get('fosfatasa_alcalina_indirecta'),
            glucosa_total=json_analisis.get('glucosa_total'),
            glucosa_material=json_analisis.get('glucosa_material'),
            glucosa_metodo=json_analisis.get('glucosa_metodo'),
            transaminasa_glutamico_oxalacetica_total=json_analisis.get('transaminasa_glutamico_oxalacetica_total'),
            glutamico_piruvica_total=json_analisis.get('glutamico_piruvica_total'),
            lipoproteinas_alta_densidad_total=json_analisis.get('lipoproteinas_alta_densidad_total'),
            lipoproteinas_baja_densidad_total=json_analisis.get('lipoproteinas_baja_densidad_total')
        )

class AnalisisOrina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # examen fisico
    # densidad
    examen_fisico_densidad = db.Column(db.Float)
    # reaccion
    examen_fisico_reaccion = db.Column(db.Float)
    # aspecto
    examen_fisico_aspecto = db.Column(db.String(100))
    # color
    examen_fisico_color = db.Column(db.String(100))
    # examen microscopico
    # epiteliales
    examen_microscopico_epiteliales = db.Column(db.String(100))
    # leucocitos
    examen_microscopico_leucocitos = db.Column(db.Float)
    # piocitos
    examen_microscopico_piocitos = db.Column(db.String(100))
    # hematies
    examen_microscopico_hematies = db.Column(db.Float)
    # cilindros
    examen_microscopico_cilindros = db.Column(db.String(100))
    # mucus
    examen_microscopico_mucus = db.Column(db.String(100))
    # cristales
    examen_microscopico_cristales = db.Column(db.String(100))
    # germenes
    examen_microscopico_germenes = db.Column(db.String(100))

    #relationship with analisis
    analisis_id = db.relationship('Analisis', back_populates='analisis_orina')

    def __init__(self, examen_fisico_densidad, examen_fisico_reaccion, examen_fisico_aspecto, examen_fisico_color, examen_microscopico_epiteliales, examen_microscopico_leucocitos, examen_microscopico_piocitos, examen_microscopico_hematies, examen_microscopico_cilindros, examen_microscopico_mucus, examen_microscopico_cristales, examen_microscopico_germenes):
        self.examen_fisico_densidad = examen_fisico_densidad
        self.examen_fisico_reaccion = examen_fisico_reaccion
        self.examen_fisico_aspecto = examen_fisico_aspecto
        self.examen_fisico_color = examen_fisico_color
        self.examen_microscopico_epiteliales = examen_microscopico_epiteliales
        self.examen_microscopico_leucocitos = examen_microscopico_leucocitos
        self.examen_microscopico_piocitos = examen_microscopico_piocitos
        self.examen_microscopico_hematies = examen_microscopico_hematies
        self.examen_microscopico_cilindros = examen_microscopico_cilindros
        self.examen_microscopico_mucus = examen_microscopico_mucus
        self.examen_microscopico_cristales = examen_microscopico_cristales
        self.examen_microscopico_germenes = examen_microscopico_germenes
    
    def __repr__(self):
        return '<AnalisisOrina %r>' % self.id

    def serialize(self):
        return {
            'examen_fisico_densidad': self.examen_fisico_densidad,
            'examen_fisico_reaccion': self.examen_fisico_reaccion,
            'examen_fisico_aspecto': self.examen_fisico_aspecto,
            'examen_fisico_color': self.examen_fisico_color,
            'examen_microscopico_epiteliales': self.examen_microscopico_epiteliales,
            'examen_microscopico_leucocitos': self.examen_microscopico_leucocitos,
            'examen_microscopico_piocitos': self.examen_microscopico_piocitos,
            'examen_microscopico_hematies': self.examen_microscopico_hematies,
            'examen_microscopico_cilindros': self.examen_microscopico_cilindros,
            'examen_microscopico_mucus': self.examen_microscopico_mucus,
            'examen_microscopico_cristales': self.examen_microscopico_cristales,
            'examen_microscopico_germenes': self.examen_microscopico_germenes
        }

    def to_json(self):
        return {
            'examen_fisico_densidad': self.examen_fisico_densidad,
            'examen_fisico_reaccion': self.examen_fisico_reaccion,
            'examen_fisico_aspecto': self.examen_fisico_aspecto,
            'examen_fisico_color': self.examen_fisico_color,
            'examen_microscopico_epiteliales': self.examen_microscopico_epiteliales,
            'examen_microscopico_leucocitos': self.examen_microscopico_leucocitos,
            'examen_microscopico_piocitos': self.examen_microscopico_piocitos,
            'examen_microscopico_hematies': self.examen_microscopico_hematies,
            'examen_microscopico_cilindros': self.examen_microscopico_cilindros,
            'examen_microscopico_mucus': self.examen_microscopico_mucus,
            'examen_microscopico_cristales': self.examen_microscopico_cristales,
            'examen_microscopico_germenes': self.examen_microscopico_germenes
        }
    
    def from_json(json_analisis):
        return AnalisisOrina(
            examen_fisico_densidad=json_analisis.get('examen_fisico_densidad'),
            examen_fisico_reaccion=json_analisis.get('examen_fisico_reaccion'),
            examen_fisico_aspecto=json_analisis.get('examen_fisico_aspecto'),
            examen_fisico_color=json_analisis.get('examen_fisico_color'),
            examen_microscopico_epiteliales=json_analisis.get('examen_microscopico_epiteliales'),
            examen_microscopico_leucocitos=json_analisis.get('examen_microscopico_leucocitos'),
            examen_microscopico_piocitos=json_analisis.get('examen_microscopico_piocitos'),
            examen_microscopico_hematies=json_analisis.get('examen_microscopico_hematies'),
            examen_microscopico_cilindros=json_analisis.get('examen_microscopico_cilindros'),
            examen_microscopico_mucus=json_analisis.get('examen_microscopico_mucus'),
            examen_microscopico_cristales=json_analisis.get('examen_microscopico_cristales'),
            examen_microscopico_germenes=json_analisis.get('examen_microscopico_germenes')
        )
