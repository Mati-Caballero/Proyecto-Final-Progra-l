import pygame
from generar_csv import lista_preguntas
from constantes import *
import random
from Importar_imagenes import *
import time
from parseo_puntajes import *
import opciones

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



for carta in cartas_respuestas:
    carta['superficie'].fill(COLOR_VIOLETA_CLARO)

#DEFINO TEXTO PREGUNTA
fuente_pregunta = pygame.font.SysFont("Pixel Times",30)
fuente_respuesta = pygame.font.SysFont("Pixel Times",15)
fuente_puntuacion =pygame.font.SysFont("Pixel Times",23)
fuente_tiempo = pygame.font.SysFont("Pixel Times", 20)

puntuacion = 0
random.shuffle(lista_preguntas)
indice_pregunta = 0

click_sonido = pygame.mixer.Sound('VENTANAS\sonidos\click.mp3')
click_sonido.set_volume(1)

error_sonido = pygame.mixer.Sound('VENTANAS\sonidos\error.mp3')
error_sonido.set_volume(1)

# cantidad_oportunidades = opciones.cantidad_vidas
contador_vueltas = 0
cantidad_preguntas = 0

clock = pygame.time.Clock()
ultimo_tiempo = pygame.time.get_ticks()  # Tiempo de inicio para la cuenta regresiva
contador_tiempo = opciones.cantidad_tiempo # Segundos de cuenta regresiva

def mostrar_juego(pantalla:pygame.Surface,eventos):
    
    global indice_pregunta
    global puntuacion 
    global cantidad_oportunidades
    global cantidad_preguntas
    global contador_vueltas
    global contador_tiempo
    global ultimo_tiempo
    global fondo_carta_respuesta
    
    cantidad_oportunidades = opciones.cantidad_vidas
    
    if contador_vueltas > 0:
        cantidad_oportunidades = opciones.cantidad_vidas
        contador_vueltas = 0
    
    retorno = "juego"
    pregunta = lista_preguntas[indice_pregunta]
    
    tiempo_actual = pygame.time.get_ticks()
    
    if tiempo_actual - ultimo_tiempo >= 1000:
        contador_tiempo -= 1
        ultimo_tiempo = tiempo_actual
        print(contador_tiempo)
    pygame.display.update()
    
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
                        
                        puntuacion += opciones.cantidad_puntos_preguntas
                        contador_tiempo = opciones.cantidad_tiempo# Reinicia la cuenta regresiva
                        
                    elif pregunta['respuesta_correcta'] != respuesta:
                        print("RESPUESTA INCORRECTA")
                        puntuacion -= opciones.cantidad_puntos_preguntas
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
                        contador_vueltas += 1
                        contador_tiempo = opciones.cantidad_tiempo
                        puntuacion = 0
                    if cantidad_preguntas > len(lista_preguntas):
                        retorno = "terminado"
                        cantidad_preguntas = 0
    
    if contador_tiempo == 0:
        retorno = "terminado"
        contador_vueltas += 1
        contador_tiempo = opciones.cantidad_tiempo
    
    pantalla.blit(fondo_juego,(0,0))
    
    #Muestro la carta
    pantalla.blit(carta_pregunta['superficie'],(80,70))
    blit_text(carta_pregunta['superficie'],pregunta['pregunta'],(10,10),fuente_pregunta)
    
    #VIDAS
    # if cantidad_oportunidades == 5:
    #     pantalla.blit(imagen_vida_3, (300, 10))
    # elif cantidad_oportunidades == 4:
    #     pantalla.blit(imagen_vida_3, (300, 10))
    if cantidad_oportunidades == 3:
        pantalla.blit(imagen_vida_3, (300, 10))
    elif cantidad_oportunidades == 2:
        pantalla.blit(imagen_vida_2, (300, 10))
    elif cantidad_oportunidades == 1:
        pantalla.blit(imagen_vida_1, (300, 10))
    
    #CARTAS RESPUESTAS
    #IMPRIMO EN PANTALLA LA CARTA R1, R2 y R3 Y SU TEXTO
    fondo_carta_respuesta =pygame.draw.rect(fondo_juego, COLOR_VIOLETA_OSCURO, (115, 240, 250, 60),0 , 5 ,5, 5, 5, 5)
    cartas_respuestas[0]['rectangulo'] = pantalla.blit(cartas_respuestas[0]['superficie'],(125,250))
    blit_text(cartas_respuestas[0]['superficie'],pregunta['respuesta_a'],(10,10),fuente_respuesta,COLOR_BLANCO)
    
    fondo_carta_respuesta =pygame.draw.rect(fondo_juego, COLOR_VIOLETA_OSCURO, (115, 320, 250, 60),0 , 5 ,5, 5, 5, 5)
    cartas_respuestas[1]['rectangulo'] = pantalla.blit(cartas_respuestas[1]['superficie'],(125,330))
    blit_text(cartas_respuestas[1]['superficie'],pregunta['respuesta_b'],(10,10),fuente_respuesta,COLOR_BLANCO)
    
    fondo_carta_respuesta =pygame.draw.rect(fondo_juego, COLOR_VIOLETA_OSCURO, (115, 400, 250, 60),0 , 5 ,5, 5, 5, 5)
    cartas_respuestas[2]['rectangulo'] = pantalla.blit(cartas_respuestas[2]['superficie'],(125,410))
    blit_text(cartas_respuestas[2]['superficie'],pregunta['respuesta_c'],(10,10),fuente_respuesta,COLOR_BLANCO) 

    #MUESTRO PUNTUACION
    blit_text(pantalla,f"Puntuación: {puntuacion} puntos",(10,10),fuente_puntuacion,COLOR_BLANCO)

    # MUESTRO EL TIEMPO RESTANTE
    blit_text(pantalla, f"Tiempo: {contador_tiempo} s", (355, 25), fuente_tiempo, COLOR_NEGRO)

    guardar_puntuacion(puntuacion)
    
    return retorno