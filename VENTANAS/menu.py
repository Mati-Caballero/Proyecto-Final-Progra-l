import pygame
from constantes import *
from Importar_imagenes import*

pygame.init()

fuente_menu = pygame.font.SysFont("Pixel Times",30)

#Botones
boton_jugar = {"superficie":pygame.Surface(TAMAÑO_BOTON),"rectangulo":pygame.Rect(0,0,0,0)}
boton_salir = {"superficie":pygame.Surface(TAMAÑO_BOTON),"rectangulo":pygame.Rect(0,0,0,0)}
boton_opciones = {"superficie":pygame.Surface(TAMAÑO_BOTON),"rectangulo":pygame.Rect(0,0,0,0)}
boton_puntuaciones = {"superficie":pygame.Surface(TAMAÑO_BOTON),"rectangulo":pygame.Rect(0,0,0,0)}

#Sonido click
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

def mostrar_menu(pantalla:pygame.Surface,eventos):
    retorno = "menu"#Un estado de la ventana en la que estoy parado
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_jugar["rectangulo"].collidepoint(evento.pos):
                print("JUGAR")
                click_sonido.play()
                retorno = "juego"
            elif boton_opciones["rectangulo"].collidepoint(evento.pos):
                print("OPCIONES")
                click_sonido.play()
                retorno = "opciones"
            elif boton_puntuaciones["rectangulo"].collidepoint(evento.pos):
                print("PUNTUACIONES")
                click_sonido.play()
                retorno = "puntuaciones"
            elif boton_salir["rectangulo"].collidepoint(evento.pos):
                click_sonido.play()
                print("SALIR")
                retorno = "salir"
        elif evento.type == pygame.QUIT:
            retorno = "salir"
    
    boton_jugar["rectangulo"] = pantalla.blit(boton_jugar["superficie"],(160,110))
    boton_opciones["rectangulo"] = pantalla.blit(boton_opciones["superficie"],(160,210))
    boton_puntuaciones["rectangulo"] = pantalla.blit(boton_puntuaciones["superficie"],(160,310))
    boton_salir["rectangulo"] = pantalla.blit(boton_salir["superficie"],(160,415))
    
    fondo_menu.blit(imagen_play, (150,95))
    fondo_menu.blit(imagen_menu, (150,200))
    fondo_menu.blit(imagen_score, (150,305))
    fondo_menu.blit(imagen_back, (150,405))
    
    return retorno