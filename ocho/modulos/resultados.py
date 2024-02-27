import os
from tabulate import tabulate

def Menucat():
    categorias=[1,2,3]
    titulo='''
    +++++++++++++++++++++++++
    +       CATEGORIAS      +
    +++++++++++++++++++++++++
    '''
    opciones='1. Novatos\n2. Intermedio\n3. Avanzado\n'
    print(titulo)
    print(opciones)
    op = int(input('Ingrese el numero de categoria de la que quiere ver los resultados: '))
    if op not in categorias:
        print('Esa opcion no existe')
        Menucat()
    return op



def Results(lstTorneo:dict):
    op=Menucat()
    if (op==1):
        categoria = 'Novato'
    if (op==2):
        categoria = 'Intermedio'
    if (op==3):
        categoria = 'Avanzado'
    
    os.system('cls')
    titulo = """
    +++++++++++++++++++++++++
    + RESULTADOS DEL TORNEO +
    +++++++++++++++++++++++++
    """
    print(titulo)
    tabla = [[categoria, lstTorneo[categoria][key]['id'], lstTorneo[categoria][key]['Nombre'], lstTorneo[categoria][key]['edad'], lstTorneo[categoria][key]['PJ'], lstTorneo[categoria][key]['PG'], lstTorneo[categoria][key]['PP'], lstTorneo[categoria][key]['PA'], lstTorneo[categoria][key]['TP']]for key,value in lstTorneo[categoria].items()]
    tabla_ordenada = sorted(tabla, key=lambda x: (x[8] , x[7]), reverse=True)
    print(tabulate(tabla_ordenada, headers=['Categoria', 'id', 'Nombre', 'edad', 'PJ', 'PG','PP','PA', 'TP']))
    
    print(f'El ganador del torneo en la categoria {categoria} es {tabla_ordenada[0][2]}')
    
    os.system('pause')