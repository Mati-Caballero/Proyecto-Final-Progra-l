import pygame 
from constantes import *
from menu import *
from Importar_imagenes import *

pygame.init()

fuente_boton = pygame.font.SysFont("Pixel Times",23)
fuente_volumen =  pygame.font.SysFont("Pixel Times",30)

boton_suma = {"superficie":pygame.Surface(TAMAÑO_BOTON_SUMA),"rectangulo":pygame.Rect(0,0,0,0)}
boton_resta = {"superficie":pygame.Surface(TAMAÑO_BOTON_SUMA),"rectangulo":pygame.Rect(0,0,0,0)}
boton_volver = {"superficie":pygame.Surface(TAMAÑO_BOTON_VOLVER),"rectangulo":pygame.Rect(0,0,0,0)}
boton_mute = {"superficie":pygame.Surface(TAMAÑO_BOTON_MUTE),"rectangulo":pygame.Rect(0,0,0,0)}
boton_suma_puntaje = {"superficie":pygame.Surface(TAMAÑO_BOTON_SUMA),"rectangulo":pygame.Rect(0,0,0,0)}
boton_resta_puntaje = {"superficie":pygame.Surface(TAMAÑO_BOTON_SUMA),"rectangulo":pygame.Rect(0,0,0,0)}
boton_suma_respuesta = {"superficie":pygame.Surface(TAMAÑO_BOTON_SUMA),"rectangulo":pygame.Rect(0,0,0,0)}
boton_resta_respuesta = {"superficie":pygame.Surface(TAMAÑO_BOTON_SUMA),"rectangulo":pygame.Rect(0,0,0,0)}
boton_suma_vidas = {"superficie":pygame.Surface(TAMAÑO_BOTON_SUMA),"rectangulo":pygame.Rect(0,0,0,0)}
boton_resta_vidas = {"superficie":pygame.Surface(TAMAÑO_BOTON_SUMA),"rectangulo":pygame.Rect(0,0,0,0)}
boton_suma_tiempo = {"superficie":pygame.Surface(TAMAÑO_BOTON_SUMA),"rectangulo":pygame.Rect(0,0,0,0)}
boton_resta_tiempo = {"superficie":pygame.Surface(TAMAÑO_BOTON_SUMA),"rectangulo":pygame.Rect(0,0,0,0)}


click_sonido = pygame.mixer.Sound("VENTANAS\sonidos\click.mp3")
click_sonido.set_volume(1)

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

def modificar_opcion(cant_opcion, cant_max, cant_min, cant_dif ):
    if cant_opcion < cant_max:
        cant_opcion += cant_dif
    if cant_opcion > cant_min:
        cant_opcion -= cant_dif
    return cant_opcion
                # elif boton_suma_puntaje['rectangulo'].collidepoint(evento.pos):
                #             if cantidad_puntos_preguntas < 351:
                #                 cantidad_puntos_preguntas += 50
                # elif boton_resta_puntaje['rectangulo'].collidepoint(evento.pos):
                #             if cantidad_puntos_preguntas > 51:
                #                 cantidad_puntos_preguntas -= 50

volumen = 100
cantidad_puntos_preguntas = 100
cantidad_respuestas_posibles = 3
cantidad_vidas = 3
cantidad_tiempo = 10
    
def mostrar_opciones(pantalla:pygame.Surface,eventos):
    global volumen
    global cantidad_puntos_preguntas
    global cantidad_respuestas_posibles
    global cantidad_vidas
    global cantidad_tiempo
    
    
    retorno = "opciones"
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_suma['rectangulo'].collidepoint(evento.pos):
                if volumen < 96: 
                    volumen += 5
                    click_sonido.play()
            elif boton_resta['rectangulo'].collidepoint(evento.pos):
                if volumen > 0: 
                    volumen -= 5
                    click_sonido.play()
            elif boton_volver['rectangulo'].collidepoint(evento.pos):
                retorno = "menu"
                click_sonido.play()
                print(cantidad_puntos_preguntas)
            elif boton_mute['rectangulo'].collidepoint(evento.pos):
                if volumen <= 100 and volumen > 0:
                    volumen = 0
                    click_sonido.play()
                else:
                    volumen = 100
                    click_sonido.play()
            
            elif boton_suma_puntaje['rectangulo'].collidepoint(evento.pos):
                if cantidad_puntos_preguntas < 351:
                    cantidad_puntos_preguntas += 50
            elif boton_resta_puntaje['rectangulo'].collidepoint(evento.pos):
                if cantidad_puntos_preguntas > 51:
                    cantidad_puntos_preguntas -= 50
            elif boton_suma_respuesta['rectangulo'].collidepoint(evento.pos):
                if cantidad_respuestas_posibles < 3:
                    cantidad_respuestas_posibles += 1
            elif boton_resta_respuesta['rectangulo'].collidepoint(evento.pos):
                if cantidad_respuestas_posibles > 1:
                    cantidad_respuestas_posibles -= 1
            elif boton_suma_vidas['rectangulo'].collidepoint(evento.pos):
                if cantidad_vidas < 5:
                    cantidad_vidas += 1
            elif boton_resta_vidas["rectangulo"].collidepoint(evento.pos):
                if cantidad_vidas > 1:
                    cantidad_vidas -= 1
            elif boton_suma_tiempo['rectangulo'].collidepoint(evento.pos):
                if cantidad_tiempo < 30:
                    cantidad_tiempo += 5
            elif boton_resta_tiempo['rectangulo'].collidepoint(evento.pos):
                if cantidad_tiempo > 5:
                    cantidad_tiempo -= 5
        elif evento.type == pygame.QUIT:
            retorno = "salir"
    
    pantalla.blit(fondo_opciones,(0, 0))
    
    boton_volver['rectangulo'] = pantalla.blit(boton_volver['superficie'],(21,40))
    boton_mute['rectangulo'] = pantalla.blit(boton_mute['superficie'],(405,36))
    boton_resta['rectangulo'] = pantalla.blit(boton_resta['superficie'],(80,110))
    boton_suma['rectangulo'] = pantalla.blit(boton_suma['superficie'],(390,110))
    boton_resta_puntaje['rectangulo'] = pantalla.blit(boton_resta_puntaje['superficie'],(80,210))
    boton_suma_puntaje['rectangulo'] = pantalla.blit(boton_suma_puntaje['superficie'],(390,210))
    boton_resta_respuesta['rectangulo'] = pantalla.blit(boton_resta_respuesta['superficie'],(80,310))
    boton_suma_respuesta['rectangulo'] = pantalla.blit(boton_suma_respuesta['superficie'],(390,310))
    boton_resta_vidas['rectangulo'] = pantalla.blit(boton_resta_vidas['superficie'],(80,410))
    boton_suma_vidas['rectangulo'] = pantalla.blit(boton_suma_vidas['superficie'],(390,410))
    boton_resta_tiempo['rectangulo'] = pantalla.blit(boton_resta_tiempo['superficie'],(80,510))
    boton_suma_tiempo['rectangulo'] = pantalla.blit(boton_suma_tiempo['superficie'],(390,510))
    
    if volumen == 100:
        pantalla.blit(imagen_volumen_100,(130,85))
    elif volumen < 100 and volumen > 79:
        pantalla.blit(imagen_volumen_80,(130,85))
    elif volumen < 79 and volumen > 59:
        pantalla.blit(imagen_volumen_60,(130,85))
    elif volumen < 59 and volumen > 39:
        pantalla.blit(imagen_volumen_40,(130,85))
    elif volumen < 39 and volumen > 0:
        pantalla.blit(imagen_volumen_20,(130,85))
    elif volumen == 0:
        pantalla.blit(imagen_mute_off,(390,1))
        pantalla.blit(imagen_volumen_0,(130,85))
    if volumen > 0:
        pantalla.blit(imagen_mute_on,(390, 1))
    
    pantalla.blit(imagen_volumen_100,(130,195))
    pantalla.blit(imagen_volumen_100,(130,295))
    pantalla.blit(imagen_volumen_100,(130,295))
    pantalla.blit(imagen_volumen_100,(130,395))
    pantalla.blit(imagen_volumen_100,(130,495))
    
    pantalla.blit(imagen_suma, (375,90))
    pantalla.blit(imagen_resta, (65,100))
    pantalla.blit(imagen_suma, (375,190))
    pantalla.blit(imagen_resta, (65,200))
    pantalla.blit(imagen_suma, (375,290))
    pantalla.blit(imagen_resta, (65,300))
    pantalla.blit(imagen_suma, (375,390))
    pantalla.blit(imagen_resta, (65,400))
    pantalla.blit(imagen_suma, (375,490))
    pantalla.blit(imagen_resta, (65,500))
    
    pantalla.blit(imagen_volver, (10,10))
    
    blit_text(pantalla,f"{volumen} %",(215,105),fuente_volumen,COLOR_BLANCO)
    blit_text(pantalla,f"{cantidad_puntos_preguntas}",(220,210),fuente_volumen,COLOR_BLANCO)
    blit_text(pantalla,f"{cantidad_respuestas_posibles}",(220,310),fuente_volumen,COLOR_BLANCO)
    blit_text(pantalla,f"{cantidad_vidas}",(220,410),fuente_volumen,COLOR_BLANCO)
    blit_text(pantalla,f"{cantidad_tiempo}",(220,510),fuente_volumen,COLOR_BLANCO)
    
    blit_text(pantalla,"Volumen", (190,60),fuente_boton,COLOR_BLANCO)
    blit_text(pantalla,"Puntaje por acierto", (145,170),fuente_boton,COLOR_BLANCO)
    blit_text(pantalla,"Cantidad Preguntas", (145,270),fuente_boton,COLOR_BLANCO)
    blit_text(pantalla,"Cantidad de Vidas", (150,370),fuente_boton,COLOR_BLANCO)
    blit_text(pantalla,"Tiempo", (210,470),fuente_boton,COLOR_BLANCO)
    
    return retorno