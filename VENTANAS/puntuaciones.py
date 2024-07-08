import pygame 
from constantes import *
from Importar_imagenes import *
from parseo_puntajes import top_mejores_diez

pygame.init()

fuente = pygame.font.SysFont("Pixel Times",22)
fuente_boton = pygame.font.SysFont("Pixel Times",23)

boton_volver = {"superficie":pygame.Surface(TAMAÑO_BOTON_VOLVER),"rectangulo":pygame.Rect(0,0,0,0)}
# boton_volver['superficie'].fill(COLOR_AZUL) # Le asigno un color a esa superficie

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

def mostrar_puntuaciones(pantalla:pygame.Surface,eventos):
    global volumen
    global fondo_puntajes
    retorno = "puntuaciones"
    
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver['rectangulo'].collidepoint(evento.pos):
                click_sonido.play()
                retorno = "menu"
        elif evento.type == pygame.QUIT:
            retorno = "salir"
            
    pantalla.blit(fondo_puntuaciones, (0,0))

    boton_volver['rectangulo'] = pantalla.blit(boton_volver['superficie'],(21,40))
    pantalla.blit(imagen_volver, (10, 10))
    
    nombre_top = " "
    fecha_top = " "
    puntaje_top =" "
    mejores_diez = top_mejores_diez()
    
    for i in mejores_diez: #RECORRO LOS MEJORES JUGADORES Y LE ASIGNO LOS VALORES A CADA UNO
        nombre = i["nombre"]
        fecha = i["fecha"]
        puntaje = i["puntuacion"]
        nombre_top += f'{nombre}\n'
        fecha_top += f'{fecha}\n'
        puntaje_top += f'{puntaje}\n'

    fondo_puntajes = pygame.draw.rect(pantalla, COLOR_ROSA, (5, 120, 130, 300), 0, 5, 5, 5, 5, 5)
    fondo_puntajes = pygame.draw.rect(pantalla, COLOR_ROSA, (170, 120, 180, 300), 0, 5, 5, 5, 5, 5)
    fondo_puntajes = pygame.draw.rect(pantalla, COLOR_ROSA, (375, 120, 120, 300), 0, 5, 5, 5, 5, 5)

    blit_text(boton_volver['superficie'],"VOLVER",(10,10),fuente_boton,COLOR_BLANCO)
    blit_text(pantalla,f' NOMBRE\n{nombre_top}',(10,150),fuente,COLOR_BLANCO)
    blit_text(pantalla, f'FECHA\n{fecha_top}', (200, 150),fuente,COLOR_BLANCO) 
    blit_text(pantalla, f'PUNTOS\n{puntaje_top}', (390, 150),fuente,COLOR_BLANCO)         
    
    return retorno
