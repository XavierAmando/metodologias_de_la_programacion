# bucles
# Xavier Armando Montoya Lerma
# 2530403
# 1-3

# RESUMEN EJECUTIVO
"""
 Un bucle for se usa para repetir acciones un número conocido de veces o para recorrer listas.
 El bucle while es más natural cuando la repetición depende de una condición que puede cambiar durante la ejecución.
 Un contador sirve para llevar cuántas veces pasa algo, y un acumulador para ir sumando valores progresivamente.
 Definir bien la condición de salida evita ciclos infinitos que pueden congelar el programa.
 Este documento incluirá la descripción de cada problema, las entradas y salidas esperadas,
 las validaciones necesarias y el uso adecuado de for y while en recorridos, menús
 y lectura repetida de datos según la situación del programa.


"""
# comentarios
"""
 NOTAS SOBRE EL USO DE BUCLES:
 Usar for cuando conoces de antemano cuántas iteraciones necesitas (por ejemplo, recorrer del 1 al 10).
 Usar while cuando la cantidad de repeticiones depende de una condición variable
 (como leer datos hasta que el usuario escriba "EXIT").
 Inicializar correctamente contadores y acumuladores antes de entrar al bucle.
 Actualizar siempre las variables de control dentro del while para evitar ciclos infinitos.
 Mantener el cuerpo de los bucles lo más simple posible; si la lógica es compleja,
 es mejor moverla a funciones para que el código sea más claro y fácil de mantener.

"""


# Problem 1: Sum of range with for

"""

Descripción:
Calcula la suma de todos los enteros desde 1 hasta n (incluyendo n). Además, calcula la suma solo de los números pares en ese mismo rango usando un bucle for.

Entradas:
- n (int; límite superior del rango).

Salidas:
- "Sum 1..n:" <total_sum>
- "Even sum 1..n:" <even_sum>

Validaciones:
- Verificar que n pueda convertirse a int.
- n >= 1; si no se cumple, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Uso de range(1, n + 1)
- Uso de un for con acumuladores para total_sum y even_sum.
"""
# solucion problema 1
try:
    n = int(input("Enter n: "))

    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0

        # Recorremos de 1 a n usando for
        for number in range(1, n + 1):
            total_sum += number

            if number % 2 == 0:
                even_sum += number

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)

except:
    print("Error: invalid input")

# caso de prueba
#  Caso Normal
"""
Entrada:

Enter n: 10


Proceso esperado:

Suma total: 1 + 2 + ... + 10 = 55

Suma pares: 2 + 4 + 6 + 8 + 10 = 30

Salida esperada:

Sum 1..n: 55
Even sum 1..n: 30
"""
#  Caso Borde límite mínimo válido
"""
Entrada:

Enter n: 1


Proceso esperado:

Suma total: 1

Suma pares: 0 (ningún número par)

Salida esperada:

Sum 1..n: 1
Even sum 1..n: 0
"""
# 3. Caso Error
"""
A) Número inválido (n < 1)

Entrada:

Enter n: 0


Salida esperada:

Error: invalid input

B) Formato inválido (cae en el except)

Entrada:

Enter n: hola


Salida esperada:

Error: invalid input

"""


# Problem 2: Multiplication table with for

""""
Descripción:
Genera y muestra la tabla de multiplicar de un número base, desde 1 hasta un límite m. Por ejemplo, si base = 5 y m = 4, muestra:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20

Entradas:
- base (int)
- m (int; límite de la tabla)

Salidas:
- Línea por cada multiplicación:
  - "5 x 1 = 5"
  - "5 x 2 = 10"
  - etc.

Validaciones:
- base y m convertibles a int.
- m >= 1; si no, "Error: invalid input".

Operaciones clave sugeridas:
- for i in range(1, m + 1):
- Cálculo de producto y formateo de la salida con f-strings.
"""
# solucion problema 2


try:
    base = int(input("Enter base: "))
    m = int(input("Enter limit m: "))

    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m + 1):
            product = base * i
            print(f"{base} x {i} = {product}")

except:
    print("Error: invalid input")

# casos de pruebas
# Caso Normal
"""
Entrada:

Enter base: 5
Enter limit m: 4


Salida esperada:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
"""
# Caso Borde (límite mínimo válido)
"""
Entrada:

Enter base: 7
Enter limit m: 1


Salida esperada:

7 x 1 = 7
"""
# Caso Error
"""
A) m inválido (menor que 1)

Entrada:

Enter base: 5
Enter limit m: 0


Salida esperada:

Error: invalid input

B) Formato inválido (cae en el except)

Entrada:

Enter base: hola
Enter limit m: 5


Salida esperada:

Error: invalid input
"""


# Problem 3: Average of numbers with while and sentinel

"""
Descripción:
Lee números uno por uno hasta que el usuario ingrese un valor sentinela (por ejemplo, -1). Calcula el promedio de los números válidos ingresados y la cantidad de números leídos. Si el usuario sólo ingresa el sentinela sin números válidos, muestra un mensaje de error.

Entradas:
- number (float; se lee repetidamente).
- sentinel_value (fijo en el código, por ejemplo: -1).

Salidas:
- "Count:" <count>
- "Average:" <average_value>
- Si no se ingresan datos válidos:
  - "Error: no data"

Validaciones:
- Cada lectura debe intentar convertirse a float.
- Ignorar el sentinela en los cálculos.

Operaciones clave sugeridas:
- while True con break al leer el sentinela o
- while number != sentinel_value
- Acumulador para suma y contador para cantidad.
"""
# solucion problema 3


sentinel_value = -1

total_sum = 0.0
count = 0

while True:
    user_input = input("Enter a number (-1 to stop): ")

    # Validación de conversión a float
    try:
        number = float(user_input)
    except ValueError:
        print("Error: invalid input")
        continue

    # Revisar sentinela
    if number == sentinel_value:
        break

    # Acumular valores válidos
    total_sum += number
    count += 1

# Verificar si hubo datos
if count == 0:
    print("Error: no data")
else:
    average_value = total_sum / count
    print("Count:", count)
    print("Average:", average_value)

# casos de pruebas 
# Caso normal
"""
Entrada:

10
5
3
-1


Proceso:

Suma: 10 + 5 + 3 = 18

Count = 3

Promedio = 18 / 3 = 6

Salida esperada:

Count: 3
Average: 6.0
"""
# Caso borde (solo un número válido antes del sentinela)
"""
Entrada:

8
-1


Salida esperada:

Count: 1
Average: 8.0
"""
# Caso error (no se ingresan datos válidos antes del sentinela)
""""
Entrada:

-1


Salida esperada:

Error: no data
"""
# Problem 4: Password attempts with while

"""
Descripción:
Implementa un sistema sencillo de intento de contraseña. Define en el código una contraseña correcta (por ejemplo, "admin123"). El usuario tiene un máximo de MAX_ATTEMPTS intentos para introducirla. Si acierta dentro del límite, mostrar un mensaje de éxito. Si agota los intentos, mostrar un mensaje de bloqueo.

Entradas:
- user_password (string; se lee en cada intento).

Salidas:
- Si acierta:
  - "Login success"
- Si falla todos los intentos:
  - "Account locked"

Validaciones:
- MAX_ATTEMPTS > 0 (definido como constante en el código, por ejemplo 3).
- Contar correctamente los intentos.

Operaciones clave sugeridas:
- while attempts < MAX_ATTEMPTS:
- Comparación de cadenas, contador de intentos.
- Opción de usar break al éxito.
"""
# solucion problema 4
CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
attempts = 0

while attempts < MAX_ATTEMPTS:
    user_pin = input("Por favor ingresa tu PIN: ")

    if user_pin == CORRECT_PIN:
        print("Acceso concedido. Bienvenido!")
        break
    else:
        attempts += 1
        remaining_attempts = MAX_ATTEMPTS - attempts

        if remaining_attempts > 0:
            print("Ingresa un PIN no válido")
            print(f"PIN incorrecto. Te quedan {remaining_attempts} intentos.")
        else:
            print("Cuenta bloqueada por demasiados intentos fallidos.")

# Caso normal (acierta antes de agotar):
"""
Intento 1: hola -> "Código mal, te faltan 2 intentos"
Intento 2: admin123 -> "Login success"
"""

# Caso borde (acierta en el último intento):
"""
Intento 1: 111 -> "Código mal, te faltan 2 intentos"
Intento 2: 222 -> "Código mal, te falta 1 intento"
Intento 3: admin123 -> "Login success"
"""

# Caso error (agota intentos):
"""
Intento 1: a -> "Código mal, te faltan 2 intentos"
Intento 2: b -> "Código mal, te falta 1 intento"
Intento 3: c -> (luego) "Account locked"
"""


# Problem 5: Simple menu with while
"""

Descripción:
Implementa un menú de texto que se repite hasta que el usuario seleccione la opción de salir. Ejemplo de menú:
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
El programa debe ejecutar la acción correspondiente a cada opción y volver a mostrar el menú hasta que se elija 0.

Entradas:
- option (string o int; elección del usuario).

Salidas:
- Mensajes según la opción:
  - "Hello!" para saludo.
  - "Counter:" <counter_value> para mostrar contador.
  - "Counter incremented" al incrementar.
  - "Bye!" al salir.
- Para opciones inválidas:
  - "Error: invalid option"

Validaciones:
- Normalizar option (por ejemplo, convertir a int con manejo de error).
- Asegurar que sólo 0,1,2,3 sean aceptadas como válidas.

Operaciones clave sugeridas:
- while option != 0:
- if/elif para cada opción.
- Variable counter inicializada fuera del bucle.
"""
# solucion problema 5
counter = 0

while True:
    print("------ MENU ------")
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")
    print("------------------")

    option_text = input("Choose an option: ").strip()

    # Validación: intentar convertir a int
    try:
        option = int(option_text)
    except:
        print("Error: invalid option\n")
        continue

    # Validar opción válida
    if option not in (0, 1, 2, 3):
        print("Error: invalid option\n")
        continue

    # Acciones del menú
    if option == 1:
        print("Hello!\n")
    elif option == 2:
        print(f"Counter: {counter}\n")
    elif option == 3:
        counter += 1
        print("Counter incremented\n")
    elif option == 0:
        print("Bye!")
        break

# CASOS DE PRUEBA
# Caso Normal
"""
Entrada simulada del usuario:

1
2
3
2
0


Salida esperada:

Hello!
Counter: 0
Counter incremented
Counter: 1
Bye!
"""
# Caso Borde (opción mínima y máxima válidas)
"""
Entrada:

3
3
3
0


Salida esperada:

Counter incremented
Counter incremented
Counter incremented
Bye!


(Caso borde porque solo usa los extremos: incrementa varias veces y luego sale.)
"""
# Caso Error (opciones inválidas y valores no numéricos)
"""
Entrada:

hola
9
-2
2
0


Salida esperada:

Error: invalid option
Error: invalid option
Error: invalid option
Counter: 0
Bye!
"""

# Problem 6: Pattern printing with nested loop
"""
Descripción:
Usa bucles for anidados para imprimir un patrón de asteriscos en forma de triángulo rectángulo. Por ejemplo, para n = 4:
*
**
***
****
Además, imprime un segundo patrón invertido (opcional si lo deseas extender, pero documenta tu decisión).

Entradas:
- n (int; número de filas del patrón).

Salidas:
- Patrón línea por línea:
  - "*"
  - "**"
  - "***"
  - "****"
- (Opcional) Patrón invertido si se implementa.

Validaciones:
- n convertible a int.
- n >= 1; si no, "Error: invalid input".

Operaciones clave sugeridas:
- for i in range(1, n + 1):
    - construir una cadena con i asteriscos usando "*" * i
- (Opcional) otro bucle for para el patrón invertido.
"""
# soLucion problema 6
try:
    n = int(input("Enter number of rows: "))

    if n < 1:
        print("Error: invalid input")
    else:
        # Patrón normal
        print("Normal pattern:")
        for i in range(1, n + 1):
            print("*" * i)

        # Patrón invertido (opcional)
        print("Inverted pattern (optional):")
        for i in range(n, 0, -1):
            print("*" * i)

except:
    print("Error: invalid input")

# casos de prueba (normal, borde y error)
#) Caso Normal
""""
Entrada:

4


Salida esperada:

Normal pattern:
*
**
***
****
Inverted pattern (optional):
****
***
**
*
"""
# Caso Borde
"""
Entrada:

1


Salida esperada:

Normal pattern:
*
Inverted pattern (optional):
*


(Borde porque n está en el mínimo permitido.)
"""
# Caso Error
"""
Entrada:

0


Salida esperada:

Error: invalid input


Otro error posible:

hola


Salida:

Error: invalid input
"""

# conclusiones
"""
 Los bucles for son ideales cuando ya sabes cuántas veces repetir algo,
 mientras que los while son más flexibles cuando dependes de una condición,
 como leer datos hasta un sentinela o manejar intentos de contraseña.
 Los contadores y acumuladores facilitaron llevar control de cantidades y sumas
 dentro de los bucles sin perder el orden. También noté que un while mal
 controlado puede producir ciclos infinitos si no se actualizan sus variables.
 Los menús interactivos y el sistema de intentos mostraron usos reales del while.
 Con los bucles anidados entendí mejor cómo construir patrones y controlar niveles
 de repetición dentro de otro ciclo.
"""

# REFERENCIAS
"""
1)https://elpythonista.com/bucles-en-python-for-y-while-guia-completa-2025-ejemplos
2)https://tutorial.recursospython.com/bucles/
3)https://youtu.be/abKLLfMn-pI?si=vokAU3wSdGk4P-Sz
4)apuntes de clases
5)https://youtu.be/roGiGK91kVs?si=v8Jx1tVdKfkdpkyK



"""
# repo 
"""

https://github.com/XavierAmando/metodologias_de_la_programacion.git

"""
