import os
from tabulate import tabulate

def MenuFactor():
    opciones =  ['1','2','3']
    opcion = '\n1. Energia Hidraulica\n2. Energia Termica\n3. Energia Renovable no convencional\n'
    print(opcion)
    op = (input('Ingrese el numero del factor de Emision de Electricidad\n:)_'))
    if (op not in opciones):
        MenuFactor()
    elif (op == '1'):
        Factor = 0.374
        return Factor
    elif (op == '2'):
        Factor = 0.4
        return Factor
    elif (op == '3'):
        Factor = 0.1
        return Factor
    else:
        print('Esa opcion no existe')
        MenuFactor()


Dependencias={}
def RegDep(Dependencias:dict):
    Dependencia = input('Ingrese la Dependencia: ')
    data = Dependencias.get(Dependencia,False)
    if (type(data) == dict):
        print('Esa Dependencia ya esta registrada')
    elif ((type(data) == bool) and (data == False)):
        Dep = {
            'dependencia':Dependencia,
            'ConsumoElectricidad':0,
            'ConsumoTransporte':0,
            'CO2':0,
            'Carros':[],
            'Dispositivos':[]
        }
        Dependencias.update({Dependencia:Dep})
        print(Dependencias)


def ConsumoTransporte(Dependencias:dict):
    ConsumoTrans = 0
    Dependencia = input('Ingrese la Dependencia a agregar consumo: ')
    data = Dependencias.get(Dependencia,False)
    if (type(data) == dict):
        AddCarro=True
        while AddCarro:
            os.system('cls')
            Carros = input('Ingrese un carro: ')
            Km = float(input('Ingrese cuantos Kilometros recorre el carro: '))
            Fac = MenuFactor()
            ConsumoCarro = (Km*Fac)
            Dependencias[Dependencia]['Carros'].append([Carros,ConsumoCarro])
            AddCarro= bool(input('Desea seguir agregando carros? S(si) o Enter(no) '))
        for key,value in Dependencias.items():
            for i in range(len(Dependencias[key]['Carros'])):
                ConsumoTrans += Dependencias[key]['Carros'][i][1]
        Dependencias[Dependencia].update({'ConsumoTransporte':ConsumoTrans})
        Dependencias[Dependencia]['CO2'] += ConsumoTrans
        print(Dependencias)
    elif ((type(data) == bool) and (data == False)):
        print('Esa Dependencia no esta registrada')
        os.system('pause')

def ConsumoXDisposito(Dependencias:dict):
    ConsumoTotal=0
    Dependencia = input('Ingrese la Dependencia a agregar consumo: ')
    data = Dependencias.get(Dependencia,False)
    if (type(data) == dict):
        AddDispositivo=True
        while AddDispositivo:
            os.system('cls')
            Disposito = input('Ingrese un dispositivo: ')
            Potencia = float(input('Ingrese la potencia en W que utilizan sus dispositivos: '))
            Horas = float(input('Ingrese el tiempo de uso de los dispositivos en horas: '))
            Periodo = int(input('Si el periodo facturado es mensual digite 1, si NO lo es entonces ingrese el Nro de meses que tuvo su peropdo facturado: '))
            ConsumoUno = (Potencia*Horas)/(1000)
            ConsumoMensual = ConsumoUno/Periodo
            Dependencias[Dependencia]['Dispositivos'].append([Disposito,ConsumoMensual])
            AddDispositivo= bool(input('Desea seguir agregando dispositivos? S(si) o Enter(no) '))
        for key,value in Dependencias.items():
            for i in range(len(Dependencias[key]['Dispositivos'])):
                ConsumoTotal += Dependencias[key]['Dispositivos'][i][1]
        Fac = MenuFactor()
        ConsumoElectricidad = (ConsumoTotal)*(Fac)
        Dependencias[Dependencia].update({'ConsumoElectricidad':ConsumoTotal})
        Dependencias[Dependencia]['CO2'] += ConsumoElectricidad
        print(Dependencias)
    elif ((type(data) == bool) and (data == False)):
        print('Esa Dependencia no esta registrada')

def CO2(Dependencias:dict):
    TotalCO2 = 0
    for key,value in Dependencias.items():
        TotalCO2 += Dependencias[key]['CO2']
    print(f'El total de CO2 producido por todas las Dependencias es {TotalCO2} TONELADAS ')
    
def lstDependencias(Dependencias:dict):
    os.system('cls')
    titulo = """
    +++++++++++++++++++++++++++++
    + TABLA DE CO2 DEPENDENCIAS +
    +++++++++++++++++++++++++++++
    """
    print(titulo)
    tabla=[]
    for llave,valor in Dependencias.items():
        tabla.append([Dependencias[llave]['dependencia'], Dependencias[llave]['ConsumoElectricidad'], Dependencias[llave]['ConsumoTransporte'], Dependencias[llave]['CO2']])
        tabla_ordenada = sorted(tabla, key=lambda x: x[3], reverse=True)
    print(tabulate(tabla_ordenada, headers=['Dependencia', 'ConsumoElectricidad', 'ConsumoTransporte', 'CO2'], tablefmt='grind'))
    os.system('pause')
    pausa = input('')