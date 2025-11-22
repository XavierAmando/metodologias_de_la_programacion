"""
squares=[]

for value in range(0,11)
    squares = value**2
    squares.append(square)
print(squares)
"""
"""
   una lista comprehention combina el ciclo for
   y la creacion de nuevos elemntos en ua sola
   linea y automaticamente agrega cada nuevo elemntos
   ala lista,es decir,sin utilizar el metodo append
"""
squares = [value**2 for value in range(0,11)]

# para generar los numeros pares entre el o y el 100

evens_range = [value for value in range(0,101,2)]

evens_if = [value for value in range(0,101) if value%2==0]
print(evens_if)
