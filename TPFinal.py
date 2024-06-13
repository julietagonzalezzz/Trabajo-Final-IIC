contP = 0
contC = 0
ganancia = 0
while True:
    try:
        pieza = int(input("Ingresar número de pieza entre 1 y 99 inclusive o 0 para salir: "))
        if(pieza < 0 or pieza > 100):
            print('Ingresar un número de pieza válido por favor')
            continue
        if(pieza != 0):
            PT = 0
            print(f"Su número de pieza es: ", pieza)
            while True:
                comp = int(input(f"Ingresar número de componente, los ultimos 2 dígitos deben coincidir con el número de pieza {pieza}: "))
                if(comp < 10000):
                    if(comp == 0): 
                        break
                    if((comp%100) == pieza):
                        print("Componente Válido")
                        while True:
                            precio = float(input(f"Ingresar precio del componente {comp} entre $10.00 y $999.99: "))
                            if(10.00 <= precio <= 999.99):
                                break
                        print(f"Precio del componente {comp} es: ", precio)
                        PT = PT + precio
                        contP += 1
                    else:
                        print("El coóigo de la pieza es erróneo")
                        print("Ingrese un valor válido.")
                if((comp/100) < 1):
                    break
            ganancia = ganancia + PT
            print(f"El precio total de la pieza es: {PT}")
        else:
            break
    except: 
        print('Ingrese un valor válido por favor.')
print("Cantidad de piezas procesadas: ", contP)
print("La ganancia total es: ", ganancia)