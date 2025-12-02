# MANEJO DE LSITAS,TUPLAS Y DICCIONARIOS 

# Xavier Armando Montoya Lerma
# 2530403
# Grupo IM 1-3

# RESUMEN EJECUTIVO
## ¿Qué es una lista, una tupla y un diccionario en Python y en qué se diferencian?
""""
lista
Una lista en Python es una estructura de datos muy versátil que permite almacenar una colección ordenada de elementos. Estas son algunas de sus características principales:

Ordenada: Los elementos tienen un orden definido, lo que significa que puedes acceder a ellos mediante su índice (empezando desde 0).
Mutable: Puedes modificarla después de su creación, añadiendo, eliminando o cambiando elementos.
Heterogénea: Puede contener diferentes tipos de datos, como números, cadenas, booleanos, e incluso otras listas.
Permite duplicados: Los elementos repetidos son válidos dentro de una lista.
tupla
Una tupla en Python es una estructura de datos que permite almacenar una colección de elementos ordenados e inmutables. Esto significa que, una vez creada, no se pueden modificar, añadir ni eliminar elementos de la tupla. Se definen utilizando paréntesis () o la función tuple() y pueden contener elementos de diferentes tipos, como enteros, cadenas, flotantes, entre otros.

Características principales de las tuplas:
Ordenadas: Los elementos tienen un orden fijo y se pueden acceder mediante índices.
Inmutables: No se pueden cambiar después de su creación.
Heterogéneas: Pueden contener elementos de diferentes tipos.
Eficientes: Son más rápidas que las listas para ciertas operaciones debido a su inmutabilidad.
diccionario
Un diccionario en Python es una estructura de datos que permite almacenar información en forma de pares clave-valor. Es una colección no ordenada, donde cada clave (key) es única e inmutable, mientras que los valores (value) pueden ser de cualquier tipo y modificables.

Características principales:
Claves únicas: No puede haber claves duplicadas en un diccionario.
Acceso rápido: Puedes acceder a los valores directamente usando sus claves.
Sintaxis: Se definen usando llaves {} y los pares clave-valor se separan con dos puntos
¿En qué se diferencian?
sus diferencias radican principalmente en su mutabilidad, orden y estructura:
Mutabilidad: Las listas son mutables (pueden cambiar), las tuplas son inmutables (no pueden cambiar) y los diccionarios son mutables.
Orden: Las listas y tuplas son ordenadas (los elementos tienen un orden fijo), mientras que los diccionarios son no ordenados (aunque en versiones recientes de Python mantienen el orden de inserción).
Estructura: Las listas y tuplas almacenan elementos individuales, mientras que los diccionarios almacenan pares clave-valor.

"""
# RECOMENDACIONES IMPORTANTES:
# - Usa listas cuando necesites agregar o eliminar elementos con frecuencia.
# - Usa tuplas para datos que no deben cambiar (coordenadas, fechas, configuraciones fijas).
# - Usa diccionarios cuando necesites buscar información por una clave (nombre, id, código).
# - Evita modificar una lista mientras la recorres con un for, a menos que sepas muy bien lo que haces.
# - Usa nombres de claves descriptivos en diccionarios ("name", "age", "price").
# - Escribe código legible y mensajes claros para el usuario.

# resumen ejecutivo




# problema 1
"""
Descripción:
Trabaja con una lista de productos (strings) y sus cantidades (enteros). El programa debe:
1) Crear una lista inicial de productos.
2) Permitir agregar un nuevo producto al final.
3) Mostrar la cantidad total de elementos en la lista.
4) Verificar si un producto específico está en la lista (booleano is_in_list).

Entradas:
- initial_items_text (string; por ejemplo, "apple,banana,orange").
- new_item (string; producto a agregar).
- search_item (string; producto a buscar).

Salidas:
- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false


Validaciones:
- initial_items_text no vacío tras strip().
- Separar la cadena por comas y eliminar espacios extra en cada elemento.
- new_item y search_item no vacíos.
- Manejar el caso de lista inicial vacía si el estudiante lo decide (documentar decisión).

"""

# Solución al problema 1
initial_items_text = "apple, banana, pera"
new_item = "grape"
search_item = "banana"
if not initial_items_text.strip():
    print("Error: initial_items_text no puede estar vacío.")
else:
    items_list = [item.strip() for item in initial_items_text.split(",") if item.strip()]

    
    if not new_item.strip():
        print("Error: new_item no puede estar vacío.")
    else:
        
        if not search_item.strip():
            print("Error: search_item no puede estar vacío.")
        else:
            
            items_list.append(new_item.strip())
            len_list = len(items_list)
            is_in_list = search_item.strip() in items_list

            print("Items list:", items_list)
            print("Total items:", len_list)
            print("Found item:", is_in_list)


# casos de preubas
# el que ya sale bien ya esta puesto
#caso de prueba 2 con el texto vacio 
"""
initial_items_text = "    "
new_item = "mango"
search_item = "mango"

y sale
Error: initial_items_text no puede estar vacío.
Items list: []      # queda vacío
# No mostrará más impresiones porque no pasa la validación final

"""
# caso 3 con el search error
"""
initial_items_text = "manzana, uva"
new_item = "pera"
search_item = "   "

Error: search_item no puede estar vacío.

"""


# problema 2
"""
Descripción:
Usa tuplas para representar dos puntos en un plano 2D: (x1, y1) y (x2, y2). El programa debe:
1) Crear dos tuplas point_a y point_b a partir de entradas numéricas.
2) Calcular la distancia euclidiana entre ambos puntos.
3) Crear una nueva tupla midpoint con el punto medio entre ellos.

Entradas:
- x1, y1, x2, y2 (float; coordenadas de los puntos).

Salidas:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)

Validaciones:
- Verificar que las 4 entradas se puedan convertir a float.
- No se requieren restricciones adicionales en el rango.
"""

# Solución al problema 2

plano = ((2.0, 3.0), (5.0, 7.0))  # punto A y punto B


if len(plano) != 2:
    print("Error: el plano debe tener exactamente dos puntos.")
else:
    point_a = plano[0]
    point_b = plano[1]


    if len(point_a) != 2 or len(point_b) != 2:
        print("Error: cada punto debe tener coordenadas (x, y).")
    else:
        x1, y1 = point_a
        x2, y2 = point_b

        distance = (x2 - x1) ** 2 + (y2 - y1) ** 2

    
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        midpoint = (mx, my)

        print("Point A:", point_a)
        print("Point B:", point_b)
        print("Distance:", distance)
        print("Midpoint:", midpoint)



## casos de pruebas
# caso de prueba 1 normañ
""""
plano = ((2.0, 3.0), (5.0, 7.0))
Point A: (2.0, 3.0)
Point B: (5.0, 7.0)
Distance: 25
Midpoint: (3.5, 5.0)




"""
# caso 2 distancia igal a cero
""""

plano = ((4.0, 4.0), (4.0, 4.0))
Point A: (4.0, 4.0)
Point B: (4.0, 4.0)


Distance: 0


Midpoint: (4.0, 4.0)
"""
# caso 3 puntos con negativos
"""
plano = ((-3.0, 2.0), (4.0, -1.0))



Point A: (-3.0, 2.0)
Point B: (4.0, -1.0)
Distance: 58
Midpoint: (0.5, 0.5)


"""


# problema 3
"""
Descripción:
Administra un pequeño catálogo de productos usando un diccionario donde:
- clave: nombre del producto (string)
- valor: precio unitario (float)
El programa debe:
1) Crear un diccionario inicial con al menos 3 productos.
2) Leer el nombre de un producto y la cantidad a comprar.
3) Calcular el total a pagar si el producto existe.
4) Si el producto no existe, mostrar un mensaje de error.

Entradas:
- product_name (string).
- quantity (int; cantidad a comprar).

Salidas:
- Si el producto existe:
  - "Unit price:" <unit_price>
  - "Quantity:" <quantity>
  - "Total:" <total_price>
- Si el producto no existe:
  - "Error: product not found"

Validaciones:
- quantity > 0.
- product_name no vacío tras strip().
- Verificar si product_name está en el diccionario (clave).

Operaciones clave sugeridas:
- Definir dict literal: product_prices = {"apple": 10.0, ...}
- in para verificar existencia de clave.
- Acceso: unit_price = product_prices[product_name]

"""

# Solución al problema 3
product_prices = {
    "apple": 10.0,
    "strawberry": 5.0,
    "orange": 8.0
}   
product_name = "strawberry"
quantity = 3
if quantity <= 0:
    print("Error: quantity debe ser mayor que 0.")
elif not product_name.strip():
    print("Error: no puede estar vacío.")
else:
    if product_name.strip() in product_prices:
        unit_price = product_prices[product_name.strip()]
        total_price = unit_price * quantity
        print("Unit price:", unit_price)
        print("Quantity:", quantity)
        print("Total:", total_price)
    else:
        print("Error")

# caso de pruebas
# caso 1 producto normal
"""
product_name = "strawberry"
quantity = 3
Unit price: 5.0


Quantity: 3
Total: 15.0



"""
# caso de prueba 2 producto no existe
"""
product_name = "mango"
quantity = 2

Error




"""
# caso de prueba 3 quntity invalido
"""
product_name = "apple"
quantity = 0


Error: quantity debe ser mayor que 0.




"""


# problema 4
"""
Descripción:
Administra las calificaciones de un grupo usando un diccionario:
- clave: nombre del estudiante (string)
- valor: lista de calificaciones (list of float)
El programa debe:
1) Crear un diccionario con al menos 3 estudiantes, cada uno con una lista de calificaciones.
2) Leer el nombre de un estudiante.
3) Calcular el promedio de sus calificaciones.
4) Indicar si el estudiante está aprobado (average >= 70.0) con un booleano is_passed.

Entradas:
- student_name (string).

Salidas:
- Si el estudiante existe:
  - "Grades:" <grades_list>
  - "Average:" <average>
  - "Passed:" true|false
- Si el estudiante no existe:
  - "Error: student not found"

Validaciones:
- student_name no vacío tras strip().
- Verificar si student_name es una clave en el diccionario.
- Verificar que la lista de calificaciones no esté vacía antes de calcular el promedio.

Operaciones clave sugeridas:
- Diccionario de listas: grades = {"Alice": [90, 85], ...}
- sum(), len() para promedio.
- in para verificar clave.

"""
# Solución al problema 4
student_grades = {
    "Xavier": [85.0, 90.0, 78.0],
    "Alexis vega": [65.0, 70.0, 72.0],
    "Cristiano": [95.0, 88.0, 92.0]
}
student_name = "Xavier"
if not student_name.strip():
    print("Error: no puede estar vacío.")
else:
    if student_name.strip() in student_grades:
        grades_list = student_grades[student_name.strip()]
        if len(grades_list) == 0:
            print("Error: la lista de calificaciones está vacía.")
        else:
            average = sum(grades_list) / len(grades_list)
            is_passed = average >= 70.0
            print("Grades:", grades_list)
  
            print("Average:", average)
            print("Passed:", is_passed)
    else:
        print("Error: student not found")


# casos de pruebas
# caso de p

# problema 5
"""
Descripción:
Cuenta la frecuencia de cada palabra en una oración usando:
- Una lista de palabras.
- Un diccionario donde:
  - clave: palabra (string)
  - valor: frecuencia (int)
El programa debe:
1) Leer una oración.
2) Convertirla a minúsculas y separarla en una lista de palabras.
3) Construir un diccionario de frecuencias.
4) Mostrar el diccionario completo y la palabra más frecuente.

Entradas:
- sentence (string).

Salidas:
- "Words list:" <words_list>
- "Frequencies:" <freq_dict>
- "Most common word:" <word> (si hay empate, cualquier una es válida)

Validaciones:
- sentence no vacía tras strip().
- Manejar signos de puntuación simples si el estudiante decide hacerlo (documentar su decisión, por ejemplo usando replace()).
- Verificar que la lista de palabras no esté vacía.
"""
# Solución al problema 5
sentence = "Real madrid uwu es el mejor equipo de futbol xd xd xd xd xd"
if not sentence.strip():
    print("Error: sentence no puede estar vacío.")
else:
    words_list = sentence.lower().split()
    if len(words_list) == 0:
        print("Error: la lista de palabras está vacía.")
    else:
        freq_dict = {}
        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
        most_common_word = max(freq_dict, key=freq_dict.get)
        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)

# problema 6
"""

Descripción:
Implementa un mini "contact book" usando un diccionario donde:
- clave: nombre de contacto (string)
- valor: número de teléfono (string)
El programa debe:
1) Crear un diccionario inicial con algunos contactos.
2) Leer una acción action_text ("ADD", "SEARCH" o "DELETE").
3) Según la acción:
   - "ADD": lee name y phone, agrega o actualiza el contacto.
   - "SEARCH": lee name y muestra el teléfono si existe.
   - "DELETE": lee name y elimina el contacto si existe.
4) Mostrar un mensaje indicando el resultado de la operación.

Entradas:
- action_text (string; "ADD", "SEARCH" o "DELETE").
- name (string; depende de la acción).
- phone (string; solo para "ADD").

Salidas:
- Para "ADD":
  - "Contact saved:" name, phone
- Para "SEARCH":
  - Si existe: "Phone:" <phone>
  - Si no existe: "Error: contact not found"
- Para "DELETE":
  - Si existe: "Contact deleted:" name
  - Si no existe: "Error: contact not found"

Validaciones:
- Normalizar action_text a mayúsculas.
- Verificar que action_text sea una de las tres opciones válidas.
- name no vacío tras strip().
- Para "ADD": phone no vacío tras strip().

Operaciones clave sugeridas:
- Diccionario: contacts = {"Alice": "1234567890", ...}
- get(), in, pop()
- Estructura if/elif para manejar cada acción.
"""

# Solución al problema 6
contacts = {
    "Xavier": "555-1234",
    "Alexis vega": "555-5678",
    "Cristiano": "555-8765"
}
action_text = "ADD"
name = "Lionel"
phone = "555-4321"
action = action_text.strip().upper()
if action not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: acción no válida.")
elif not name.strip():
    print("Error: name no puede estar vacío.")
else:
    if action == "ADD":
        if not phone.strip():
            print("Error: no puede estar vacío.")
        else:
            contacts[name.strip()] = phone.strip()
            print("Contact saved:", name.strip(), phone.strip())
    elif action == "SEARCH":
        if name.strip() in contacts:
            print("Phone:", contacts[name.strip()])
        else:
            print("Error: contact not found")
    elif action == "DELETE":
        if name.strip() in contacts:
            contacts.pop(name.strip())
            print("Contact deleted:", name.strip())
        else:
            print("Error: contact not found")


# casos de prueba
"""
tendremos que cambiar el texto para hacer que cambie lo que imprime

"""
action_text = "SEARCH"
name = "Cristiano"
phone = ""
# es en caso de de usar el search
" y imprime Phone: 555-8765"
# ahora en caso de deleted o contacto inexistente
action_text = "DELETE"
name = "Neymar"
phone = ""
# imprime
"Error: contact not found"



# referencias
"""
use los apuntes de la clase 
https://youtu.be/w53HiWSZnzU?si=53OMyzkkSTNmUsQy
https://pythonaplicado.com/leer/capitulo-6/tuplas-listas-y-diccionarios
https://youtu.be/PogXFDqR770?si=aKEYox0UqZ3t_R2Q
https://youtu.be/numQzIgpOo0?si=52c8-Dt22t-s6x5j




"""