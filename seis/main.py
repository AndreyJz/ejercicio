import modulos.funciones as f
import modulos.Menu as m

lstDependencias = {}

if __name__ == '__main__':
    isAppRunning = True
    while isAppRunning:
        f.os.system('cls')
        op=m.MenuPrin()
        if (op == '1'):
            isAddDependencia = True
            while isAddDependencia:
                f.os.system('cls')
                f.RegDep(lstDependencias)
                isAddDependencia = bool(input('Desea agregar otra Dependencia? S(Si) o Enter(No) '))
        if (op == '2'):
            isAddConsumo = True
            while isAddConsumo:
                f.os.system('cls')
                opC=m.MenuConsumo()
                if (opC == '1'):
                    f.os.system('cls')
                    f.ConsumoXDisposito(lstDependencias)
                elif (opC == '2'):
                    f.os.system('cls')
                    f.ConsumoTransporte(lstDependencias)
                isAddConsumo = bool(input('Desea registrar otro Consumo? S(Si) o Enter(No) '))
        if (op == '3'):
            isLookCO2 = True
            while isLookCO2:
                f.os.system('cls')
                f.CO2(lstDependencias)
                isLookCO2 = bool(input('Desea seguir viendo la cantidad de producciones de CO2? S(Si) o Enter(No)' ))
        if (op == '4'):
            isList = True
            while isList:
                f.os.system('cls')
                f.lstDependencias(lstDependencias)
                isList = bool(input('Desea seguir mirando la tabla? S(Si) o Enter(No)' ))
        if (op == '5'):
            isAppRunning=False

