import json

def guardar_puntuacion(puntuacion):
    """
    Crea un JSON guardando las puntuaciones de cada jugador
    """
    puntuacion = str(puntuacion)
    with open("puntuacion.json", "w") as archivo:
        json.dump({"puntuacion": puntuacion}, archivo)

def cargar_puntuacion():
    """
    Parsea y carga el Json con los puntajes, si no hay ninguna partida jugada la puntuacion es 0
    """
    with open("puntuacion.json", "r") as archivo:
        datos = json.load(archivo)
        return datos.get("puntuacion", 0)

def partidas_json(nombre,fecha,puntuacion):
    """
    Crea un JSON con las partidas jugadas
    """
    lista_jugadores = []
    
    datos_del_jugador = {'nombre':nombre,'fecha':fecha.strftime('%d/%m/%Y'),'puntuacion':puntuacion}
    
    with open('partidas.json', mode ='r', encoding='utf-8') as archivo:
        lista_jugadores = json.load(archivo)
    
    lista_jugadores.append(datos_del_jugador)
    
    with open('partidas.json', mode='w', encoding='utf-8') as archivo:
        json.dump(lista_jugadores, archivo,indent=4)
    
    return lista_jugadores

def nomralizar_datos(lista_puntuacion:list):
    
    for key in lista_puntuacion:
        if type(key["puntuacion"]) == str:
            valor_clave = int(key["puntuacion"])
            key["puntuacion"] = valor_clave

def top_mejores_diez():
    """
    Ordena la el JSON con el metodo burbujeo y no permite mostrar mas de 10
    """
    lista_jugadores = []
    
    with open('partidas.json', mode='r', encoding='utf-8') as archivo: 
        lista_jugadores = json.load(archivo) 
    
    nomralizar_datos(lista_jugadores)
    
    for i in range(len(lista_jugadores)):
        for j in range( i+1, len(lista_jugadores), 1):
            if lista_jugadores[i]["puntuacion"] < lista_jugadores[j]["puntuacion"]:
                aux = lista_jugadores[i]
                lista_jugadores[i] = lista_jugadores[j]
                lista_jugadores[j] = aux
    
    mejores_diez = lista_jugadores[:10]
    
    return mejores_diez