


import random

cant_intentos = 0
cant_intentos_max = 5
nro_secreto= random.randint(0,100)

adivinado=False

print("Bienvenido al juego")
while not adivinado and cant_intentos<cant_intentos_max:
    numero_ingres= input("Introduce un nro del 0 al 99: ")
    numero_ingresado= int(numero_ingres)
    if  numero_ingresado==nro_secreto:
        numero_ingresado = True
        print("el nro es correcto")
    elif numero_ingresado>nro_secreto:
        print("el numero secreto es menor")
    else: 
        print("el nro secreto es mayor")

    cant_intentos+=1

if not cant_intentos<cant_intentos_max:
    print("Superaste la cantidad máxima de intentos")
