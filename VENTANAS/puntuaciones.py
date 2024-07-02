import pygame 
from constantes import *

pygame.init()

fuente = pygame.font.SysFont("Arial Narrow",32)
fuente_boton = pygame.font.SysFont("Arial Narrow",23)

boton_volver = {"superficie":pygame.Surface(TAMAÑO_BOTON_VOLVER),"rectangulo":pygame.Rect(0,0,0,0)}
boton_volver['superficie'].fill(COLOR_AZUL) # Le asigno un color a esa superficie

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

    retorno = "puntuaciones"
    
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver['rectangulo'].collidepoint(evento.pos):
                click_sonido.play()
                retorno = "menu"
        elif evento.type == pygame.QUIT:
            retorno = "salir"
            
    pantalla.fill(COLOR_BLANCO)

    boton_volver['rectangulo'] = pantalla.blit(boton_volver['superficie'],(5,5))
    
    blit_text(boton_volver['superficie'],"VOLVER",(10,10),fuente_boton,COLOR_BLANCO)        
    blit_text(pantalla,f"ACA SE DEBE MOSTRAR EL TOP 10",(20,200),fuente,COLOR_NEGRO) 
    
    return retorno
