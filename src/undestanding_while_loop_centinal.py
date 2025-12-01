"""
Docstring for understanding_while_loop_centinel

    un prgarama que:
        -cuente cuantos numers ingreso el usuario
        -Realice la suma de esos numeros
        -diga cual es el minimo de los numeris ingresados
        -diga cual es el maximo de los numeris ingresados
"""
counter =0
sum_cantidad=0.0
minimo= None
maximum=None

while True:
    print("Escribe exit para salir")
    user_input = input("Ingresa una cantidad (MXN): ")

    if user_input == "exit":
        break
    
    try:
        value = float(user_input)
    except ValueError:
        print("Caracter invalido. ingresa un numero")
        continue
    except KeyboardInterrupt:
        print("Salida del manual")
        break

    counter+=1  #counter = counter +1 (contador)

    sum_cantidad += value # sum_quantitiles = sum_quantitiles + value (sumador)

    if minimo is None or value < minimo :
        minimo = value


    if maximum is None or value > maximum :
        maximum = value


print("cantidad ingresada de numeros: ", counter)
print("suma de cantidades: ", sum_cantidad)
print("minimo de cantidades: ", maximum)
print("maximo de cantidades: ", minimo)