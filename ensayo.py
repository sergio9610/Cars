nombres = []
y = ['2','3']
for i in range(len(y)):
    name=input('\n ingresa un nombre: ')
    nombres.append(name)

for nombre in range(len(nombres)):
    #print(nombre)
    if nombres[nombre] == '':
        print('\n   MENSAJE: Debe ingresar un nickname a cada jugador \n') 
    else:
        break