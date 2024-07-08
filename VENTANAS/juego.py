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
    {"superficie":pygame.Surface(TAMAÑO_RESPUESTA),"rectangulo":pygame.Rect((0,0,0,0))},#R4 -> 3
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

bandera_vueltas = True
cantidad_preguntas = 0

# clock = pygame.time.Clock()
ultimo_tiempo = pygame.time.get_ticks()

def mostrar_juego(pantalla:pygame.Surface,eventos):
    
    global indice_pregunta
    global puntuacion 
    global cantidad_preguntas
    global bandera_vueltas
    global contador_tiempo
    global ultimo_tiempo
    global fondo_carta_respuesta
    global cantidad_vidas
    
    if bandera_vueltas:
        contador_tiempo = opciones.cantidad_tiempo
        cantidad_vidas = opciones.cantidad_vidas
        bandera_vueltas = False
    
    retorno = "juego"
    pregunta = lista_preguntas[indice_pregunta]
    
    tiempo_actual = pygame.time.get_ticks()
    
    if tiempo_actual - ultimo_tiempo >= 1000:
        opciones.cantidad_tiempo -= 1
        ultimo_tiempo = tiempo_actual
        print(opciones.cantidad_tiempo)
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
                    elif i == 2:
                        respuesta = 'c'
                    else:
                        respuesta = 'd'
                    
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
                        opciones.cantidad_tiempo = contador_tiempo
                        
                    elif pregunta['respuesta_correcta'] != respuesta:
                        print("RESPUESTA INCORRECTA")
                        puntuacion -= opciones.cantidad_puntos_preguntas
                        error_sonido.play()
                        carta_pregunta['superficie'].fill((COLOR_VIOLETA_CLARO))
                        
                        for carta in cartas_respuestas:
                            carta['superficie'].fill(COLOR_VIOLETA_CLARO)
                        indice_pregunta += 1    
                        opciones.cantidad_vidas -= 1
                        
                        if indice_pregunta != len(lista_preguntas):
                            pregunta = lista_preguntas[indice_pregunta]
                        else:
                            #TERMINO EL JUEGO
                            indice_pregunta = 0
                            random.shuffle(lista_preguntas)
                            pregunta = lista_preguntas[indice_pregunta]
                    
                    cantidad_preguntas += 1
                    
                    if opciones.cantidad_vidas == 0:
                        retorno = "terminado"
                        opciones.cantidad_tiempo = contador_tiempo
                        opciones.cantidad_vidas = cantidad_vidas
                        puntuacion = 0
                        bandera_vueltas = True
                        
                    if cantidad_preguntas > len(lista_preguntas):
                        retorno = "terminado"
                        cantidad_preguntas = 0
    
    if opciones.cantidad_tiempo == 0:
        retorno = "terminado"
        opciones.cantidad_tiempo = contador_tiempo
        opciones.cantidad_vidas = cantidad_vidas
        bandera_vueltas = True
    
    pantalla.blit(fondo_juego,(0,0))
    
    #Muestro la carta
    pantalla.blit(carta_pregunta['superficie'],(80,70))
    blit_text(carta_pregunta['superficie'],pregunta['pregunta'],(10,10),fuente_pregunta)
    
    #VIDAS
    match opciones.cantidad_vidas:
        case 5:
            pantalla.blit(imagen_vida_5, (300, 10))
        case 4:
            pantalla.blit(imagen_vida_4, (300, 10))
        case 3:
            pantalla.blit(imagen_vida_3, (300, 10))
        case 2:
            pantalla.blit(imagen_vida_2, (300, 10))
        case 1:
            pantalla.blit(imagen_vida_1, (300, 10))
    
    #CARTAS RESPUESTAS
    
    if opciones.cantidad_respuestas_posibles == 4:
        posiciones = [(240, 250), (320, 330), (400, 410), (480, 490)]
    elif opciones.cantidad_respuestas_posibles == 3:
        posiciones = [(240, 250), (320, 330), (400, 410)]
    elif opciones.cantidad_respuestas_posibles == 2:
        posiciones = [(240, 250), (320, 330), (240, 250), (320, 330)]
    
    respuestas = ['respuesta_a', 'respuesta_b', 'respuesta_c', 'respuesta_d']
    
    if opciones.cantidad_respuestas_posibles == 4:
        for i in range(len(cartas_respuestas)):
            fondo_carta_respuesta = pygame.draw.rect(fondo_juego, COLOR_VIOLETA_OSCURO, (115, posiciones[i][0], 250, 60), 0, 5, 5, 5, 5, 5)
            cartas_respuestas[i]['rectangulo'] = pantalla.blit(cartas_respuestas[i]['superficie'], (125, posiciones[i][1]))
            blit_text(cartas_respuestas[i]['superficie'], pregunta[respuestas[i]], (10, 10), fuente_respuesta, COLOR_BLANCO)
    elif opciones.cantidad_respuestas_posibles == 3:
        if pregunta["respuesta_correcta"] in ["a", "b", "c"]:
            indices = [0, 1, 2]
        else:
            indices = [0, 1, 2]
        for i in indices:
            fondo_carta_respuesta = pygame.draw.rect(fondo_juego, COLOR_VIOLETA_OSCURO, (115, posiciones[i][0], 250, 60), 0, 5, 5, 5, 5, 5)
            cartas_respuestas[i]["rectangulo"] = pantalla.blit(cartas_respuestas[i]["superficie"], ( 125, posiciones[i][1]))
            blit_text(cartas_respuestas[i]["superficie"], pregunta[respuestas[i]], (10, 10), fuente_respuesta, COLOR_BLANCO)
    elif opciones.cantidad_respuestas_posibles == 2:
        if pregunta["respuesta_correcta"] in ["a","b"]:
            indices = [0, 1]
        else:
            indices = [2, 3]
        for i in indices:
            fondo_carta_respuesta = pygame.draw.rect(fondo_juego, COLOR_VIOLETA_OSCURO, (115, posiciones[i][0], 250, 60), 0, 5, 5, 5, 5, 5)
            cartas_respuestas[i]["rectangulo"] = pantalla.blit(cartas_respuestas[i]["superficie"], ( 125, posiciones[i][1]))
            blit_text(cartas_respuestas[i]["superficie"], pregunta[respuestas[i]], (10, 10), fuente_respuesta, COLOR_BLANCO)
    
    #MUESTRO PUNTUACION
    blit_text(pantalla,f"Puntuación: {puntuacion} puntos",(10,10),fuente_puntuacion,COLOR_BLANCO)
    # MUESTRO EL TIEMPO RESTANTE
    blit_text(pantalla, f"Tiempo: {opciones.cantidad_tiempo} s", (353, 25), fuente_tiempo, COLOR_BLANCO)
    
    guardar_puntuacion(puntuacion)
    
    return retorno