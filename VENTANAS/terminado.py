import pygame 
from constantes import *
from Importar_imagenes import fondo_terminado, imagen_game_over, imagen_you_win
import datetime
from juego import*
from parseo_puntajes import *

pygame.init()

fuente =  pygame.font.SysFont("Pixel Times",35)
cuadro = {"superficie":pygame.Surface(CUADRO_TEXTO),"rectangulo":pygame.Rect(0,0,0,0)}
cuadro['superficie'].fill(COLOR_VIOLETA_CLARO) # Le asigno un color a esa superficie
fondo_cuadro = pygame.draw.rect(fondo_terminado, COLOR_VIOLETA_OSCURO, (90, 290, 300, 50),0 , 5 ,5, 5, 5, 5)

nombre = ""

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

def mostrar_juego_terminado(pantalla:pygame.Surface,eventos,puntaje):
    global nombre
    retorno = "terminado"

    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pass
        if evento.type == pygame.KEYDOWN:
            bloc_mayus = pygame.key.get_mods() and pygame.KMOD_CAPS
            letra_presionada = pygame.key.name(evento.key)

            if letra_presionada == 'backspace' and len(nombre) > 0:
                nombre = nombre[:-1]#Elimino el último
                cuadro['superficie'].fill(COLOR_VIOLETA_CLARO)# limpio la superficie de su texto anterior

            if letra_presionada == 'space':
                nombre += " "
            
            if len(letra_presionada) == 1 and letra_presionada.isalpha(): 
                if bloc_mayus:
                    nombre += letra_presionada.upper()
                else:
                    nombre += letra_presionada
                    
            if letra_presionada == 'return' and len(nombre) > 0:
                retorno = "salir"
                fecha = datetime.datetime.now()
                puntuacion = cargar_puntuacion()
                partidas_json(nombre, fecha, puntuacion)
                
        elif evento.type == pygame.QUIT:
            retorno = "salir"
            
        # pantalla.fill(COLOR_BLANCO)
        pantalla.blit(fondo_terminado, (0, 0))
        
        if puntaje < 1000:
            pantalla.blit(imagen_game_over, (150, 50))
        elif puntaje > 999:
            pantalla.blit(imagen_you_win, (150, 50))
        
        cuadro['rectangulo'] = pantalla.blit(cuadro['superficie'],(100,300))

        blit_text(cuadro['superficie'],nombre,(10,10),fuente,COLOR_BLANCO)
        blit_text(pantalla,f"Usted obtuvo: {puntaje} puntos",(30,250),fuente,COLOR_NEGRO)

    return retorno