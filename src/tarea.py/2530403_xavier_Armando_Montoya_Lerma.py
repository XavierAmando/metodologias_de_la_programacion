# MANEJO DE LSITAS,TUPLAS Y DICCIONARIOS 

# Xavier Armando Montoya Lerma
# 2530403
# Grupo IM 103

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
initial_items_text = "apple, banana, orange"        
new_item = "grape"
search_item = "banana"

# Validaciones
if not initial_items_text.strip():
    print("Error: initial_items_text no puede estar vacío.")
    items_list = []
else:
    items_list = [item.strip() for item in initial_items_text.split(",") if item.strip()]

if not new_item.strip():
    print("Error: new_item no puede estar vacío.")

if not search_item.strip():
    print("Error: search_item no puede estar vacío.")

# Si no hubo errores, continuar
if initial_items_text.strip() and new_item.strip() and search_item.strip():

    # Agregar nuevo producto
    items_list.append(new_item.strip())

    # Cantidad total de elementos
    len_list = len(items_list)

    # Verificar si el producto está en la lista
    is_in_list = search_item.strip() in items_list

    # Salidas
    print("Items list:", items_list)
    print("Total items:", len_list)
    print("Found item:", is_in_list)
