"""
las listas tambien pueden almacenar numeros y de hecho, son ideales para 
esto.
python ofrece una gran cantidad de herramientas que ayudan a trabajar eficientamente
listas de numeros.
"""
# metodo bult-in range()
"""
e metodo range() nos ayuda a crear facilmente
series de numeros
ejemplo
"""
print("numeros del 0 y 9")
for value in range(10): #10 numeros entre 0-9
    print (value)
print("numeros del 1-9")    
for value in range(1,10): # 10 numeros entre 1-9    
    print (value)


print("numeros impares del 1 al 9")
for value in range(1,10,2): # 10 numero entre 1-9
    print(value)
    
odd_numbers = list(range(1,10,2))
print(odd_numbers)



print("numeros pares1 al 9")
for value in range(0,10,2): # 10 numero entre 1-9
    print(value)
even_numbers = list(range(0,10,2))
print(even_numbers)

print("tabla del 9")
for value in range(0,91,9): # 10 numero entre 1-9
    print(value)

tabla_del_9 = list(range(0,91,9))
print(tabla_del_9)

# cuadrados de los primeros 10 numeros
squares = [] 
for number in range(1,11) :
    square = number**2
    squares.append(square)
print(squares)

## mas metodos built-in 
# metodos min ()
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))# salida 9

# metdo max()
digits = [1,2,3,4,5,6,7,8,9,0]
print(max(digits))# salida 9

# metodomsum()
digits = [1,2,3,4,5,6,7,8,9,0]
print(sum(digits))# salida:45