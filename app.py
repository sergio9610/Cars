from modulos import *

# ------- Función de aplicación -------
def main():
    while True: 
    # Visualizaciones iniciales 
        figura()
        visConfig()

    # Validación Número de Jugadores
        while True:
            try:
                global numJugadores    # se define globalmente para luego ser llamado
                numJugadores = numeroJugadores()
                if numJugadores > 0:
                    break
                else:
                    print(Fore.RED+'\n   MENSAJE: Debe ingresar un número mayor a 0\n')
            except ValueError:
                print(Fore.RED+'\n   ERROR: Debe ingresar un número válido\n')
    
    # Lista de Jugadores
        global listaJugadores
        listaJugadores = nombreJugadores(numJugadores)
    

    # Validación Pista        
        while True:
            try:
                pistas()
                global pista 
                pista = int(input('\n   Ingrese la opción: '))
                if 0 < pista < 5:
                    break
                else:
                    print('MENSAJE: Debe ingresar un número mayor a 0 y menor a 5')
            except ValueError:
                print(Fore.RED+'\n   ERROR: Debe ingresar un número válido\n')
    
    
    # Iniciación del Juego
        while True:
            try:
                datos(numJugadores,pista,listaJugadores)
                enter = input("\n   Presione"+Fore.MAGENTA+" ENTER "+Fore.WHITE+"para continuar\n")
                if True:
                    break
            except ValueError:
                print('ERROR')
   
    # Movimiento de la Carrera        
        while True:
            try:
                pistasKm = [1000,5000,10000,21000]
                global listaPodio
                listaPodio = carrera(numJugadores,listaJugadores,pistasKm,pista)
                if True:
                    break
            except ValueError:
                print('ERROR')

    # Podio de la Carrera
        while True:
            try:
                calificacion(listaPodio)
                enter = input("\n   Presione"+Fore.RED+" ENTER "+Fore.WHITE+"para Finalizar el Juego")
                if True:
                    break
            except ValueError:
                print("ERROR")

# ------- Ejecución de aplicación -------
main()
