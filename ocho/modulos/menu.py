import os

def Menu():
    opcion=[1,2,3,4,5]
    titulo='''
    +++++++++++++++++++++++++++++
    +   TORNEO CAMPUS DE MESA   +
    +++++++++++++++++++++++++++++
    '''
    opciones='1. Registrar Jugador\n2. Registrar Partido\n3. Seguimiento de Jugador\n4. Resultado\n5. Salir\n'
    print(titulo)
    print(opciones)
    op = int(input('Ingrese el numero de la seccion a la quiere ingresar: '))
    if op not in opcion:
        print('Esa opcion no existe')
        Menu()
    return op