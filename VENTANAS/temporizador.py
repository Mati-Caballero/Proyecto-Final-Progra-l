import time

def temporizador(tiempo_de_juego:int):
    
    while tiempo_de_juego:
        min = tiempo_de_juego // 60
        seg = tiempo_de_juego % 60
        
        tiempo_restante = f"{min:02d}:{seg:02d}"
        print(f"Tiempo restante: {tiempo_restante}", end= "\r")
        time.sleep(1)
        tiempo_de_juego -= 1
    print("¡Tiempo finalizado!")

temporizador(10)