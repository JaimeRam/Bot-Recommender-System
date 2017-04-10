# coding=utf-8

class User(object):
    
    name = None #Nombre usuarop
    age = 0  #Edad usuario
    sex = None  #Sexo usuario
    preferencias = dict()
    contenidosVisualizados =[]
    
    def __init__(self, name):
        self.name = name # Nombre Usuario
        
    #Función que establece la lista de preferencias incial en función del sexo y la edad
    def initPreferences(self):
        if (self.age < 20) and (self.sex == u'Hombre'):
            self.preferencias = {1045: -0.25, 1050: -0.25, 1055: 0.1, 1060: 0.25, 1065: 0.3}
        elif (self.age < 20) and (self.sex == u'Mujer'):
            self.preferencias = {1045: -0.25, 1050: -0.25, 1055: 0.25, 1060: 0.15, 1065: 0.15}
        elif (self.age >= 20 and self.age < 35) and (self.sex == u'Hombre'):
            self.preferencias = {1045: 0.1, 1050: -0.1, 1055: 0.1, 1060: 0.25, 1065: 0.3}
        elif (self.age >= 20 and self.age < 35) and (self.sex == u'Mujer'):
            self.preferencias = {1045: 0.1, 1050: -0.1, 1055: 0.25, 1060: 0.1, 1065: 0}
        elif (self.age >= 35 and self.age < 50) and (self.sex == u'Hombre'):
            self.preferencias = {1045: 0.5, 1050: 0.3, 1055: 0.3, 1060: 0.1, 1065: 0.3}
        elif (self.age >= 35 and self.age < 50) and (self.sex == u'Mujer'):
            self.preferencias = {1045: 0.5, 1050: 0.3, 1055: 0.4, 1060: 0.15, 1065: 0}
        elif (self.age >= 50) and (self.sex == u'Hombre'):
            self.preferencias = {1045: 0.5, 1050: 0.4, 1055: 0.3, 1060: 0.1, 1065: 0.3}
        elif (self.age >= 50) and (self.sex == u'Mujer'):
            self.preferencias = {1045: 0.5, 1050: 0.25, 1055: 0.6, 1060: 0.1, 1065: 0}
    
    #Función que devuelve el id del topic con máxima preferencia
    def getPreferencesMax(self):
        max = -1
        pref = None
        for k, v in self.preferencias.items():
            if (v >= max):
                max = v
                pref = k
        print(pref)
        return pref
        
    def contenidoVisualizado(self, content):
        for c in self.contenidosVisualizados:
            print(c)
            print(content)
            if (c == content):
                return True
        return False