import random


def adivina_numero(x): # adivina el numero entre 1 y x.
    print('BIENVENIDO')
    print(f'Debes adivinar el numero entre 1 y {x}.')
    numero_aleatorio = random.randint(1,x) # se genera el numero aleatorio
    prediccion = 0
    vidas = 3

    while prediccion != numero_aleatorio and vidas > 0:
        prediccion = int(input(f'ingresa un numero entre 1 y {x}.'))
        if prediccion > numero_aleatorio:
            print(f' {prediccion} es un numero muy grande')
            vidas -= 1
        elif prediccion < numero_aleatorio:
            print(f'{prediccion} es muy bajo.')
            vidas -= 1
    if vidas == 0:
        print('deberias dedicarte a otra cosa')
    elif prediccion == numero_aleatorio:
        print('Felicitaciones, le has atinado.')
