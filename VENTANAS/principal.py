import pygame 
from constantes import *
from menu import *
from juego import *
from opciones import *
from terminado import *
from puntuaciones import *
import opciones
import juego

pygame.init()
pantalla = pygame.display.set_mode(PANTALLA) #Se crea una ventana

pygame.display.set_caption("Preguntados")
ventana_actual = 'menu'
corriendo = True
bandera_juego = True
FPS = 60
clock = pygame.time.Clock() 

while corriendo:
    clock.tick(FPS)
    if ventana_actual == 'menu':
        ventana_actual = mostrar_menu(pantalla,pygame.event.get())
        pantalla.blit(fondo_menu, (0, 0))
    elif ventana_actual == 'opciones':
        ventana_actual = mostrar_opciones(pantalla,pygame.event.get())
        # pantalla.blit(fondo_opciones, (0, 0))
    elif ventana_actual == 'juego':
        if bandera_juego:
            pygame.mixer.music.load("VENTANAS\sonidos\musica.mp3") #Define musica de fondo mientras juego
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(opciones.volumen / 100) #Ajusta el sonido de la música de fondo para que sea el mismo que en las opciones
            bandera_juego = False
        ventana_actual = mostrar_juego(pantalla,pygame.event.get())
    elif ventana_actual == 'puntuaciones':
        ventana_actual = mostrar_puntuaciones(pantalla,pygame.event.get())
    elif ventana_actual == 'terminado':
        if bandera_juego == False:
            pygame.mixer.music.stop() #Detiene mi música de fondo
            bandera_juego = True
        ventana_actual = mostrar_juego_terminado(pantalla,pygame.event.get(),juego.puntuacion)
    elif ventana_actual == 'salir':
        corriendo = False

    pygame.display.flip() #ACTUALIZA LA INFORMACION

pygame.quit()