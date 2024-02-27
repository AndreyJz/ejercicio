import os
from tabulate import tabulate
lstPartidos = {}

def AddGame(lstTorneo:dict,lstPartidos:dict):
    os.system('cls')
    titulo = """
    +++++++++++++++++++++++++++
    +   REGISTRO DE PARTIDO   +
    +++++++++++++++++++++++++++
    """
    print(titulo)

    nroPartido = int(input('Ingrese el numero del partido : '))
    if nroPartido in lstPartidos:
        print(f'Ya existe un partido con el número {nroPartido}.')
        os.system('pause')
        
    else:
        partido = {
            'set1':{},
            'set2':{},
            'set3':{}
            }
        categoria = input('Ingrese la categoria del partido: (Novato) o (Intermedio) o (Avanzado), Asegurese de escribirlo tal cual esta ahí.. ')
        id1 = int((input('Ingrese el Id del jugador 1 ')))
        id2 = int((input('Ingrese el Id del jugador 2 ')))
        data1 = lstTorneo.get(categoria).get(id1,False)
        data2 = lstTorneo.get(categoria).get(id2,False)
        if(type(data1 and data2) == dict):
            Player1 = lstTorneo[categoria][id1]['Nombre']
            Player2 = lstTorneo[categoria][id2]['Nombre']
            Sets={
                'SetP1':0,
                'SetP2':0
            }
            SetP1=0
            SetP2=0
            PuntosFav=0
            for llave,valor in partido.items():
                PuntosP1 = int(input(f'Ingrese los puntos marcador por {Player1} en el {llave}: '))
                PuntosP2 = int(input(f'Ingrese los puntos marcador por {Player2} en el {llave}: '))
                
                if(type(PuntosP1 and PuntosP2) == int):
                    pass
                else:
                    os.system('cls')
                    print('Dato erroeno, solo puede ingresar numeros')
                    print('Volvera a empezar desde el pricipio...')
                    os.system('pause')
                    AddGame(lstTorneo,lstPartidos)
                   
                    
                if (((PuntosP1 > 11) and (PuntosP2 >= 10)) and ((PuntosP1-2) == (PuntosP2))) or (((PuntosP2 > 11) and (PuntosP1 >= 10)) and ((PuntosP2-2) == (PuntosP1))):
                   pass 
                elif ((PuntosP1 > 11) and (PuntosP2 <= 10)):
                    print('La cantidad maxima de puntos por set si es superior a 11 debe ser 2 puntos por encima del rival')
                    print('Volvera a empezar desde el pricipio...')
                    os.system('pause')
                    AddGame(lstTorneo,lstPartidos)
                
                
                partido[llave][Player1] = {'id':id1, 'nombre':Player1, 'pts':PuntosP1}
                partido[llave][Player2] = {'id':id2, 'nombre':Player2, 'pts':PuntosP2}
                
                PuntosFav += (partido[llave][Player1]['pts'])-(partido[llave][Player2]['pts'])
            
            
                if partido[llave][Player1]['pts']>partido[llave][Player2]['pts']:
                    print(f'\n{Player1} le gano a {Player2} en el {llave}\n')
                    SetP1 += 1
                    Sets.update({'SetP1':SetP1})
                if partido[llave][Player2]['pts']>partido[llave][Player1]['pts']:
                    print(f'\n{Player2} le gano a {Player1} en el {llave}\n')
                    SetP2 += 1
                    Sets.update({'SetP2':SetP2})
                
                
                if (Sets['SetP1'] == 2):
                    lstTorneo[categoria][id1]['PA'] += PuntosFav
                    lstTorneo[categoria][id1]['PJ'] += 1
                    lstTorneo[categoria][id1]['PG'] += 1
                    lstTorneo[categoria][id1]['TP'] += 2
                    lstTorneo[categoria][id2]['PJ'] += 1
                    lstTorneo[categoria][id2]['PP'] += 1
                    lstPartidos.update({nroPartido:partido})
                    break
                elif (Sets['SetP2'] == 2):
                    lstTorneo[categoria][id2]['PA'] += PuntosFav
                    lstTorneo[categoria][id2]['PJ'] += 1
                    lstTorneo[categoria][id2]['PG'] += 1
                    lstTorneo[categoria][id2]['TP'] += 2
                    lstTorneo[categoria][id1]['PJ'] += 1
                    lstTorneo[categoria][id1]['PP'] += 1
                    lstPartidos.update({nroPartido:partido})
                    break
       
        else:
            print('Alguno de los jugadores no se encuentra registrado en esa categoria o directamente no lo registro en ninguna, registrelo primero')
            os.system('pause')