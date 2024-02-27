
nombre = input('Ingrese su nombre ')
edad = input('Ingrese su edad ')
peso = float(input('Ingrese su peso en Kg (utilice un punto para las cifras decimales) '))
altura = float(input('Ingrese su altura en m (utilice un punto para las cifras decimales) '))

IMC = (peso/(altura**2))

if (IMC < 18.5):
    print(f'El IMC de {nombre} con {edad} años, marca: {IMC} y dice que esta delgado\n')
elif (IMC >= 18.5) and (IMC <= 24.9):
    print(f'E IMC de {nombre} con {edad} años, marca: {IMC} y dice que esta normal\n')
elif (IMC >= 25) and (IMC <= 29.9):
    print(f'El IMC de {nombre} con {edad} años, marca: {IMC} y dice que esta en sobrepeso\n')
elif (IMC >= 30) and (IMC <= 34.9):
    print(f'El IMC de {nombre} con {edad} años, marca: {IMC} y dice que esta en obesidad I\n')
elif (IMC >= 35) and (IMC <= 39.9):
    print(f'El IMC de {nombre} con {edad} años, marca: {IMC} y dice que esta en obesidad II\n')
elif (IMC >= 40):
    print(f'El IMC de {nombre} con {edad} años, marca: {IMC} y dice que esta en obesidad III\n')
