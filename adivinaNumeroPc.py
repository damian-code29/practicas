import random
def adivina_numero_2(x):
    #saludo
    print('BIENVENIDO')
    print(f'selecciona un numero entre 1 y {x} para que la pc intente adivinarlo. ')
    print('ingresa (a) si es muy alta, (b) si es muy baja ó (c) si es correcto. ')

    limite_inferior = 1
    limite_superior = x
    respuesta = ''
    while respuesta != 'c':
        # generamos prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior,limite_superior)
        else: 
            prediccion = limite_inferior
        respuesta = input(f'Mi prediccion es {prediccion}. ').lower()

        if respuesta == 'a':
            limite_superior =  prediccion -1
        elif respuesta == 'b':
            limite_inferior = prediccion + 1
    print('Felicitaciones, a acertado la pc con el numero : {prediccion}')  