import os

def generar_csv(nombre_archivo:str,lista:list):
    if len(lista) > 0:
        lista_claves = list(lista[0].keys())
        separador = ","
        cabecera = separador.join(lista_claves)
        print(cabecera)
        
        with open(nombre_archivo,"w", encoding="utf-8") as archivo:
            archivo.write(cabecera + "\n")
            for elemento in lista:
                lista_valores = list(elemento.values())
                for i in range(len(lista_valores)):
                    lista_valores[i] = str(lista_valores[i])

                dato = separador.join(lista_valores)
                dato += "\n"
                archivo.write(dato)
    else:
        print("ERROR LISTA VACIA")

def parse_csv(nombre_archivo:str): 
    lista_elementos = [] #Lista preguntas
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r" , encoding='utf-8') as archivo:
            primer_linea = archivo.readline()
            primer_linea = primer_linea.replace("\n","")
            lista_claves = primer_linea.split(",")
            for linea in archivo:
                linea_aux = linea.replace("\n","")
                lista_valores = linea_aux.split(",")
                diccionario_aux = {} #Preguntas                
                for i in range(len(lista_claves)):
                    diccionario_aux[lista_claves[i]] = lista_valores[i]
                
                lista_elementos.append(diccionario_aux)
        
        return lista_elementos
    else:
        print("ARCHIVO NO ENCONTRADO")

lista_preguntas = parse_csv("VENTANAS\preguntas.csv")

