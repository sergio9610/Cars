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
                print('ERROR: Debe ingresar un número válido')
    
    # Lista de Jugadores
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
                print('ERROR: Debe ingresar un número válido')
    
    
    # Iniciación del Juego
        while True:
            try:
                datos(numJugadores,pista,listaJugadores)
                enter = input("\n   Click en"+Fore.MAGENTA+" ENTER "+Fore.WHITE+"para continuar")
                if True:
                    break
            except ValueError:
                print('ERROR')

        
# ------- Ejecución de aplicación -------
main()