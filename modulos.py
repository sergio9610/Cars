from os import system
from colorama import Fore
import random

# ---------- Figura ----------
def figura():
    #Título
    system("cls")    
    print(Fore.BLUE+"       ___     _     ___   ___")
    print(Fore.WHITE+"      / __|   /_\   | _ \ / __|")
    print(Fore.BLUE+"     | (__   / _ \  |   / \ \ ")
    print(Fore.WHITE+"      \__ | /_/ \_\ |_|_\ /_/")

# ---------- Figura 2 ----------
def visConfig():
    print(Fore.BLUE+"\n   =================================")
    print(Fore.WHITE+"        Configuración del Juego")
    print(Fore.BLUE+"   =================================\n")

# ---------- Número de Jugadores ----------
def numeroJugadores():
    jugadores = int(input(Fore.WHITE+"   Ingrese la cantidad de jugadores: "))
    return jugadores


# ---------- Nombre de Jugadores ----------
def nombreJugadores(numeroJugadores):
    figura()
    visConfig()
    global listaJugadores # se define globalmente para luego ser llamado
    listaJugadores = [];
    
    for i in range(numeroJugadores):
        listaJugadores.append(input(Fore.WHITE+"   Ingrese el nickname del jugador "+str(i+1)+": "))
    
    return listaJugadores


# ---------- Pistas ----------
def pistas():
    figura()
    print(Fore.BLUE+"\n   =================================")
    print(Fore.WHITE+"            Escoja la Pista")
    print(Fore.BLUE+"   =================================\n")
    print(Fore.WHITE+"   Pista 1. 2km ")
    print(Fore.WHITE+"   Pista 2. 5km ")
    print(Fore.WHITE+"   Pista 3. 10km ")
    print(Fore.WHITE+"   Pista 4. 21km ")


# ---------- Datos Carrera ----------
def datos(numJugadores,pista,listaJugadores):
    print(Fore.BLUE+"\n   =================================")
    print(Fore.WHITE+"        Datos de la Carrera")
    print(Fore.BLUE+"   =================================\n")
    print(Fore.WHITE+"   Número de jugadores: "+Fore.BLUE+str(numJugadores)+Fore.WHITE+"\n   Pista: "+Fore.BLUE+str(pista))
    print("\n   Conductor       Carro          Carril\n")
    for numero in range(numJugadores):
        print(Fore.WHITE+"   "+listaJugadores[numero],end="")
        for jugador in range(18-len(listaJugadores[numero])):
            print(" ",end="")
        print(str(numero+1),end="")
        print("              "+str(numero+1))
    
# ---------- Carrera ----------
def carrera(numJugadores,listaJugadores,pistas,pista):
    system("cls")
    listaCarriles = []
    # Se añaden carriles a partir del número de jugadores con el valor de la pista
    for i in range(int(numJugadores)): 
            listaCarriles.append(pistas[pista-1])  
    
    bandera = 0 # bandera de finalización
    listaPodio = [] 
    
    # Ciclo principal para completación de llegada
    while bandera == 0: 
        listaAux = listaJugadores[:] # lista auxiliar para asignación de turnos
    
    # For que barre los jugadores y movimientos del carro
        auxVisual = 0   # variable auxiliar para visualizar los movimientos generados
        for i in range(numJugadores): 
            turno = random.choice(listaAux) # generación del turno aleatorio
            listaAux.remove(turno) # solo se debe mover un jugador por turno
            movimiento = random.randint(1,6)*100 # generación del movimiento aleatorio (dado)
            
            if auxVisual%2 == 0:
                print("\n    JUGADOR: "+Fore.BLUE+turno)
                if movimiento == 100:
                    print(Fore.WHITE+"              ___")
                    print(Fore.WHITE+"            __| (|__")
                    print(Fore.WHITE+"---> 100m  |_()_()_|")
                elif movimiento == 200:
                    print(Fore.WHITE+"                   ___")
                    print(Fore.WHITE+"                 __| (|__")
                    print(Fore.WHITE+"----> 200m      |_()_()_|")
                elif movimiento == 300:
                    print(Fore.WHITE+"                      ___")
                    print(Fore.WHITE+"                    __| (|__")
                    print(Fore.WHITE+"----> 300m         |_()_()_|")
                elif movimiento == 400:
                    print(Fore.WHITE+"                         ___")
                    print(Fore.WHITE+"                       __| (|__")
                    print(Fore.WHITE+"----> 400m            |_()_()_|")
                elif movimiento == 500:
                    print(Fore.WHITE+"                            ___")
                    print(Fore.WHITE+"                          __| (|__")
                    print(Fore.WHITE+"-----> 500m              |_()_()_|")
                elif movimiento == 600:
                    print(Fore.WHITE+"                               ___")
                    print(Fore.WHITE+"                             __| (|__")
                    print(Fore.WHITE+"-----> 600m                 |_()_()_|")
                
                enter = input("\n   Presione"+Fore.GREEN+" ENTER "+Fore.WHITE+"para continuar")
            auxVisual = auxVisual + 1
            
            # Verificaciónd de finalización del carril
            if(listaCarriles[listaJugadores.index(turno)] > 0): 
                listaCarriles[listaJugadores.index(turno)] = listaCarriles[listaJugadores.index(turno)]-movimiento # actualización del recorrido 
            
            if(listaCarriles[listaJugadores.index(turno)] <= 0):  
                
                # Verificaición del jugador en el podio
                banderaPodio = turno in listaPodio 
                if banderaPodio == False: 
                    listaPodio.append(turno) 
        
        # Confirmación y verificación de carros en la meta
        carrosMeta = 0 
        for i in range(numJugadores): 
            if listaCarriles[i] <= 0: 
                carrosMeta = carrosMeta+1 # actualización de carros en la meta

        if carrosMeta == numJugadores: 
            bandera = 1  # finalización de carrera
    
    return listaPodio

# ---------- Calificación ----------
def calificacion(listaPodio):
    figura()
    print(Fore.BLUE+"\n   =================================")
    print(Fore.WHITE+"                Podio")
    print(Fore.BLUE+"   =================================\n")
    print("               "+Fore.WHITE+listaPodio[0])
    print("               _____")
    print("     "+Fore.WHITE+listaPodio[1]+"      /     \ ")
    print("    ___       |  "+Fore.YELLOW+"1"+Fore.WHITE+"  |")
    print(Fore.WHITE+"   /   \      \_____/         "+Fore.WHITE+listaPodio[2])
    print("   | "+Fore.CYAN+"2"+Fore.WHITE+" |                     ___")
    print("   \___/                    /   \ ")
    print("                            | "+Fore.LIGHTRED_EX+"3"+Fore.WHITE+" |")
    print("                            \___/")