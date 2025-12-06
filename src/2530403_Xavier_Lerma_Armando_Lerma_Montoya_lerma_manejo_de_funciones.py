# manejo de funciones

# Xavier Armando Montoya Lerma
# 2530403
# Grupo IM 103
# RESUMEN EJECUTIVO
""" 
 Las funciones en Python son bloques de código reutilizables que permiten organizar mejor un programa.
 Sirven para evitar repetir instrucciones y para dividir un problema grande en partes más pequeñas y claras.
 Los parámetros aparecen en la definición de la función y son los nombres que recibirán los datos.
 Los argumentos aparecen en la llamada de la función y son los valores reales que se envían a esos parámetros.
 Es útil separar la lógica en funciones porque hace el código más fácil de leer, mantener y probar.
 Además, permite reutilizar la misma lógica en distintas partes del programa sin duplicarla.
 Un valor de retorno es el resultado que la función envía de vuelta mediante la instrucción return.
 Devolver valores es mejor que solo imprimirlos porque permite usarlos en cálculos u otras funciones.
 También facilita las pruebas y hace que la función sea más flexible, ya que no depende de mostrar texto en pantalla.
"""
# buenas practicas
"""
 Es buena práctica crear funciones pequeñas que realicen una sola tarea (single responsibility).
 Cuando notes que estás copiando y pegando código, considera convertir esa lógica repetida en una función.
 Siempre que sea posible, intenta que tus funciones sean “puras”: mismo input, mismo output y sin efectos secundarios.
 Añade comentarios breves que expliquen qué hace cada función y qué parámetros recibe.
 Usa nombres claros y descriptivos para tus funciones, como calculate_bmi, en lugar de nombres vagos como f1 o do_it.
 Es buena práctica crear funciones pequeñas que realicen una sola tarea (single responsibility).
 Cuando notes que estás copiando y pegando código, considera convertir esa lógica repetida en una función.
 Siempre que sea posible, intenta que tus funciones sean “puras”: mismo input, mismo output y sin efectos secundarios.
 Añade comentarios breves que expliquen qué hace cada función y qué parámetros recibe.
 Usa nombres claros y descriptivos para tus funciones, como calculate_bmi, en lugar de nombres vagos como f1 o do_it
 .
 """

# Problem 1: Rectangle area and perimeter (basic functions)

"""
Descripción:
Define dos funciones:
- calculate_area(width, height): regresa el área de un rectángulo.
- calculate_perimeter(width, height): regresa el perímetro.
El código principal debe leer (o definir) los valores, llamar a las funciones y mostrar los resultados.

Entradas:
- width (float)
- height (float)

Salidas:
- "Area:" <area_value>
- "Perimeter:" <perimeter_value>

Validaciones:
- width > 0
- height > 0
- Si alguna condición no se cumple, mostrar "Error: invalid input" y no llamar a las funciones.

Operaciones clave sugeridas:
- area = width * height
- perimeter = 2 * (width + height)
"""

def calculate_area(width, height):
    """
    Funcion que calcula el area de un rectangulo
    """
    area = width * height
    return area
def calculate_perimeter(width, height):
    """
    Funcion que calcula el perimetro de un rectangulo
    """
    perimeter = 2 * (width + height)
    return perimeter
# Codigo principal
try:
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    if width <= 0 or height <= 0:
        print("Error: invalid input")
    else:
        area_value = calculate_area(width, height)
        perimeter_value = calculate_perimeter(width, height)

        print("Area:", area_value)
        print("Perimeter:", perimeter_value)
except:
    print("Error: invalid input")


# CASOS DE PRUEBA

#Caso normal:
"""
Entrada: width = 5.0, height = 3.0
Resultado esperado:
Area = 15.0
Perimeter = 16.0
"""
# Caso borde:
"""
Entrada: width = 0.0001, height = 10.0
Resultado esperado:
Area = 0.001
Perimeter = 20.0002
(Ambos valores deben pasar validación porque son > 0)
"""
# Caso error:
"""
Entrada: width = -4, height = 7
Resultado esperado:
 Mensaje: "Error: invalid input"
(No se deben calcular área ni perímetro)
"""



# Problem 2: Grade classifier (function with return string)
"""

Descripción:
Define una función classify_grade(score) que reciba una calificación numérica (0–100) y regrese una categoría:
- "A" si score >= 90
- "B" si 80 <= score < 90
- "C" si 70 <= score < 80
- "D" si 60 <= score < 70
- "F" si score < 60
El código principal debe llamar la función y mostrar el resultado.

Entradas:
- score (float o int)

Salidas:
- "Score:" <score>
- "Category:" <grade_letter>

Validaciones:
- 0 <= score <= 100
- Si no se cumple, mostrar "Error: invalid input" y no clasificar.

Operaciones clave sugeridas:
- if/elif para rangos.
- Función con un único return al final o varios returns (pero bien documentados).
"""
def classify_grade(score):
    """
    Funcion que clasifica la calificacion en letras
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
# Codigo principal
try:
    score = float(input("Enter score: "))

    if score < 0 or score > 100:
        print("Error: invalid input")
    else:
        grade_letter = classify_grade(score)
        print("Score:", score)
        print("Category:", grade_letter)
except:
    print("Error: invalid input")

# CASOS DE PRUEBA


# Caso normal:
"""
Entrada: score = 85
Resultado esperado:
Category = "B"
"""
# Caso borde:
"""
Entrada: score = 90
Resultado esperado:
Category = "A"
(Exactamente en el límite superior de la categoría A)
"""
# Caso error:
"""
Entrada: score = 120
Resultado esperado:
Mensaje: "Error: invalid input"
(No debe clasificar la calificación)
"""



# Problem 3: List statistics function (min, max, average)

"""
Descripción:
Define una función summarize_numbers(numbers_list) que reciba una lista de números y regrese un diccionario con:
- "min": mínimo
- "max": máximo
- "average": promedio (float)
El código principal debe construir la lista (por ejemplo, a partir de texto separado por comas), llamar la función y mostrar los valores.

Entradas:
- numbers_text (string; por ejemplo, "10,20,30")
- Internamente: numbers_list (list of float o int)

Salidas:
- "Min:" <min_value>
- "Max:" <max_value>
- "Average:" <average_value>

Validaciones:
- numbers_text no vacío tras strip().
- Lista no vacía después de la conversión.
- Todos los elementos deben poder convertirse a números; si alguno falla, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- split() para construir la lista de strings.
- Conversión a float o int dentro de un ciclo.
- sum(), len(), min(), max() dentro de summarize_numbers().
"""
def summarize_numbers(numbers_list):
    """
    Funcion que resume una lista de numeros
    """
    min_value = min(numbers_list)
    max_value = max(numbers_list)
    average_value = sum(numbers_list) / len(numbers_list)
    return {
        "min": min_value,
        "max": max_value,
        "average": average_value
    }
# Codigo principal
numbers_text = input("Enter numbers (comma separated): ")
if not numbers_text.strip():
    print("Error: invalid input")
    exit()
try:
    numbers_list = [float(num.strip()) for num in numbers_text.split(",")]
    if not numbers_list:
        print("Error: invalid input")
    else:
        summary = summarize_numbers(numbers_list)
        print("Min:", summary["min"])
        print("Max:", summary["max"])
        print("Average:", summary["average"])
except:
    print("Error: invalid input")


# CASOS DE PRUEBA

# Caso normal:
"""
Entrada: "3, 7, 10"
Resultado esperado:
Min = 3
Max = 10
Average = 6.666...
"""
# Caso borde:
"""
Entrada: "5"
Resultado esperado:
Min = 5
Max = 5
Average = 5
(Lista con un solo número, válido)
"""
# Caso error:
"""
Entrada: ""
Resultado esperado:
Mensaje: "Error: invalid input"
(No debe intentar convertir la lista)
"""


# Problem 4: Apply discount list (pure function)

"""
Descripción:
Define una función apply_discount(prices_list, discount_rate) que:
- reciba una lista de precios (float) y una tasa de descuento (por ejemplo, 0.10 para 10%)
- regrese una nueva lista con los precios ya descontados (no modificar la lista original).
El código principal debe:
- Crear una lista de precios.
- Llamar a la función.
- Mostrar la lista original y la nueva lista con descuento.

Entradas:
- prices_text (string; por ejemplo, "100,200,300")
- discount_rate (float, entre 0 y 1)

Salidas:
- "Original prices:" <original_list>
- "Discounted prices:" <discounted_list>

Validaciones:
- prices_text no vacío y lista resultante no vacía.
- Todos los precios > 0.
- 0 <= discount_rate <= 1; si no, "Error: invalid input".

Operaciones clave sugeridas:
- Construir la lista de float desde texto.
- En la función, usar un ciclo para crear una nueva lista:
  - discounted_price = price * (1 - discount_rate)
- No modificar la lista de entrada (pure function).
"""    
def apply_discount(prices_list, discount_rate):
    """
    Funcion que aplica un descuento a una lista de precios
    """
    discounted_list = []
    for price in prices_list:
        discounted_price = price * (1 - discount_rate)
        discounted_list.append(discounted_price)
    return discounted_list
# Codigo principal
prices_text = input("Enter prices (comma separated): ")
discount_rate_input = input("Enter discount rate (0-1): ")
if not prices_text.strip():
    print("Error: invalid input")
    exit()
try:
    prices_list = [float(price.strip()) for price in prices_text.split(",")]
    discount_rate = float(discount_rate_input)

    if not prices_list or any(price <= 0 for price in prices_list) or discount_rate < 0 or discount_rate > 1:
        print("Error: invalid input")
    else:
        discounted_list = apply_discount(prices_list, discount_rate)
        print("Original prices:", prices_list)
        print("Discounted prices:", discounted_list)
except:
    print("Error: invalid input")

# CASOS DE PRUEBA

# Caso normal:
"""
Entrada:
prices_list = "100, 200, 50"
discount_rate = "0.2"
Resultado esperado:
Original prices = [100.0, 200.0, 50.0]
Discounted prices = [80.0, 160.0, 40.0]
"""

# Caso borde:
"""
Entrada:
prices_list = "1"
discount_rate = "0"
Resultado esperado:
Original prices = [1.0]
Discounted prices = [1.0]
(Caso límite con un solo precio y sin descuento)
"""

# Caso error:
"""
Entrada:
prices_list = "-5, 10"
discount_rate = "0.3"
Resultado esperado:
Mensaje: "Error: invalid input"
(No debe calcular descuentos porque hay un precio negativo)
"""


# Problem 5: Greeting function with default parameters

""""
Descripción:
Define una función greet(name, title="") que:
- Concatene opcionalmente el título antes del nombre (por ejemplo, "Dr. Alice", "Eng. Bob").
- Regrese el mensaje: "Hello, <full_name>!"
Si title está vacío, solo usar el nombre. El código principal debe llamar a la función usando argumentos posicionales y nombrados.

Entradas:
- name (string)
- title (string opcional)

Salidas:
- "Greeting:" <greeting_message>

Validaciones:
- name no vacío tras strip().
- title puede estar vacío, pero si no lo está, también se normaliza con strip().

Operaciones clave sugeridas:
- Uso de parámetros con valor por defecto: def greet(name, title=""):
- Uso de argumentos nombrados: greet(name="Alice", title="Dr.")
"""
def greet(name, title=""):
    """
    Funcion que saluda a una persona con un titulo opcional
    """
    if title.strip():
        full_name = f"{title.strip()} {name.strip()}"
    else:
        full_name = name.strip()
    return f"Hello, {full_name}!"
# Codigo principal
name = input("Enter name: ")
title = input("Enter title (optional): ")
if not name.strip():
    print("Error: invalid input")
else:
    greeting_message = greet(name, title)
    print("Greeting:", greeting_message)

# CASOS DE PRUEBA

# Caso normal:
"""
Entrada:
name = "Alice"
title = "Dr."
Resultado esperado:
Greeting: "Hello, Dr. Alice!"
"""

# Caso borde:
"""
Entrada:
name = "Bob"
title = ""
Resultado esperado:
Greeting: "Hello, Bob!"
(Caso límite: no se proporciona título)
"""

# Caso error:
"""
Entrada:
name = ""
title = "Engineer"
Resultado esperado:
Mensaje: "Error: invalid input"
(No debe generar saludo si el nombre está vacío)
"""


# Problem 6: Factorial function (iterative or recursive)
"""
Descripción:
Define una función factorial(n) que regrese n! (n factorial). Puedes implementarla de forma iterativa (con for) o recursiva, pero debes documentar tu elección en comentarios. El código principal debe:
- Leer/definir n.
- Validar n.
- Llamar a factorial(n).
- Mostrar el resultado.

Entradas:
- n (int)

Salidas:
- "n:" <n>
- "Factorial:" <factorial_value>

Validaciones:
- n entero.
- n >= 0.
- Opcional: limitar n a un máximo razonable (por ejemplo n <= 20) para evitar números demasiado grandes; si no se cumple, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Versión iterativa:
  - result = 1
  - for i in range(1, n + 1): result *= i
- Versión recursiva (opcional):
  - factorial(0) = 1
  - factorial(n) = n * factorial(n - 1)
"""
def factorial(n):
    """
    Funcion que calcula el factorial de un numero de forma iterativa
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# Codigo principal
try:
    n = int(input("Enter n: "))

    if n < 0 or n > 20:
        print("Error: invalid input")
    else:
        factorial_value = factorial(n)
        print("n:", n)
        print("Factorial:", factorial_value)
except:
    print("Error: invalid input")

# CASOS DE PRUEBA

# Caso normal:
"""
Entrada:
n = 5
Resultado esperado:
Factorial = 120
"""

# Caso borde:
"""
Entrada:
n = 0
Resultado esperado:
Factorial = 1
(Caso límite: el factorial de 0 es 1)
"""

# Caso error:
"""
Entrada:
n = -3
Resultado esperado:
Mensaje: "Error: invalid input"
(No debe calcular factorial de números negativos)
"""


# conclusion
"""
 Las funciones me ayudaron a organizar mejor el programa y a reutilizar código sin repetirlo en varios lugares.
 Aprendí que usar return es más útil que imprimir, porque así puedo guardar el resultado y usarlo en otros cálculos.
 También vi que los parámetros y los valores por defecto hacen que la función sea más flexible y fácil de adaptar.
 Encapsular lógica en funciones fue muy cómodo en cálculos repetidos, validaciones y tareas que se usan muchas veces.
 Entendí la diferencia entre la lógica principal del programa y las funciones de apoyo que realizan tareas específicas.
 Esto hace que el programa sea más claro, más modular y más sencillo de mantener o modificar.
"""

# referencias
"""
https://youtu.be/9k91jETchkI?si=zAJ-Bg4w-8G-NjoR
https://youtu.be/hLRoDs4wNCU?si=HrUtaeuAVjfNSKJ7
apuntes de clases
https://elpythonista.com/funciones-en-python-guia-completa-2025-sintaxis-parametros-y-ejemplos
https://imaginaformacion.com/tutoriales/funciones-en-python
"""

#Repositorio
"""
https://github.com/XavierAmando/metodologias_de_la_programacion.git
"""
