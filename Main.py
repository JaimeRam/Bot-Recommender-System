# coding=utf-8

import telebot              # Librería telebot para interactuar con la API de Telegram
from telebot import types  
import Topic
import Content
import User
import random
 
TOKEN = 'Your Token' #Identificador único de nuestro bot para Telegram
 
bot = telebot.TeleBot(TOKEN) # Creamos un bot con nuestro Token

lista_topics = Topic.Topic.definir_topics()
lista_contenidos = Content.Content.definir_contenidos()
lista_usuarios = dict()
    
def listener(mensajes): # Definimos un listener a modo debug para visualizar en consola todos los mensajes recibidos por el usuario.
    for m in mensajes: 
        chat_id = m.chat.id
        print(chat_id)
        texto = m.text
        print('ID: ' + str(chat_id) + ' MENSAJE: ' + texto) # Imprimimos el ID de usuario y el mensaje recibido por consola
 
bot.set_update_listener(listener) # Indicamos a la librería que lo que hemos definido antes se encargará de los mensajes

@bot.message_handler(commands=['about']) # Definimos un "handler", que indica al bot que cada vez que reciba el comando
                                             # 'about' tiene que realizar lo que se define abajo
def comando_about(mensaje):
    chat_id = mensaje.chat.id # Almacenamos el ID del mensaje
    bot.send_message(chat_id, 'Este es un bot creado para la asignatura de Interfaces Adaptativos del Máster en IA de la UNED') # Y le mandamos la respuesta
    
#Comando principal de inicio de la aplicación    

@bot.message_handler(commands=['start']) # Definimos un "handler", que indica al bot que cada vez que reciba el comando
                                             # 'start' tiene que realizar lo que se define abajo
                                             
def send_welcome(message):
    msg = bot.reply_to(message, """\
Hola, bienvenido al bot recomendador de contenidos
¿Cómo te llamas?
""")
    bot.register_next_step_handler(msg, process_name_step)

#Función que pregunta por la edad al usuario
def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User.User(name)
        lista_usuarios[chat_id] = user
        print(user.name)
        msg = bot.reply_to(message, '¿Cuántos años tienes ?')
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_age_step(message):
    try:
        chat_id = message.chat.id
        age = message.text
        if not age.isdigit():
            msg = bot.reply_to(message, 'La edad debería de ser un número. ¿Cuántos años tienes?')
            bot.register_next_step_handler(msg, process_age_step)
            return
        user = lista_usuarios[chat_id]
        user.age = int(age)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Hombre', 'Mujer')
        msg = bot.reply_to(message, '¿Cuál es tu sexo?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_sex_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

#Función que registra el sexo del usuario
def process_sex_step(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        user = lista_usuarios[chat_id]
        if (sex == u'Hombre') or (sex == u'Mujer'):
            user.sex = sex
        else:
            raise Exception()
        bot.send_message(chat_id, 'Encantado de conocerte ' + user.name + '\n Edad: ' + str(user.age) + '\n Sexo: ' + user.sex)
        user.initPreferences() #Inicializamos las preferencias por defecto para el envío personalizado de contenidos
        print(user.preferencias)
        print(user.getPreferencesMax())
        bot.send_message(chat_id, 'Tu identificador es el ' + str(chat_id))
        bot.send_message(chat_id, '¿Quieres que te envíe contenidos personalizados?, puedes hacerlo mediante el comando /getcontent')
    except Exception as e:
        bot.reply_to(message, 'oooops')
        
@bot.message_handler(commands=['getcontent']) # Definimos un "handler", que indica al bot que cada vez que reciba el comando
                                             # 'getcontent' tiene que realizar lo que se define abajo
def comando_content(message):
    chat_id = message.chat.id # Almacenamos el ID del mensaje
    user = lista_usuarios[chat_id] #Obtenemos el usuario que utiliza la aplicación
    content = Content.Content.getContentbyID(lista_contenidos, user.getPreferencesMax())
    
    if (user.contenidoVisualizado(content.id_topic)):
        content = None
        while (content is None):
            aleatorio = random.uniform(-0.25, 1) #Generamos un número aleatorio entre -0.25 y 1
            content = random.choice(lista_contenidos)
            if (user.preferencias[content.id_topic] >= aleatorio) and (not (user.contenidoVisualizado(content.id_topic))):
                bot.send_message(chat_id, content.url)
            else:
                content = None
    else:
        bot.send_message(chat_id, content.url)
    #Añadimos el contenido a la lista de contenidos visualizados por el usuario
    user.contenidosVisualizados.append(content.id_topic)
        
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Bueno', 'Malo')
    msg = bot.reply_to(message, "Cómo valorarías el contenido sugerido?", reply_markup=markup)
    bot.register_next_step_handler
    
def process_value_step(message):
    try:
        chat_id = message.chat.id
        response = message.text
        user = lista_usuarios[chat_id]
        value = 0
        if (response == u'Bueno'):
            value = 0.1
        elif (response == u'Malo'):
            value = -0.1
        else:
            raise Exception()
        id_content = user.contenidosVisualizados[-1] #Obtenemos el último elemento de la lista, que coincide con el último visualizado
        print(user.preferencias)
        user.preferencias[id_content] = user.preferencias[id_content] + value
        print(user.preferencias)
    except Exception as e:
        bot.reply_to(message, 'oooops')
    
bot.polling(none_stop=True) # Iniciamos nuestro bot para que esté atento a los mensajes