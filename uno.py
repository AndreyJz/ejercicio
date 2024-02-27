import os
lstNro = []

for i in range(3):
    while True:
        Nro = int(input('Ingrese el número entero positivo {} de 3: '.format(i+1)))
        if Nro <= 0:
            print('Eso no es un número entero positivo, por favor vuelva a ingresar.')
        else:
            lstNro.append(Nro)
            break


suma = (lstNro[0] + lstNro[1] + lstNro[2])
print(f'La suma de {lstNro[0]} + {lstNro[1]} + {lstNro[2]} = {suma}')
