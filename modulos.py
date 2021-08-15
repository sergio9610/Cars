from os import system
from colorama import Fore

# ------- Figura -------
def figura():
    #Título
    system("cls")    
    print(Fore.BLUE+"       ___     _     ___   ___")
    print(Fore.WHITE+"      / __|   /_\   | _ \ / __|")
    print(Fore.BLUE+"     | (__   / _ \  |   / \ \ ")
    print(Fore.WHITE+"      \__ | /_/ \_\ |_|_\ /_/")
    print(Fore.BLUE+"\n   =================================")
    print(Fore.WHITE+"        Configuración del Juego")
    print(Fore.BLUE+"   =================================\n")

# ------- Número de Jugadores -------
def numeroJugadores():
    jugadores = int(input(Fore.WHITE+"   Ingrese la cantidad de jugadores: "))
    return jugadores


# ------- Nombre de Jugadores -------
def nombreJugadores(numeroJugadores):
    figura()
    global listaJugadores
    listaJugadores = [];
    
    for i in range(numeroJugadores):
        listaJugadores.append(input(Fore.WHITE+"   Ingrese el nickname del jugador "+str(i+1)+": "))
    
    return listaJugadores


# ------- Pistas -------
def pistas():
    figura()
    print(Fore.BLUE+"   =================================")
    print(Fore.WHITE+"            Escoja la Pista")
    print(Fore.BLUE+"   =================================\n")

    #pistas = [10000,15000,21000,42000]
    print(Fore.WHITE+"   Pista 1. 10km ")
    print(Fore.WHITE+"   Pista 2. 15km ")
    print(Fore.WHITE+"   Pista 3. 21km ")
    print(Fore.WHITE+"   Pista 4. 42km ")

#------- Datos Carrera ------
def datos(numJugadores,pista,listaJugadores):
    #figura()
    print(Fore.BLUE+"\n   =================================")
    print(Fore.WHITE+"        Datos de la Carrera")
    print(Fore.BLUE+"   =================================\n")
    print(Fore.WHITE+"   Número de jugadores: "+Fore.BLUE+str(numJugadores)+Fore.WHITE+"\n   Pista: "+Fore.BLUE+str(pista))
    #print("pista-> "+str(pista)+"      longitud-> ")
    print("\n   Conductor       Carro          Carril\n")
    for i in range(numJugadores):
        print(Fore.WHITE+"   "+listaJugadores[i],end="")
        for j in range(18-len(listaJugadores[i])):
            print(" ",end="")
        print(str(i+1),end="")
        print("              "+str(i+1))
    