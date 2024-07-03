import pygame
from parseo import lista_preguntas
from constantes import *
import random
from Importar_imagenes import *
import json

def blit_text(surface, text, pos, font, color=pygame.Color('black')): 
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

pygame.init()#Inicializa el proyecto

carta_pregunta = {"superficie":pygame.Surface(TAMAÑO_PREGUNTA), "rectangulo":pygame.Rect((0,0,0,0))}
carta_pregunta['superficie'].fill(COLOR_VIOLETA_CLARO)

fondo_carta_pregunta = pygame.draw.rect(fondo_juego, COLOR_VIOLETA_OSCURO, (70, 60, 350, 160),0 , 5 ,5, 5, 5, 5)

cartas_respuestas = [
    {"superficie":pygame.Surface(TAMAÑO_RESPUESTA),"rectangulo":pygame.Rect((0,0,0,0))},#R1 -> 0
    {"superficie":pygame.Surface(TAMAÑO_RESPUESTA),"rectangulo":pygame.Rect((0,0,0,0))},#R2 -> 1
    {"superficie":pygame.Surface(TAMAÑO_RESPUESTA),"rectangulo":pygame.Rect((0,0,0,0))},#R3 -> 2
]

fondo_carta_respuesta =pygame.draw.rect(fondo_juego, COLOR_VIOLETA_OSCURO, (115, 240, 250, 60),0 , 5 ,5, 5, 5, 5)
fondo_carta_respuesta =pygame.draw.rect(fondo_juego, COLOR_VIOLETA_OSCURO, (115, 320, 250, 60),0 , 5 ,5, 5, 5, 5)
fondo_carta_respuesta =pygame.draw.rect(fondo_juego, COLOR_VIOLETA_OSCURO, (115, 400, 250, 60),0 , 5 ,5, 5, 5, 5)

for carta in cartas_respuestas:
    carta['superficie'].fill(COLOR_VIOLETA_CLARO)

#DEFINO TEXTO PREGUNTA
fuente_pregunta = pygame.font.SysFont("Pixel Times",30)
fuente_respuesta = pygame.font.SysFont("Pixel Times",25)
fuente_puntuacion =pygame.font.SysFont("Pixel Times",23)

puntuacion = 0
random.shuffle(lista_preguntas)
indice_pregunta = 0

click_sonido = pygame.mixer.Sound('VENTANAS\sonidos\click.mp3')
click_sonido.set_volume(1)

error_sonido = pygame.mixer.Sound('VENTANAS\sonidos\error.mp3')
error_sonido.set_volume(1)

def guardar_puntuacion(puntuacion):#CREO UN JSON DONDE SE GUARDEN LAS PUNTUACIONES DE CADA JUGADOR
    puntuacion = str(puntuacion) #EN DATO STR
    with open("puntuacion.json", "w") as archivo:
        json.dump({"puntuacion": puntuacion}, archivo)

def cargar_puntuacion():
    with open("puntuacion.json", "r") as archivo: #PARSEO Y CARGO EL JSON CON LOS PUNTAJES
        datos = json.load(archivo) #CARGO EL ARCHIVO 
        return datos.get("puntuacion", 0) #LLAMO LA PUNTUACION POR DEFECTO SI NO HAY NINGUNA PARTICDA JUGADAS LE DOY UNA PUNTUACION DE 0

cantidad_oportunidades = 3
cantidad_preguntas = 0

def mostrar_juego(pantalla:pygame.Surface,eventos):
    global indice_pregunta
    global puntuacion 
    global cantidad_oportunidades
    global cantidad_preguntas
    
    retorno = "juego"
    pregunta = lista_preguntas[indice_pregunta]
    for evento in eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(cartas_respuestas)):
                if cartas_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                    if i == 0:
                        respuesta = 'a'
                    elif i == 1:
                        respuesta = 'b'
                    else:
                        respuesta = 'c'
                    if pregunta['respuesta_correcta'] == respuesta:
                        click_sonido.play()
                        print("RESPUESTA CORRECTA")                 
                        carta_pregunta['superficie'].fill((COLOR_VIOLETA_CLARO))
                        for carta in cartas_respuestas:
                            carta['superficie'].fill(COLOR_VIOLETA_CLARO)
                        
                        indice_pregunta += 1    
                        
                        if indice_pregunta != len(lista_preguntas):
                            pregunta = lista_preguntas[indice_pregunta]
                        else:
                            #TERMINO EL JUEGO
                            indice_pregunta = 0
                            random.shuffle(lista_preguntas)
                            pregunta = lista_preguntas[indice_pregunta]
                        
                        puntuacion += 100
                    elif pregunta['respuesta_correcta'] != respuesta:
                        print("RESPUESTA INCORRECTA")
                        puntuacion -= 50
                        error_sonido.play()
                        
                        carta_pregunta['superficie'].fill((COLOR_VIOLETA_CLARO))
                        for carta in cartas_respuestas:
                            carta['superficie'].fill(COLOR_VIOLETA_CLARO)
                        
                        indice_pregunta += 1    
                        cantidad_oportunidades -= 1
                        
                        if indice_pregunta != len(lista_preguntas):
                            pregunta = lista_preguntas[indice_pregunta]
                        else:
                            #TERMINO EL JUEGO
                            indice_pregunta = 0
                            random.shuffle(lista_preguntas)
                            pregunta = lista_preguntas[indice_pregunta]
                        
                    cantidad_preguntas += 1
                        
                    if cantidad_oportunidades == 0:
                        retorno = "terminado"
                    if cantidad_preguntas > len(lista_preguntas):
                        retorno = "terminado"
                        
    pantalla.blit(fondo_juego,(0,0))

    #Carta Pregunta
    #Muestro la carta
    pantalla.blit(carta_pregunta['superficie'],(80,70))
    #Muestro el texto (USANDO PANTALLA)
    blit_text(carta_pregunta['superficie'],pregunta['pregunta'],(10,10),fuente_pregunta)

    #VIDAS
    if cantidad_oportunidades == 3:
        pantalla.blit(imagen_vida_3, (300, 10))
    elif cantidad_oportunidades == 2:
        pantalla.blit(imagen_vida_2, (300, 10))
    elif cantidad_oportunidades == 1:
        pantalla.blit(imagen_vida_1, (300, 10))
    
    #CARTAS RESPUESTAS
    #IMPRIMO EN PANTALLA LA CARTA R1 Y SU TEXTO
    cartas_respuestas[0]['rectangulo'] = pantalla.blit(cartas_respuestas[0]['superficie'],(125,250))
    blit_text(cartas_respuestas[0]['superficie'],pregunta['respuesta_a'],(10,10),fuente_respuesta,COLOR_BLANCO)

    #IMPRIMO EN PANTALLA LA CARTA R2 Y SU TEXTO
    cartas_respuestas[1]['rectangulo'] = pantalla.blit(cartas_respuestas[1]['superficie'],(125,330))
    blit_text(cartas_respuestas[1]['superficie'],pregunta['respuesta_b'],(10,10),fuente_respuesta,COLOR_BLANCO)

    #IMPRIMO EN PANTALLA LA CARTA R3 Y SU TEXTO
    cartas_respuestas[2]['rectangulo'] = pantalla.blit(cartas_respuestas[2]['superficie'],(125,410))
    blit_text(cartas_respuestas[2]['superficie'],pregunta['respuesta_c'],(10,10),fuente_respuesta,COLOR_BLANCO) 

    #MUESTRO PUNTUACION
    blit_text(pantalla,f"Puntuación: {puntuacion} puntos",(10,10),fuente_puntuacion,COLOR_NEGRO)

    guardar_puntuacion(puntuacion)
    
    return retorno
