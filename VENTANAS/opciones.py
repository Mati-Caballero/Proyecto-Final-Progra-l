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

volumen = 100

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
                if volumen <= 100 and volumen > 0:
                    volumen = 0
                    click_sonido.play()
                else:
                    volumen = 100
                    click_sonido.play()
                
        elif evento.type == pygame.QUIT:
            retorno = "salir"

    pantalla.blit(fondo_opciones,(0, 0))

    boton_resta['rectangulo'] = pantalla.blit(boton_resta['superficie'],(80,150))
    boton_suma['rectangulo'] = pantalla.blit(boton_suma['superficie'],(390,150))
    boton_mute['rectangulo'] = pantalla.blit(boton_mute['superficie'],(405,36))
    boton_volver['rectangulo'] = pantalla.blit(boton_volver['superficie'],(21,40))
    
    if volumen == 100:
        pantalla.blit(imagen_volumen_100,(130,135))
    elif volumen < 100 and volumen > 79:
        pantalla.blit(imagen_volumen_80,(130,135))
    elif volumen < 79 and volumen > 59:
        pantalla.blit(imagen_volumen_60,(130,135))
    elif volumen < 59 and volumen > 39:
        pantalla.blit(imagen_volumen_40,(130,135))
    elif volumen < 39 and volumen > 0:
        pantalla.blit(imagen_volumen_20,(130,135))
    elif volumen == 0:
        pantalla.blit(imagen_mute_off,(390,1))
        pantalla.blit(imagen_volumen_0,(130,135))
    if volumen > 0:
        pantalla.blit(imagen_mute_on,(390, 1))

    blit_text(pantalla,f"{volumen} %",(220,155),fuente_volumen,COLOR_NEGRO)

    pantalla.blit(imagen_suma, (375,130))
    pantalla.blit(imagen_resta, (65,140))
    pantalla.blit(imagen_volver, (10,10))
    
    return retorno