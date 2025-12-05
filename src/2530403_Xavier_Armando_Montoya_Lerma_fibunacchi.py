# Xavier Armando. Montoya Lerma
# 2530403
# 1-3








"""
  
Antes del código, agrega algo como (en comentarios):

Problem: Fibonacci series generator  
Description: Program that reads an integer n and prints the first n terms of the Fibonacci series starting at 0 and 1.  

Inputs:  
- n (int; number of terms to generate)  

Outputs:  
- "Fibonacci series:" followed by the n terms separated by spaces or commas  

Validations:  
- n must be an integer  
- n must be >= 1  
- (Optional) n must be <= 50  

Test cases:  
1) Normal: n = ... → expected series: ...  
2) Border: n = ... → expected series: ...  
3) Error: n = ... → expected message: "Error: invalid input"

"""
# La serie de Fibonacci es una secuencia donde cada número
#  es la suma de los dos anteriores (0, 1, 1, 2, 3, 5...).
# “Calcular la serie hasta n términos” significa generar 
# exactamente n valores empezando desde 0 y 1.

# Este programa leerá el valor de n, verificará que sea un 
# entero válido y dentro del rango permitido.
# Si la validación se cumple, generará la serie de Fibonacci
#  usando un ciclo y mostrará los n términos en pantalla.

# Programa: Serie de Fibonacci con validaciones

user_input = input("Enter number of terms: ")


try:
    n = int(user_input)
except ValueError:
    print("Error: invalid input")
    exit()

if n < 1:
    print("Error: invalid input")
    exit()


if n > 50:
    print("Error: invalid input")
    exit()

fib = []

if n >= 1:
    fib.append(0)
if n >= 2:
    fib.append(1)

for i in range(2, n):
    siguiente = fib[-1] + fib[-2]
    fib.append(siguiente)


print("Fibonacci series:", " ".join(str(num) for num in fib))


# Caso Normal
"""
Entrada:

Enter number of terms: 7


Proceso esperado:

7 es entero ✔

7 ≥ 1 ✔

7 ≤ 50 ✔

Genera los primeros 7 términos: 0, 1, 1, 2, 3, 5, 8

Salida esperada:

[0, 1, 1, 2, 3, 5, 8]


(o como decidas imprimir la lista)
"""
# Caso Borde (mínimo válido)
"""
Entrada:

Enter number of terms: 1


Proceso esperado:

1 es entero ✔

Es el valor mínimo permitido ✔

Solo debe devolver el primer término

Salida esperada:

[0]
"""
 # Caso Error (entrada no válida)
"""
Entrada:

Enter number of terms: hola


Proceso esperado:

No se puede convertir a entero ❌

Salida esperada:

Error: invalid input

"""


#CONCLUSION

# El uso de un bucle facilitó generar la serie porque permitió construir
# cada término a partir de los anteriores.

# Manejar correctamente los casos n = 1 y n = 2 es importante para evitar
# errores y asegurar que la serie inicie correctamente.

# Esta lógica puede reutilizarse en otros programas que necesiten cálculos
# secuenciales, acumulativos o basados en valores previos.

# Además, sirve como base para funciones matemáticas, algoritmos de 
# optimización o simulaciones que dependan de iteraciones controladas.

# References:
# 1) Python Documentation – "for" and "while" Statements: https://docs.python.org/3/tutorial/controlflow.html
# 2) Python Fibonacci Tutorials – Real Python / W3Schools: explicación de listas y generación de secuencias.
# 3) Apuntes de clase de Programación (Unidad: Estructuras de control y ciclos).