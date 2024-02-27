import os
lstNro = []
lstNroPar = []
lstNroImpar = []
Num10 = []
Num20y50 = []
Num100 = []

Num=True
while Num:
    Nro = int(input('Ingrese números enteros positivos: '))
    if Nro < 0:
        print('Ups escribiste un numero que no es entero positivo')
        Healt=True
        while Healt:
            os.system('pause')
            opciones =  ['a','b','c','d','e','f','g']
            opcion = 'a. Total de números ingresados\nb. Total de números pares ingresados\nc. Promedio de los números pares\nd. Promedio de los números impares\ne. Cuantos números son menores que 10\nf. Cuantos números están entre 20 y 50\ng. Cuantos números son mayores que 100'
            print(opcion)
            op = (input('Que quiere ver?\n:)_'))
            if (op == 'a'):
                print(f'{len(lstNro)} numeros fueron ingresados')
            if (op == 'b'):
                print(f'{len(lstNroPar)} numeros pares fueron ingresados')
            if (op == 'c'):
                prompar = (len(lstNroPar)/len(lstNro))
                print(f'{prompar} es el promedio de numeros pares')
            if (op == 'd'):
                promimpar = (len(lstNroImpar)/len(lstNro))
                print(f'{promimpar} es el promedio de numeros impares')
            if (op == 'e'):
                print(f'{len(Num10)} numeros son menores que 10')
            if (op == 'f'):
                print(f'{len(Num20y50)} numeros estan entre 20 y 50')
            if (op == 'g'):
                print(f'{len(Num100)} numeros son mayores que 100')
            else:
                print('Esa opcion no es valida')
            Healt= bool(input('Desea ver mas cosas? S(si) o Enter(no)'))
        break
    else:
        lstNro.append(Nro)
        if (Nro%2) == 0: 
            lstNroPar.append(Nro)
        else:
            lstNroImpar.append(Nro)
        if (Nro < 10):
            Num10.append(Nro)
        elif ((Nro >= 20) and (Nro <= 50)):
            Num20y50.append(Nro)
        elif (Nro > 100):
            Num100.append(Nro)
