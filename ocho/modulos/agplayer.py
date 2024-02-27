import os

lstTorneo = {}


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
    op = int(input('Ingrese el numero de categoria a la que se quiere inscribir: '))
    if op not in categorias:
        print('Esa opcion no existe')
        Menucat()
    return op


def addPlayer(lstTorneo:dict):
    os.system('cls')
    id = int(input('Ingrese el Id del jugador '))
    op = Menucat()
    if(op==1):
        data = lstTorneo.get('Novato').get(id,False)
    elif(op==2):
        data = lstTorneo.get('Intermedio').get(id,False)
    elif(op==3):
        data = lstTorneo.get('Avanzado').get(id,False)    
    if (type(data) == dict):
        print('Este jugador ya se encuentra registrado')
        os.system('pause')
        addPlayer(lstTorneo)
    
    nombre = input('Ingrese el nombre del jugador ')
    edad = int(input('Ingrese la edad '))
    data = lstTorneo.get(id,False)

    if(type(data) == bool and data == False):
        Player={
        'id':id,
        'Nombre':nombre,
        'edad':edad,
        'PJ':0,
        'PG':0,
        'PP':0,
        'PA':0,
        'TP':0   
        }

    if (op==1):
        if (edad >= 15)and(edad <= 16):
            data = lstTorneo.get('Avanzado').get(id,False)
            data2 = lstTorneo.get('Intermedio').get(id,False)
            if (type(data) == dict) or (type(data2) == dict):
                print(f'El jugador con {id} ya se encuentra registrado en otra categoria..')
                os.system('pause')
                addPlayer(lstTorneo)
            if (type(data) == bool and data == False) or (type(data2) == bool and data2 == False): 
                lstTorneo['Novato'].update({id:Player})
                if (len(lstTorneo['Novato']) != 0) and (len(lstTorneo['Novato']) < 2):
                    print(f'Para empezar a jugar un Torneo se debe tener al menos 5 personas escitas en esta categoria, debes completar a los 5 antes de salir, llevas {len(lstTorneo['Novato'])}/5')
                    os.system('pause')
                    addPlayer(lstTorneo)       
        else:
            print('Su edad no coincide con la reglamentaria para esta categoria. Novato(15-16)')
            print('Volvera a empezar desde el pricipio...')
            os.system('pause')
            addPlayer(lstTorneo)
    if (op==2):
        if (edad >= 17)and(edad <= 20):
            data = lstTorneo.get('Avanzado').get(id,False)
            data2 = lstTorneo.get('Novato').get(id,False)
            if (type(data) == dict) or (type(data2) == dict):
                print(f'El jugador con {id} ya se encuentra registrado en otra categoria..')
                os.system('pause')
                addPlayer(lstTorneo) 
            if (type(data2) == bool and data == False) or (type(data2) == bool and data2 == False): 
                lstTorneo['Intermedio'].update({id:Player})
                if (len(lstTorneo['Intermedio']) != 0) and (len(lstTorneo['Intermedio']) < 2):
                    print(f'Para empezar a jugar un Torneo se debe tener al menos 5 personas escitas en esta categoria, debes completar a los 5 antes de salir, llevas {len(lstTorneo['Intermedio'])}/5')
                    os.system('pause')
                    addPlayer(lstTorneo)
        else:
            print('Su edad no coincide con la reglamentaria para esta categoria. Intermedio(17-20)')
            print('Volvera a empezar desde el pricipio...')
            os.system('pause')
            addPlayer(lstTorneo)
    if (op==3):
        if (edad > 20):
            data = lstTorneo.get('Novato').get(id,False)
            data2 = lstTorneo.get('Intermedio').get(id,False)
            if (type(data) == dict) or (type(data2) == dict):
                print(f'El jugador con {id} ya se encuentra registrado en otra categoria..')
                os.system('pause')
                addPlayer(lstTorneo) 
            if (type(data) == bool and data == False) or (type(data2) == bool and data2 == False): 
                lstTorneo['Avanzado'].update({id:Player})
                if (len(lstTorneo['Avanzado']) != 0) and (len(lstTorneo['Avanzado']) < 2):
                    print(f'Para empezar a jugar un Torneo se debe tener al menos 5 personas escitas en esta categoria, debes completar a los 5 antes de salir, llevas {len(lstTorneo['Avanzado'])}/5')
                    os.system('pause')
                    addPlayer(lstTorneo)
        else:
            print('Su edad no coincide con la reglamentaria para esta categoria. Avanzado(más de 20)')
            print('Volvera a empezar desde el pricipio...')
            os.system('pause')
            addPlayer(lstTorneo)
            

    
    