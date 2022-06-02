from .examen_fisico_densidad import *
from .examen_microscopico_epitelial import *
from .examen_microscopico_leucocitos import *
from .examen_microscopico_hematies import *
from .examen_microscopico_cilindros import *
from .examen_microscopico_mucus import *
from .examen_microscopico_cristales import *
from .examen_microscopico_germenes import *
from .examen_fisico_reaccion import *
from .examen_fisico_aspecto import *
from .bilirrubina_total import *
from .bilirrubina_directa import *
from .bilirrubina_indirecta import *
from .fosfatasa_alcalina_recien_nacido import *
from .fosfatasa_alcalina_bebe import *
from .fosfatasa_alcalina_ninio import *
from .fosfatasa_alcalina_adulto import *
from .glutamico_piruvica_hombre import *
from .glutamico_piruvica_mujer import *
from .glutamico_oxalacetica_hombre import *
from .glutamico_oxalacetica_mujer import *
from .trigliceridos import *
from .colesterol_total import *
from .hdl_hombre import *
from .hdl_mujer import *
from .ldl import *
from .creatinina import *
from .urea import *
from .glucosa import *
from .globulos_rojos_total_mujer import *
from .globulos_rojos_total_hombre import *
from .hematocritos_hombre import *
from .hematocritos_mujer import *
from .hemoglobina_g_hombre import *
from .hemoglobina_g_mujer import *
from .serie_roja_aspecto import *
from .leucocitos import *
from .neutrofilos_cayado import *
from .neutrofilos_segmentado import *
from .eosinofilos import *
from .basofilos import *
from .linfocitos import *
from .monocitos import *


def initialize_routes(api):
    api.add_resource(ExamenFisicoDensidadApi, '/Clidas/api/rutinas/examen-fisico-densidad/<id>')
    api.add_resource(ExamenesFisicosDensidadApi, '/Clidas/api/rutinas/examenes-fisico-densidad')
    #api.add_resource(ExamenesMicroscopicoEpitelialApi, '/Clidas/api/rutinas/examen-microscopico-epitelial')
    #api.add_resource(ExamenMicroscopicoEpitelialApi, '/Clidas/api/rutinas/examen-microscopico-epitelial/<id>')
    api.add_resource(ExamenesMicroscopicosLeucocitosApi, '/Clidas/api/rutinas/examen-microscopico-leucocitos')
    api.add_resource(ExamenMicroscopicoLeucocitosApi, '/Clidas/api/rutinas/examen-microscopico-leucocitos/<id>')
    api.add_resource(ExamenesMicroscopicosHematiesApi, '/Clidas/api/rutinas/examen-microscopico-hematies')
    api.add_resource(ExamenMicroscopicoHematiesApi, '/Clidas/api/rutinas/examen-microscopico-hematies/<id>')
    #api.add_resource(ExamenesMicroscopicoCilindrosApi, '/Clidas/api/rutinas/examen-microscopico-cilindros')
    #api.add_resource(ExamenMicroscopicoCilindrosApi, '/Clidas/api/rutinas/examen-microscopico-cilindros/<id>')
    #api.add_resource(ExamenesMicroscopicoMucusApi, '/Clidas/api/rutinas/examen-microscopico-mucus')
    #api.add_resource(ExamenMicroscopicoMucusApi, '/Clidas/api/rutinas/examen-microscopico-mucus/<id>')
    #api.add_resource(ExamenesMicroscopicoCristalesApi, '/Clidas/api/rutinas/examen-microscopico-cristales')
    #api.add_resource(ExamenMicroscopicoCristalesApi, '/Clidas/api/rutinas/examen-microscopico-cristales/<id>')
    #api.add_resource(ExamenesMicroscopicoGermenesApi, '/Clidas/api/rutinas/examen-microscopico-germenes')
    #api.add_resource(ExamenMicroscopicoGermenesApi, '/Clidas/api/rutinas/examen-microscopico-germenes/<id>')
    api.add_resource(ExamenesFisicosReaccionApi, '/Clidas/api/rutinas/examen-fisico-reaccion')
    api.add_resource(ExamenFisicoReaccionApi, '/Clidas/api/rutinas/examen-fisico-reaccion/<id>')
    #api.add_resource(ExamenesFisicoAspectoApi, '/Clidas/api/rutinas/examen-fisico-aspecto')
    #api.add_resource(ExamenFisicoAspectoApi, '/Clidas/api/rutinas/examen-fisico-aspecto/<id>')
    api.add_resource(BilirrubinaTotalApi, '/Clidas/api/rutinas/bilirrubina-total')
    api.add_resource(BilirrubinasTotalApi, '/Clidas/api/rutinas/bilirrubina-total/<id>')
    api.add_resource(BilirrubinaDirectaApi, '/Clidas/api/rutinas/bilirrubina-directa')
    api.add_resource(BilirrubinasDirectaApi, '/Clidas/api/rutinas/bilirrubina-directa/<id>')
    api.add_resource(BilirrubinaIndirectaApi, '/Clidas/api/rutinas/bilirrubina-indirecta')
    api.add_resource(BilirrubinasIndirectaApi, '/Clidas/api/rutinas/bilirrubina-indirecta/<id>')
    api.add_resource(FosfatasaAlcalinaRecienNacidoApi, '/Clidas/api/rutinas/fosfatasa-alcalina-recien-nacido')
    api.add_resource(FosfatasasAlcalinaRecienNacidoApi, '/Clidas/api/rutinas/fosfatasa-alcalina-recien-nacido/<id>')
    api.add_resource(FosfatasaAlcalinaBebeApi, '/Clidas/api/rutinas/fosfatasa-alcalina-bebe')
    api.add_resource(FosfatasasAlcalinaBebeApi, '/Clidas/api/rutinas/fosfatasa-alcalina-bebe/<id>')
    api.add_resource(FosfatasaAlcalinaNinioApi, '/Clidas/api/rutinas/fosfatasa-alcalina-ninio')
    api.add_resource(FosfatasasAlcalinaNinioApi, '/Clidas/api/rutinas/fosfatasa-alcalina-ninio/<id>')
    api.add_resource(FosfatasaAlcalinaAdultoApi, '/Clidas/api/rutinas/fosfatasa-alcalina-adulto')
    api.add_resource(FosfatasasAlcalinaAdultoApi, '/Clidas/api/rutinas/fosfatasa-alcalina-adulto/<id>')
    api.add_resource(GlutamicoPiruvicaHombreApi, '/Clidas/api/rutinas/glutamico-piruvica-hombre')
    api.add_resource(GlutamicosPiruvicaHombreApi, '/Clidas/api/rutinas/glutamico-piruvica-hombre/<id>')
    api.add_resource(GlutamicoPiruvicaMujerApi, '/Clidas/api/rutinas/glutamico-piruvica-mujer')
    api.add_resource(GlutamicosPiruvicaMujerApi, '/Clidas/api/rutinas/glutamico-piruvica-mujer/<id>')
    api.add_resource(GlutamicosOxalaceticaHombreApi, '/Clidas/api/rutinas/glutamico-oxalacetica-hombre')
    api.add_resource(GlutamicoOxalaceticaHombreApi, '/Clidas/api/rutinas/glutamico-oxalacetica-hombre/<id>')
    api.add_resource(GlutamicosOxalaceticaMujerApi, '/Clidas/api/rutinas/glutamico-oxalacetica-mujer')
    api.add_resource(GlutamicoOxalaceticaMujerApi, '/Clidas/api/rutinas/glutamico-oxalacetica-mujer/<id>')
    api.add_resource(TrigliceridosApi, '/Clidas/api/rutinas/trigliceridos')
    api.add_resource(TrigliceridoApi, '/Clidas/api/rutinas/trigliceridos/<id>')
    api.add_resource(ColesterolesTotalApi, '/Clidas/api/rutinas/colesterol-total')
    api.add_resource(ColesterolTotalApi, '/Clidas/api/rutinas/colesterol-total/<id>')
    api.add_resource(HdlsHombreApi, '/Clidas/api/rutinas/hdl-hombre')
    api.add_resource(HdlHombreApi, '/Clidas/api/rutinas/hdl-hombre/<id>')
    api.add_resource(HdlsMujerApi, '/Clidas/api/rutinas/hdl-mujer')
    api.add_resource(HdlMujerApi, '/Clidas/api/rutinas/hdl-mujer/<id>')
    api.add_resource(LdlsApi, '/Clidas/api/rutinas/ldl')
    api.add_resource(LdlApi, '/Clidas/api/rutinas/ldl/<id>')
    api.add_resource(CreatininasApi, '/Clidas/api/rutinas/creatinina')
    api.add_resource(CreatininaApi, '/Clidas/api/rutinas/creatinina/<id>')
    api.add_resource(UreasApi, '/Clidas/api/rutinas/urea')
    api.add_resource(UreaApi, '/Clidas/api/rutinas/urea/<id>')
    api.add_resource(GlucosasApi, '/Clidas/api/rutinas/glucosa')
    api.add_resource(GlucosaApi, '/Clidas/api/rutinas/glucosa/<id>')
    api.add_resource(GlobulosRojosTotalMujerApi, '/Clidas/api/rutinas/globulos-rojos-total-mujer')
    api.add_resource(GlobuloRojosTotalMujerApi, '/Clidas/api/rutinas/globulos-rojos-total-mujer/<id>')
    api.add_resource(GlobulosRojosTotalHombreApi, '/Clidas/api/rutinas/globulos-rojos-total-hombre')
    api.add_resource(GlobuloRojosTotalHombreApi, '/Clidas/api/rutinas/globulos-rojos-total-hombre/<id>')
    api.add_resource(HematocritosHombreApi, '/Clidas/api/rutinas/hematocritos-hombre')
    api.add_resource(HematocritoHombreApi, '/Clidas/api/rutinas/hematocritos-hombre/<id>')
    api.add_resource(HematocritosMujerApi, '/Clidas/api/rutinas/hematocritos-mujer')
    api.add_resource(HematocritoMujerApi, '/Clidas/api/rutinas/hematocritos-mujer/<id>')
    api.add_resource(HemoglobinasGHombreApi, '/Clidas/api/rutinas/hemoglobina-g-hombre')
    api.add_resource(HemoglobinaGHombreApi, '/Clidas/api/rutinas/hemoglobina-g-hombre/<id>')
    api.add_resource(HemoglobinasGMujerApi, '/Clidas/api/rutinas/hemoglobina-g-mujer')
    api.add_resource(HemoglobinaGMujerApi, '/Clidas/api/rutinas/hemoglobina-g-mujer/<id>')
    #api.add_resource(SerieRojaAspectosApi, '/Clidas/api/rutinas/serie-roja-aspecto')
    #api.add_resource(SerieRojaAspectoApi, '/Clidas/api/rutinas/serie-roja-aspecto/<id>')
    api.add_resource(LeucocitosApi, '/Clidas/api/rutinas/leucocitos')
    api.add_resource(LeucocitoApi, '/Clidas/api/rutinas/leucocitos/<id>')
    api.add_resource(NeutrofilosCayadoApi, '/Clidas/api/rutinas/neutrofilos-cayado')
    api.add_resource(NeutrofiloCayadoApi, '/Clidas/api/rutinas/neutrofilos-cayado/<id>')
    api.add_resource(NeutrofilosSegmentadoApi, '/Clidas/api/rutinas/neutrofilos-segmentado')
    api.add_resource(NeutrofiloSegmentadoApi, '/Clidas/api/rutinas/neutrofilos-segmentado/<id>')
    #api.add_resource(EosinofilosApi, '/Clidas/api/rutinas/eosinofilos')
    #api.add_resource(EosinofiloApi, '/Clidas/api/rutinas/eosinofilos/<id>')
    api.add_resource(BasofilosApi, '/Clidas/api/rutinas/basofilos')
    api.add_resource(BasofiloApi, '/Clidas/api/rutinas/basofilos/<id>')
    api.add_resource(LinfocitosApi, '/Clidas/api/rutinas/linfocitos')
    api.add_resource(LinfocitoApi, '/Clidas/api/rutinas/linfocitos/<id>')
    api.add_resource(MonocitosApi, '/Clidas/api/rutinas/monocitos')
    api.add_resource(MonocitoApi, '/Clidas/api/rutinas/monocitos/<id>')
