import os

normal=[]
sobrepeso=[]
obesidadI=[]
obesidadII=[]
obesidadIII=[]


for i in range(20):
    os.system('cls')
    nombre = input('Ingrese su nombre ')
    edad = input('Ingrese su edad ')
    peso = float(input('Ingrese su peso en Kg (utilice un punto para las cifras decimales) '))
    altura = float(input('Ingrese su altura en m (utilice un punto para las cifras decimales) '))

    IMC = (peso/(altura**2))

    if (IMC < 18.5):
        print(f'El IMC de {nombre} con {edad} años, marca: {IMC} y dice que esta delgado\n')
        obesidadIII.append(nombre)
    elif (IMC >= 18.5) and (IMC <= 24.9):
        print(f'E IMC de {nombre} con {edad} años, marca: {IMC} y dice que esta normal\n')
        normal.append(nombre)
    elif (IMC >= 25) and (IMC <= 29.9):
        print(f'El IMC de {nombre} con {edad} años, marca: {IMC} y dice que esta en sobrepeso\n')
        sobrepeso.append(nombre)
    elif (IMC >= 30) and (IMC <= 34.9):
        print(f'El IMC de {nombre} con {edad} años, marca: {IMC} y dice que esta en obesidad I\n')
        obesidadI.append(nombre)
    elif (IMC >= 35) and (IMC <= 39.9):
        print(f'El IMC de {nombre} con {edad} años, marca: {IMC} y dice que esta en obesidad II\n')
        obesidadII.append(nombre)
    elif (IMC >= 40):
        print(f'El IMC de {nombre} con {edad} años, marca: {IMC} y dice que esta en obesidad III\n')
        obesidadIII.append(nombre)

Healt=True
while Healt:
    os.system('cls')
    opciones =  ['a','b','c','d','e']
    opcion = 'a. Cuantos estudiantes se encuentran en el peso ideal \nb. Cuantos estudiantes se encuentran en obesidad grado I\nc. Cuantos estudiantes se encuentran en obesidad grado II\nd. Cuantos estudiantes se encuentran en obesidad grado III\ne. Cuantos estudiantes se encuentran en Sobrepeso'
    print(opcion)
    op = (input('Que quiere ver?\n:)_'))
    if (op == 'a'):
        print(f'{len(normal)} estudiantes se encuentran ahi')
    if (op == 'b'):
        print(f'{len(obesidadI)} estudiantes se encuentran ahi')
    if (op == 'c'):
        print(f'{len(obesidadII)} estudiantes se encuentran ahi')
    if (op == 'd'):
        print(f'{len(obesidadIII)} estudiantes se encuentran ahi')
    if (op == 'e'):
        print(f'{len(sobrepeso)} estudiantes se encuentran ahi')
    else:
        print('Esa opcion no es valida')
        os.system('pause')
    Healt= bool(input('Desea salir ver mas cosas? S(si) o Enter(no)'))