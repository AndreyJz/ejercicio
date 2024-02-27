import os

def MenuPrin():
    titulo='''
    ++++++++++++++++++++++++++++++++
    +   ELECTRICIDAD DEPENDENCIA   +
    ++++++++++++++++++++++++++++++++
    '''
    opciones =  ['1','2','3','4','5']
    opcion = '1. Registrar Dependencia\n2. Registrar consumo por dependencia\n3. Ver CO2 producido\n4. Dependencia que produce mayor CO2\n5. Salir'
    print(titulo)
    print(opcion)
    op = (input('Ingrese el numero de la seccion a la que quiere ingresar\n:)_'))
    if (op not in opciones):
        print('Esa opcion no existe')
        os.system('pause')
        MenuPrin()
    return op

def MenuConsumo():
    titulo='''
    +++++++++++++++++++++++++
    +   REGISTRAR CONSUMO   +
    +++++++++++++++++++++++++
    '''
    opciones =  ['1','2']
    opcion = '1. Registrar Consumo de Electricidad\n2. Registrar Consumo de Transporte\n'
    print(titulo)
    print(opcion)
    opC = (input('Ingrese el numero de la seccion a la que quiere ingresar\n:)_'))
    if (opC not in opciones):
        print('Esa opcion no existe')
        os.system('pause')
        MenuConsumo()
    return opC