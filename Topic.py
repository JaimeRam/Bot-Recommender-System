# coding=utf-8

class Topic(object):
    
    def __init__(self, id, nombre, parent_topic):
        self.id = id
        self.nombre = nombre
        self.parent_topic = parent_topic
        
    #Función que define los diferentes temas y subtemas para los tipos de contenido
    @staticmethod
    def definir_topics():
        #Rama Política
        t1 = Topic(1045, 'Política', None)
        t11 = Topic(1046, 'Política Internacional', t1)
        t12 = Topic(1047, 'Política Nacional', t1)
        t13 = Topic(1048, 'Política Social', t1)
        #Rama Economía
        t2 = Topic(1049, 'Economía', None)
        t21 = Topic(1050, 'Finanzas', t2)
        t22 = Topic(1051, 'Mercados', t2)
        t23 = Topic(1052, 'Bolsa', t2)
        #Rama Cultura
        t3 = Topic(1053, 'Cultura', None)
        t31 = Topic(1054, 'Cine', t3)
        t32 = Topic(1055, 'Teatro', t3)
        t33 = Topic(1056, 'Literatura', t3)
        #Rama Tecnología
        t4 = Topic(1057, 'Tecnología', None)
        t41 = Topic(1058, 'Videojuegos', t4)
        t42 = Topic(1059, 'Futuro', t4)
        t43 = Topic(1060, 'Gadgets', t4)
        #Rama Deporte
        t5 = Topic(1061, 'Deporte', None)
        t51 = Topic(1062, 'Fútbol', t5)
        t52 = Topic(1063, 'Baloncesto', t5)
        t53 = Topic(1064, 'Tenis', t5)
        lista = dict()
        lista = {t1: [t11, t12, t13], t2: [t21, t22, t23], t3: [t31, t32, t33], t4: [t41, t42, t43], t5: [t51, t52, t53]}
        return lista