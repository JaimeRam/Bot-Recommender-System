# coding=utf-8

class Content(object):
    
    def __init__(self, id, url, id_topic):
        self.id = id
        self.url = url
        self.id_topic = id_topic
        
    #Función que define los diferentes contenidos que se le ofrecerá al usuario
    @staticmethod
    def definir_contenidos():
        #Rama Política
        c0 = Content(2012, 'http://www.eldiario.es/politica/plantea-elecciones-catalanas-caracter-plebiscitario_0_518998251.html', 1045)
        c1 = Content(2013, 'http://www.elconfidencial.com/mundo/2016-05-23/el-voto-por-correo-decidira-si-la-ultraderecha-se-hace-con-la-presidencia-en-austria_1204439/', 1045)
        c2 = Content(2015, 'http://www.elconfidencial.com/espana/cataluna/2016-05-18/udef-generalitat-telecomunicaciones-desvio-fondos_1201630/', 1045)
        c3 = Content(2014, 'http://www.eldiario.es/sociedad/TVE-produccion-animacion-espanola-independiente_0_507100338.html', 1045)
        #Rama Economía
        c4 = Content(2016, 'http://www.eldiario.es/economia/Rajoy-promete-recortes-Bruselas-gobernar_0_518998139.html', 1050)
        c5 = Content(2017, 'http://www.eldiario.es/economia/Tesla-perdidas-millonarias-produccion-acusaciones_0_517598971.html', 1050)
        c6 = Content(2018, 'http://www.prensa.com/economia/Escasez-Venezuela-produccion-Coca-Cola_0_4487551388.html', 1050)
        c7 = Content(2019, 'http://www.bolsamania.com/noticias/analisis-tecnico/el-ibex-35-preparado-para-atacar-por-enesima-vez-la-resistencia-de-los-8840-puntos--1176303.html', 1050)
        #Rama Cultura
        c8 = Content(2020, 'http://www.eldiario.es/cultura/arte/Los_museos_espanoles_celebran_su_fiesta_internacional_0_516899080.html', 1055)
        c9 = Content(2021, 'http://www.eldiario.es/cultura/Spielberg-infancia-bonachon-Roald-Dahl_0_515848823.html', 1055)
        c10 = Content(2022, 'http://www.eldiario.es/andalucia/Fuente-Ovejuna-Vega-Teatro-Canovas_0_514799463.html', 1055)
        c11 = Content(2023, 'http://www.eldiario.es/cultura/libros/censor-censurado-Camilo-Jose-Cela_0_514449689.html', 1055)
        #Rama Tecnología
        c12 = Content(2024, 'http://www.technologyreview.es/informatica/50196/la-supercomputacion-ya-sufre-los-efectos-del-fin/', 1060)
        c13 = Content(2025, 'http://www.adslzone.net/2016/05/22/uso-bots-juegos-on-line-world-of-warcraft-podria-prohibirse-toda-la-ue/', 1060)
        c14 = Content(2026, 'http://www.revistafeminity.com/espejos-inteligentes-un-reflejo-del-mundo-que-esta-por-llegar/', 1060)
        c15 = Content(2027, 'http://es.gizmodo.com/el-telefono-modular-de-google-sera-por-fin-una-realidad-1777852555', 1060)
        #Rama Deporte
        c16 = Content(2028, 'http://www.publico.es/deportes/luis-enrique-supercopa-ni-lejos.html', 1065)
        c17 = Content(2029, 'http://futbol.as.com/futbol/2016/05/23/primera/1463990919_414949.html', 1065)
        c18 = Content(2030, 'http://baloncesto.as.com/baloncesto/2016/05/23/nba/1463981819_716680.html', 1065)
        c19 = Content(2031, 'http://tenis.as.com/tenis/2016/05/21/mas_tenis/1463844531_861857.html', 1065)
        lista = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19]
        return lista
        
    @staticmethod
    def getContentbyID(lista, id):
        content = None
        for c in lista:
            if (c.id_topic == id):
                content = c
        return content