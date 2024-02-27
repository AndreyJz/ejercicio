import os

lstCiudades = []
TotalValor = 0
def RegCity(lstCiudades:list):
    for i in range(5):
        newCity = input(f'Ingrese el nombre de las ciudades ({i+1}/5): ')
        lstCiudades.append([newCity,[]])

def RegSismos(lstCiudades:list):
    n = int(input('Ingrese el numero de sismos que agregara por ciudad: '))
    for i in lstCiudades:
        City = input('Ingrese la ciudad en la que va a agregar el sismo: ')
        for idx,item in enumerate(lstCiudades):
            if (City in item):
                j=1
                for i in range(n):
                    newSismo = float(input(f'Ingrese el sismo Nro{j} que se reporto en {City} '))
                    lstCiudades[idx][1].append(newSismo)
                    j=j+1
                    print(lstCiudades)


def BucarSismos(lstCiudades:list):
        City = input('Ingrese la ciudad en la que se presento el sismo: ')
        for idx,item in enumerate(lstCiudades):
            if (City in item):
                print(f'Estos son los sismos registrados en {City}')
                print(lstCiudades[idx][1])
                os.system('pause')

def MenuPrin():
    titulo='''
    +++++++++++++++++++
    +   MENU SISMOS   +
    +++++++++++++++++++
    '''
    opciones =  ['1','2','3','4','5']
    opcion = '1. Registrar Ciudad\n2. Registrar Sismo\n3. Buscar sismos por ciudad\n4. Informe de riesgo\n5. Salir'
    print(titulo)
    print(opcion)
    op = (input('Ingrese el numero de la seccion a la que quiere ingresar\n:)_'))
    if (op not in opciones):
        print('Esa opcion no es valida')
        os.system('pause')
        MenuPrin()
    return op

def PromSismos(lstCiudades):
    total = 0
    TotalValor = 0
    n = len(lstCiudades[0][1])
    City = input('Ingrese la ciudad en la que va a mirar el promedio de sismos: ') 
    
    for idx,item in enumerate(lstCiudades):
        total += len(lstCiudades[idx][1])
        if (City in item):
            for i in range(n):
                TotalValor += lstCiudades[idx][1][i]
    Prom = TotalValor/total
    
    if Prom <= 2.5:
        print(f'El promedio de magnitud de sismos en {City} es {Prom} y se enceuntra es estado Amarillo(Sin Riesgos)')
        os.system('pause')
    elif (Prom >= 2.6 and Prom <= 4.5):
        print(f'El promedio de magnitud de sismos en {City} es {Prom} y se enceuntra es estado Naranja(Riesgo Medio)')
        os.system('pause')
    elif (Prom > 4.5):
        print(f'El promedio de magnitud de sismos en {City} es {Prom} y se enceuntra es estado Rojo(Riesgo Alto)')
        os.system('pause')