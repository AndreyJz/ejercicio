import os
from tabulate import tabulate
lstProductos={}

def MenuPrin():
    opciones =  ['1','2','3','4','5','6']
    opcion = '1. Registro de Productos\n2. Visualización de Productos\n3. Actualización de Stock\n4. Informe de Productos Críticos\n5. Cálculo de Ganancia Potencial\n6. Salir'
    print(opcion)
    op = (input('Ingrese el numero de la seccion a la que quiere ingresar\n:)_'))
    if (op not in opciones):
        print('Esa opcion no existe')
        MenuPrin()
    return op

def AddProducto(lstProductos:dict):
    CodigoProducto = input('Escriba el codigo del producto : ')
    data = lstProductos.get(CodigoProducto,False)
    if (type(data) == dict):
        print('Este producto ya se encuentra registrado')
        os.system('pause')
        AddProducto()
    elif(type(data) == bool and data == False):
        NombreProducto = input('Escriba el nombre del producto : ')
        ValorCompra = float(input('Escriba el valor de la compra del producto : '))
        ValorVenta = float(input('Escriba el valor de la venta del producto : '))
        StockMínimo = int(input('Escriba el Stock MINIMO del producto : '))
        StockMáximo = int(input('Escriba el Stock MAXIMO del producto : '))
        NombreProveedor = input('Escriba el nombre del Proveedor : ')
        Productos={
        'CodigoProducto':CodigoProducto,
        'NombreProducto':NombreProducto,
        'ValorCompra':ValorCompra,
        'ValorVenta':ValorVenta,
        'Stock':0,
        'StockMínimo':StockMínimo,
        'StockMáximo':StockMáximo,
        'NombreProveedor':NombreProveedor
        }
        lstProductos.update({CodigoProducto:Productos})
        print(lstProductos)

def ModStock(lstProductos:dict):
    CodigoProducto = input('ingrese el Codigo del producto a modificar stock: ')
    data = lstProductos.get(CodigoProducto,False)
    if(type(data) == dict):
        Mod = input('Digite el numero de lo que va a hacer? 1.Agregar Stock o 2.Restar Stock? ')
        if (Mod == '1'):
            add = int(input('ingrese la cantidad de Stock a agregar '))
            lstProductos[CodigoProducto]['Stock'] += add
        elif(Mod == '2'):
            rest = int(input('ingrese la cantidad de Stock a agregar '))
            lstProductos[CodigoProducto]['Stock'] -= rest
        else:
            print('Ingreso algo que no esta dentro de las opciones, recuerde que debe ser 1 o 2')
    elif((type(data) == bool) and (data == False)):
        print('El Producto no se encuentra registrado')


def ViewProducts(lstProductos : dict):
    os.system('cls')
    titulo = """
    ++++++++++++++++++++++
    + TABLA DE PRODUCTOS +
    ++++++++++++++++++++++
    """
    print(titulo)
    tabla = [[lstProductos[value]['CodigoProducto'], lstProductos[value]['NombreProducto'], lstProductos[value]['ValorCompra'], lstProductos[value]['ValorVenta'], lstProductos[value]['Stock'], lstProductos[value]['StockMínimo'], lstProductos[value]['StockMáximo'], lstProductos[value]['NombreProveedor']] for value in lstProductos]
    print(tabulate(tabla, headers=['CodigoProducto', 'NombreProducto', 'ValorCompra','ValorVenta','Stock','StockMínimo','StockMáximo','NombreProveedor']))

def StockMen(lstProductos:dict):
    os.system('cls')
    for key,value in lstProductos.items():
        if (lstProductos[key]['Stock'] < lstProductos[key]['StockMínimo']):
            print(lstProductos[key]['NombreProducto'])
    print('\nEstos productos tiene un Stock menor al ingresado')

def Ganancia(lstProductos:dict):
    GananciaTotal=0
    
    for key,value in lstProductos.items():
        compra = lstProductos[key]['ValorCompra']
        venta = lstProductos[key]['ValorVenta']
        stock = lstProductos[key]['Stock']
        Ganancia = (compra+venta)*stock
        print(f'La ganancia de {lstProductos[key]['NombreProducto']} es {Ganancia}$')
        GananciaTotal += Ganancia
    print(f'La ganancia total es de {GananciaTotal}$')