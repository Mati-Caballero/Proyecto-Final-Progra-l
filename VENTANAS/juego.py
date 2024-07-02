import pygame
from parseo import lista_preguntas
from constantes import *
import random

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

carta_pregunta = {"superficie":pygame.Surface(TAMAÑO_PREGUNTA),"rectangulo":pygame.Rect((0,0,0,0))}
carta_pregunta['superficie'].fill(COLOR_ROJO)

cartas_respuestas = [
    {"superficie":pygame.Surface(TAMAÑO_RESPUESTA),"rectangulo":pygame.Rect((0,0,0,0))},#R1 -> 0
    {"superficie":pygame.Surface(TAMAÑO_RESPUESTA),"rectangulo":pygame.Rect((0,0,0,0))},#R2 -> 1
    {"superficie":pygame.Surface(TAMAÑO_RESPUESTA),"rectangulo":pygame.Rect((0,0,0,0))},#R3 -> 2
]

for carta in cartas_respuestas:
    carta['superficie'].fill(COLOR_AZUL)

#DEFINO TEXTO PREGUNTA
fuente_pregunta = pygame.font.SysFont("Arial Narrow",30)
fuente_respuesta = pygame.font.SysFont("Arial Narrow",20)
fuente_puntuacion = pygame.font.SysFont("Arial Narrow",25)

puntuacion = 0
random.shuffle(lista_preguntas)
indice_pregunta = 0
#pregunta = lista_preguntas[indice_pregunta]

click_sonido = pygame.mixer.Sound('VENTANAS\click.mp3')
click_sonido.set_volume(1)

error_sonido = pygame.mixer.Sound('VENTANAS\error.mp3')
error_sonido.set_volume(1)

# pygame.mixer.music.load("musica.mp3")
# pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0.01)

cantidad_oportunidades = 3


def mostrar_juego(pantalla:pygame.Surface,eventos):
    global indice_pregunta
    global puntuacion 
    global cantidad_oportunidades
    
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
                        carta_pregunta['superficie'].fill((COLOR_ROJO))
                        for carta in cartas_respuestas:
                            carta['superficie'].fill(COLOR_AZUL)
                        
                        indice_pregunta+=1    
                        
                        if indice_pregunta != len(lista_preguntas):
                            pregunta = lista_preguntas[indice_pregunta]
                        else:
                            #TERMINO EL JUEGO
                            indice_pregunta = 0
                            random.shuffle(lista_preguntas)
                            pregunta = lista_preguntas[indice_pregunta]
                        #cartas_respuestas[i]['superficie'].fill(COLOR_VERDE)
                        
                        puntuacion += 100
                    elif pregunta['respuesta_correcta'] != respuesta:
                        print("RESPUESTA INCORRECTA")
                        puntuacion -= 50
                        error_sonido.play()
                        
                        carta_pregunta['superficie'].fill((COLOR_ROJO))
                        for carta in cartas_respuestas:
                            carta['superficie'].fill(COLOR_AZUL)
                        
                        indice_pregunta+=1    
                        
                        cantidad_oportunidades -= 1
                        
                        if indice_pregunta != len(lista_preguntas):
                            pregunta = lista_preguntas[indice_pregunta]
                        else:
                            #TERMINO EL JUEGO
                            indice_pregunta = 0
                            random.shuffle(lista_preguntas)
                            pregunta = lista_preguntas[indice_pregunta]
                        
                        if cantidad_oportunidades == 0:
                            retorno = "terminado"
                        
                        # if puntuacion > 49:
                        
                        #cartas_respuestas[i]['superficie'].fill(COLOR_ROJO)
                    
    pantalla.fill(COLOR_BLANCO)
    #Carta Pregunta
    #Muestro la carta
    pantalla.blit(carta_pregunta['superficie'],(80,50))
    #Muestro el texto (USANDO PANTALLA)
    blit_text(carta_pregunta['superficie'],pregunta['pregunta'],(10,10),fuente_pregunta)
    #blit_text(pantalla,pregunta['pregunta'],(80,50),fuente_pregunta)
    
    #CARTAS RESPUESTAS
    
    #pantalla.blit(cartas_respuestas[0]['superficie'],(125,215))
    
    #IMPRIMO EN PANTALLA LA CARTA R1 Y SU TEXTO
    cartas_respuestas[0]['rectangulo'] = pantalla.blit(cartas_respuestas[0]['superficie'],(125,215))
    blit_text(cartas_respuestas[0]['superficie'],pregunta['respuesta_a'],(10,10),fuente_respuesta,COLOR_BLANCO)

    #IMPRIMO EN PANTALLA LA CARTA R2 Y SU TEXTO
    cartas_respuestas[1]['rectangulo'] = pantalla.blit(cartas_respuestas[1]['superficie'],(125,285))
    blit_text(cartas_respuestas[1]['superficie'],pregunta['respuesta_b'],(10,10),fuente_respuesta,COLOR_BLANCO)

    #IMPRIMO EN PANTALLA LA CARTA R3 Y SU TEXTO
    cartas_respuestas[2]['rectangulo'] = pantalla.blit(cartas_respuestas[2]['superficie'],(125,355))
    blit_text(cartas_respuestas[2]['superficie'],pregunta['respuesta_c'],(10,10),fuente_respuesta,COLOR_BLANCO) 

    #MUESTRO PUNTUACION
    
    blit_text(pantalla,f"Puntuación: {puntuacion} puntos",(10,10),fuente_puntuacion,COLOR_NEGRO)

    #print(cartas_respuestas[0]['rectangulo'])
    # cartas_respuestas[1]['rectangulo']
    # cartas_respuestas[2]['rectangulo']
    # cartas_respuestas[3]['rectangulo']
    
    return retorno
    