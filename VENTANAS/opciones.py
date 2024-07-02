import pygame 
from constantes import *

pygame.init()

fuente_boton = pygame.font.SysFont("Arial Narrow",23)
fuente_volumen =  pygame.font.SysFont("Arial Narrow",50)

boton_suma = {"superficie":pygame.Surface(TAMAÑO_BOTON_SUMA),"rectangulo":pygame.Rect(0,0,0,0)}
boton_suma['superficie'].fill(COLOR_ROJO) # Le asigno un color a esa superficie

boton_resta = {"superficie":pygame.Surface(TAMAÑO_BOTON_SUMA),"rectangulo":pygame.Rect(0,0,0,0)}
boton_resta['superficie'].fill(COLOR_ROJO) # Le asigno un color a esa superficie

boton_volver = {"superficie":pygame.Surface(TAMAÑO_BOTON_VOLVER),"rectangulo":pygame.Rect(0,0,0,0)}
boton_volver['superficie'].fill(COLOR_AZUL) # Le asigno un color a esa superficie

boton_mute = {"superficie":pygame.Surface(TAMAÑO_BOTON_VOLVER),"rectangulo":pygame.Rect(0,0,0,0)}
boton_mute['superficie'].fill(COLOR_AZUL) # Le asigno un color a esa superficie

volumen = 100

click_sonido = pygame.mixer.Sound("VENTANAS\click.mp3")
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

def mostrar_opciones(pantalla:pygame.Surface,eventos):
    global volumen
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
            elif boton_mute['rectangulo'].collidepoint(evento.pos):
                if volumen > 0 and volumen <= 100:
                    volumen = 0
                    click_sonido.play()
                else:
                    volumen = 100
                    click_sonido.play()
        elif evento.type == pygame.QUIT:
            retorno = "salir"

    pantalla.fill(COLOR_BLANCO)

    boton_resta['rectangulo'] = pantalla.blit(boton_resta['superficie'],(20,200))
    boton_suma['rectangulo'] = pantalla.blit(boton_suma['superficie'],(420,200))
    boton_volver['rectangulo'] = pantalla.blit(boton_volver['superficie'],(5,5))
    boton_mute['rectangulo'] = pantalla.blit(boton_mute['superficie'],(280,20))
    
    blit_text(boton_suma['superficie'],"VOL +",(0,10),fuente_boton,COLOR_NEGRO)
    blit_text(boton_resta['superficie'],"VOL -",(0,10),fuente_boton,COLOR_NEGRO)
    blit_text(pantalla,f"{volumen} %",(200,200),fuente_volumen,COLOR_NEGRO)
    blit_text(boton_volver['superficie'],"VOLVER",(10,10),fuente_boton,COLOR_BLANCO)        
    blit_text(boton_mute['superficie'],"MUTE",(0,10),fuente_boton,COLOR_NEGRO)
    
    return retorno
