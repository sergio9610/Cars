from modulos import *

# ------- Función de aplicación -------
def main():
    while True:  
        figura()

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
            
        while True:
            try:
                pistasKm = [2000,5000,10000,21000]
                carrera(numJugadores,listaJugadores,pistasKm,pista)
                #enter = input("\n   Click en"+Fore.RED+" ENTER "+Fore.WHITE+"para continuar")
                if True:
                    break
            except ValueError:
                print('ERROR')


    # Movimientos de la carrera
        # while True:
        #     try:
        #         c = 1
        #         pistas = [10000,15000,21000,42000]
        #         carrera(numJugadores,listaJugadores,pistas,pista)
        #         #enter = input("\n   Click en"+Fore.RED+" ENTER "+Fore.WHITE+"para continuar")
        #         if c == 0:
        #             break
        #         else:
        #             print('SIGAA')
        #     except ValueError:
        #         print('ERROR')



# ------- Ejecución de aplicación -------
main()
