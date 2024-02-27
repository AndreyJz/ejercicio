import modulos.funciones as f

Ciudades = []

if __name__ == '__main__':
    isAppRunning = True
    while isAppRunning:
        f.os.system('cls')
        op=f.MenuPrin()
        if (op == '1'):
                f.os.system('cls')
                f.RegCity(Ciudades)
                f.os.system('pause')
        if (op == '2'):
            isAddSismo = True
            f.os.system('cls')
            f.RegSismos(Ciudades)
        if (op == '3'):
            isLookSismos = True
            while isLookSismos:
                f.os.system('cls')
                f.BucarSismos(Ciudades)
                isLookSismos = bool(input('Desea buscar otros sismos? S(Si) o Enter(No)' ))
        if (op == '4'):
            isRegistro = True
            while isRegistro:
                f.os.system('cls')
                f.PromSismos(Ciudades)
                isRegistro = bool(input('Desea buscar otro registro? S(Si) o Enter(No)' ))
        if (op == '5'):
            isAppRunning=False

