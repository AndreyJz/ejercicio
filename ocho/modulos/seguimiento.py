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
    op = int(input('Ingrese el numero de categoria en la que esta inscrito: '))
    if op not in categorias:
        print('Esa opcion no existe')
        Menucat()
    return op

def segPlayer(lstTorneo:dict):
    id = int(input('Ingrese el Id del jugador que quiere buscar: '))
    op=Menucat()
    if (op==1):
        categoria = 'Novato'
    if (op==2):
        categoria = 'Intermedio'
    if (op==3):
        categoria = 'Avanzado'
    
    data = lstTorneo.get(categoria).get(id,False)
    
    if (type(data) == dict):
        os.system('cls')
        titulo = """
        +++++++++++++++++++++++
        + ESTADISTICA JUGADOR +
        +++++++++++++++++++++++
        """
        print(titulo)
        tabla = [[categoria, lstTorneo[categoria][id]['id'], lstTorneo[categoria][id]['Nombre'], lstTorneo[categoria][id]['edad'], lstTorneo[categoria][id]['PJ'], lstTorneo[categoria][id]['PG'], lstTorneo[categoria][id]['PP'], lstTorneo[categoria][id]['PA'], lstTorneo[categoria][id]['TP']]]
        tabla_ordenada = sorted(tabla, key=lambda x: x[8], reverse=True)
        print(tabulate(tabla_ordenada, headers=['Categoria', 'id', 'Nombre', 'edad', 'PJ', 'PG','PP','PA', 'TP']))
        
        
        
        os.system('pause')
    

        
    elif(type(data) == bool and data == False):
        print('Este jugador no se encuentra registrado')
        os.system('pause')
        segPlayer(lstTorneo)