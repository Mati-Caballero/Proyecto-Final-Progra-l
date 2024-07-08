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

volumen = 100
cantidad_puntos_preguntas = 100
cantidad_respuestas_posibles = 4
cantidad_tiempo = 30
cantidad_vidas = 5

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
                if cantidad_respuestas_posibles < 4:
                    cantidad_respuestas_posibles += 1
            elif boton_resta_respuesta['rectangulo'].collidepoint(evento.pos):
                if cantidad_respuestas_posibles > 2:
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
        pantalla.blit(imagen_barra,(130,85))
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
    
    y = 195
    for i in range(4):
        pantalla.blit(imagen_barra,(130,y))
        y += 100
        
    coordenada_x = [375,65]
    coordenada_y = [90,100]
    for i in range(5):
        pantalla.blit(imagen_suma, (coordenada_x[0],coordenada_y[0]))
        pantalla.blit(imagen_resta, (coordenada_x[1],coordenada_y[1]))
        coordenada_y[0] += 100
        coordenada_y[1] += 100
    
    pantalla.blit(imagen_volver, (10,10))
    
    blit_text(pantalla,f"{volumen} %",(215,102),fuente_volumen,COLOR_BLANCO)
    blit_text(pantalla,f"{cantidad_puntos_preguntas}",(225,210),fuente_volumen,COLOR_BLANCO)
    blit_text(pantalla,f"{cantidad_respuestas_posibles}",(240,310),fuente_volumen,COLOR_BLANCO)
    blit_text(pantalla,f"{cantidad_vidas}",(240,410),fuente_volumen,COLOR_BLANCO)
    blit_text(pantalla,f"{cantidad_tiempo}",(230,510),fuente_volumen,COLOR_BLANCO)
    
    blit_text(pantalla,"Volumen", (190,60),fuente_boton,COLOR_BLANCO)
    blit_text(pantalla,"Puntaje por acierto", (145,170),fuente_boton,COLOR_BLANCO)
    blit_text(pantalla,"Cantidad Respuestas", (145,270),fuente_boton,COLOR_BLANCO)
    blit_text(pantalla,"Cantidad de Vidas", (150,370),fuente_boton,COLOR_BLANCO)
    blit_text(pantalla,"Tiempo", (210,470),fuente_boton,COLOR_BLANCO)
    
    return retorno