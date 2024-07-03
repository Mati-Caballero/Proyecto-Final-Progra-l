import json


def partidas_json(nombre,fecha,puntuacion): #CREO UNA FUNCION PARA LAS PARTIDAS Y GUARDARLAS EN UN JSON

    lista_jugadores = [] #CREO UNA LISTA DE JUGADORES VACIAS PARA QUE NO ROMPA EL JSON

    #CREO UN DICCIONARIO Y LE DOY LOS DATOS CON LOS PARAMEROS DE LA FUNCION:
    datos_del_jugador = {'nombre':nombre,'fecha':fecha.strftime('%d/%m/%Y'),'puntuacion':puntuacion} 

    with open('partidas.json', mode ='r', encoding='utf-8') as archivo: #CREO EL JSON Y LE CARGO LA LISTA VACIA
        lista_jugadores = json.load(archivo)

    lista_jugadores.append(datos_del_jugador) #APPENDEO EL DICCIONARIO CON TODOS LOS DATOS DEL JUGADOR

    with open('partidas.json', mode='w', encoding='utf-8') as archivo:
        json.dump(lista_jugadores, archivo,indent=4) #LE AÑADO EL DICCIONARIO CON LOS DATOS A LA LISTA AL JSON

    return lista_jugadores #DEVUELVO LA LISTA CON DICCIONARIO/S. 

def nomralizar_datos(lista_puntuacion:list):
    
    for key in lista_puntuacion:
        if type(key["puntuacion"]) == str:
            valor_clave = int(key["puntuacion"])
            key["puntuacion"] = valor_clave

def top_mejores_diez():
    lista_jugadores = []
    
    with open('partidas.json', mode='r', encoding='utf-8') as archivo: 
        lista_jugadores = json.load(archivo) #CARGO LA LISTA/DICCIONARIO DE LOS JUGADORES
    
    nomralizar_datos(lista_jugadores) #NORMALIZO DATOS LOS PUNTOS DEL JSON

    for i in range(len(lista_jugadores)): #UTILIZO METODO BURBUJEO PARA ORDENAR A LOS JUGADORES
        for j in range( i+1, len(lista_jugadores), 1):
            if lista_jugadores[i]["puntuacion"] < lista_jugadores[j]["puntuacion"]:
                aux = lista_jugadores[i]
                lista_jugadores[i] = lista_jugadores[j]
                lista_jugadores[j] = aux
                
    mejores_diez = lista_jugadores[:10]#PARA QUE NO PASE DE MAS DE DE 10 JUGADORES

    return mejores_diez