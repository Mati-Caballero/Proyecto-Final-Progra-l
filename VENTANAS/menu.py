import pygame
from constantes import *

pygame.init()

fuente_menu = pygame.font.SysFont("Arial Narrow",30)

#Fondos escenas
fondo_menu = pygame.image.load("VENTANAS\imagenes\Fondos\Fondo_main.png")
fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO, ALTO))

fondo_opciones = pygame.image.load("VENTANAS\imagenes\Fondos\Fondo_opciones.png")
fondo_opciones = pygame.transform.scale(fondo_opciones, (ANCHO, ALTO))

#Botones
boton_jugar = {"superficie":pygame.Surface(TAMAÑO_BOTON),"rectangulo":pygame.Rect(0,0,0,0)}
boton_salir = {"superficie":pygame.Surface(TAMAÑO_BOTON),"rectangulo":pygame.Rect(0,0,0,0)}
boton_opciones = {"superficie":pygame.Surface(TAMAÑO_BOTON),"rectangulo":pygame.Rect(0,0,0,0)}
boton_puntuaciones = {"superficie":pygame.Surface(TAMAÑO_BOTON),"rectangulo":pygame.Rect(0,0,0,0)}

#Imagenes botones
imagen_play = pygame.image.load("VENTANAS\imagenes\Botones\Play.png")
imagen_play = pygame.transform.scale(imagen_play, (200, 100))

imagen_menu = pygame.image.load("VENTANAS\imagenes\Botones\Menu.png")
imagen_menu = pygame.transform.scale(imagen_menu, (200, 100))

imagen_back = pygame.image.load("VENTANAS\imagenes\Botones\Back.png")
imagen_back = pygame.transform.scale(imagen_back, (200, 100))

imagen_score = pygame.image.load("VENTANAS\imagenes\Botones\Score.png")
imagen_score = pygame.transform.scale(imagen_score, (200, 100))

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
            retorno = "salir" #El estado salir -> Cuando se le da a la X

    boton_jugar["rectangulo"] = pantalla.blit(boton_jugar["superficie"],(160,60))
    boton_opciones["rectangulo"] = pantalla.blit(boton_opciones["superficie"],(160,160))
    boton_puntuaciones["rectangulo"] = pantalla.blit(boton_puntuaciones["superficie"],(160,260))
    boton_salir["rectangulo"] = pantalla.blit(boton_salir["superficie"],(160,365))
    
    fondo_menu.blit(imagen_play, (150,45))
    fondo_menu.blit(imagen_menu, (150,150))
    fondo_menu.blit(imagen_score, (150,255))
    fondo_menu.blit(imagen_back, (150,355))
    
    return retorno #Retorna el estado al que va a ir principal