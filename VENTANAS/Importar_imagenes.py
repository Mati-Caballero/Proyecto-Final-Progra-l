import pygame
import pygame.image
from constantes import *
#FONDOS ESCENAS
fondo_menu = pygame.image.load("VENTANAS\imagenes\Fondos\Fondo_main.png")
fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO, ALTO))

fondo_opciones = pygame.image.load("VENTANAS\imagenes\Fondos\Fondo_opciones.png")
fondo_opciones = pygame.transform.scale(fondo_opciones, (ANCHO, ALTO))

fondo_juego = pygame.image.load("VENTANAS\imagenes\Fondos\Fondo_juego.png")
fondo_juego = pygame.transform.scale(fondo_juego, (ANCHO, ALTO))

fondo_terminado = pygame.image.load("VENTANAS\imagenes\Fondos\Fondo_terminado.png")
fondo_terminado = pygame.transform.scale(fondo_terminado, (ANCHO, ALTO))

fondo_puntuaciones = pygame.image.load("VENTANAS\imagenes\Fondos\Fondo_puntuaciones.png")
fondo_puntuaciones = pygame.transform.scale(fondo_puntuaciones, (ANCHO, ALTO))

#GAME OVER
imagen_game_over = pygame.image.load("VENTANAS\imagenes\Game Over\Game_over.png")
imagen_game_over = pygame.transform.scale(imagen_game_over, (200,200))

imagen_you_win = pygame.image.load("VENTANAS\imagenes\Game Over\You_win.png")
imagen_you_win = pygame.transform.scale(imagen_you_win, (200,200))

#VIDAS
imagen_vida_5 = pygame.image.load("VENTANAS\imagenes\Vidas\Vida_5.png")
imagen_vida_5 = pygame.transform.scale(imagen_vida_5, (180, 50))

imagen_vida_4 = pygame.image.load("VENTANAS\imagenes\Vidas\Vida_4.png")
imagen_vida_4 = pygame.transform.scale(imagen_vida_4, (180, 50))

imagen_vida_3 = pygame.image.load("VENTANAS\imagenes\Vidas\Vida_3.png")
imagen_vida_3 = pygame.transform.scale(imagen_vida_3, (180, 50))

imagen_vida_2 = pygame.image.load("VENTANAS\imagenes\Vidas\Vida_2.png")
imagen_vida_2 = pygame.transform.scale(imagen_vida_2, (180, 50))

imagen_vida_1 = pygame.image.load("VENTANAS\imagenes\Vidas\Vida_1.png")
imagen_vida_1 = pygame.transform.scale(imagen_vida_1, (180, 50))

#BOTONES MENU
imagen_play = pygame.image.load("VENTANAS\imagenes\Botones\Play.png")
imagen_play = pygame.transform.scale(imagen_play, (200, 100))

imagen_menu = pygame.image.load("VENTANAS\imagenes\Botones\Menu.png")
imagen_menu = pygame.transform.scale(imagen_menu, (200, 100))

imagen_back = pygame.image.load("VENTANAS\imagenes\Botones\Back.png")
imagen_back = pygame.transform.scale(imagen_back, (200, 100))

imagen_score = pygame.image.load("VENTANAS\imagenes\Botones\Score.png")
imagen_score = pygame.transform.scale(imagen_score, (200, 100))

#BOTONES OPCIONES

imagen_volver = pygame.image.load("VENTANAS\imagenes\Botones\Volver.png")
imagen_volver = pygame.transform.scale(imagen_volver, (100, 80))

imagen_suma = pygame.image.load("VENTANAS\imagenes\Volumen\Botones_volumen_mas.png")
imagen_suma = pygame.transform.scale(imagen_suma, (60, 60))

imagen_resta = pygame.image.load("VENTANAS\imagenes\Volumen\Botones_volumen_menos.png")
imagen_resta = pygame.transform.scale(imagen_resta, (65, 65))

imagen_mute_on = pygame.image.load("VENTANAS\imagenes\Volumen\Mute_on.png")
imagen_mute_on = pygame.transform.scale(imagen_mute_on, (100,100))

imagen_mute_off = pygame.image.load("VENTANAS\imagenes\Volumen\Mute_off.png")
imagen_mute_off = pygame.transform.scale(imagen_mute_off, (100,100))

imagen_volumen_100 = pygame.image.load("VENTANAS\imagenes\Volumen\Volumen_100.png")
imagen_volumen_100 = pygame.transform.scale(imagen_volumen_100, (240,60))

imagen_volumen_80 = pygame.image.load("VENTANAS\imagenes\Volumen\Volumen_80.png")
imagen_volumen_80 = pygame.transform.scale(imagen_volumen_80, (240,60))

imagen_volumen_60 = pygame.image.load("VENTANAS\imagenes\Volumen\Volumen_60.png")
imagen_volumen_60 = pygame.transform.scale(imagen_volumen_60, (240,60))

imagen_volumen_40 = pygame.image.load("VENTANAS\imagenes\Volumen\Volumen_40.png")
imagen_volumen_40 = pygame.transform.scale(imagen_volumen_40, (240,60))

imagen_volumen_20 = pygame.image.load("VENTANAS\imagenes\Volumen\Volumen_20.png")
imagen_volumen_20 = pygame.transform.scale(imagen_volumen_20, (240,60))

imagen_volumen_0 = pygame.image.load("VENTANAS\imagenes\Volumen\Volumen_0.png")
imagen_volumen_0 = pygame.transform.scale(imagen_volumen_0, (240,60))