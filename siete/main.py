import modulos.funciones as f

Productos = {}

if __name__ == '__main__':
    isAppRunning = True
    while isAppRunning:
        f.os.system('cls')
        op=f.MenuPrin()
        if (op == '1'):
            isAddProducto = True
            while isAddProducto:
                f.os.system('cls')
                f.AddProducto(Productos)
                isAddProducto = bool(input('Desea agregar otro Producto? S(Si) o Enter(No) '))
        if (op == '2'):
            isLook = True
            while isLook:
                f.os.system('cls')
                f.ViewProducts(Productos)
                isLook = bool(input('Desea seguir viendo los productos? S(Si) o Enter(No)' ))
        if (op == '3'):
            isModStock = True
            while isModStock:
                f.os.system('cls')
                f.ModStock(Productos)
                isModStock = bool(input('Desea modificar el Stock de otro producto? S(Si) o Enter(No) '))
        if (op == '4'):
            isCritic = True
            while isCritic:
                f.os.system('cls')
                f.StockMen(Productos)
                isCritic= bool(input('Desea seguir mirando la lista? S(Si) o Enter(No)' ))
        if (op == '5'):
            isEarn = True
            while isEarn:
                f.os.system('cls')
                f.Ganancia(Productos)
                isEarn = bool(input('Desea seguir mirando las ganacias? S(Si) o Enter(No)' ))
        if (op == '6'):
            isAppRunning=False
