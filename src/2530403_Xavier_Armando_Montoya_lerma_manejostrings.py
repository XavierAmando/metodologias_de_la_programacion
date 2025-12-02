#manejo de strings
# Xavier Armando Montoya Lerma
# 2530403 
# 1-3



##RESUMEN EJECUTIVO 

# Un string en Python es un tipo de dato que representa texto y es inmutable, 
# lo que significa que no puede modificarse después de crearse.  
# Entre las operaciones básicas están: concatenar cadenas, obtener su longitud (len), 
# extraer subcadenas mediante slicing, buscar patrones con find o in, 
# y reemplazar texto usando replace.  
# Es importante validar y normalizar la entrada (como correos, nombres o contraseñas)  
# para evitar errores, asegurar formato correcto y mejorar la seguridad.  
# El documento cubrirá: descripción de cada problema, diseño de entradas y salidas,  
# validaciones aplicadas, uso de métodos de string y casos de prueba completos  
# incluyendo el código implementado.
"""
 Los strings son inmutables: cualquier cambio genera una nueva cadena.
- Es buena práctica normalizar entrada con strip() y lower() antes de compararla.
- Evitar "números mágicos" en índices; documentar qué extrae cada slice.
- Usar métodos de string en lugar de reescribir lógica básica.
- Diseñar validaciones claras: primero que no esté vacío, luego el formato.
- Escribir código legible: nombres de variables claros y mensajes de error entendibles.
"""



# Problem 1: Full name formatter (name + initials)
"""

Descripción:
Dado el nombre completo de una persona en una sola cadena (por ejemplo: 
"juan carlos tovar"), el programa debe:
1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
2) Mostrar el nombre formateado en Title Case y las iniciales (por ejemplo: J.C.T.).

Entradas:
- full_name (string; nombre completo, puede venir en mayúsculas, 
minúsculas o mezclado, con espacios extra).

Salidas:
- "Formatted name: <Name In Title Case>"
- "Initials: <X.X.X.>"

Validaciones:
- full_name no debe estar vacío después de strip().
- Debe contener al menos dos palabras (por ejemplo, nombre y apellido).
- No aceptar cadenas que sean solo espacios.

Operaciones clave sugeridas: strip(), split(), title(), concatenación, len().


"""
# solucion problema 1
full_name = input("Enter full name: ").strip()

if len(full_name) == 0:
    print("Error: Name cannot be empty.")
    exit()
parts = full_name.split()   

if len(parts) < 2:
    print("Error: Enter at least a first name and one last name.")
    exit()


formatted_name = " ".join(parts).title()
# Obtener iniciales en mayúscula
initials = ".".join([p[0].upper() for p in parts]) + "."

# Salidas
print("Formatted name:", formatted_name)
print("Initials:", initials)

"""
1) Normal Case


Enter full name:   Xavier Armando Montoya Lerma
Formatted name: Xavier Montoya
Initials: X.A.M.L

2) Border Case (Caso Límite)

Enter full name:   ana     lopez
Formatted name: Ana Lopez
Initials: A.L.

Enter full name:    
Error: Name cannot be empty.


"""


# Problem 2: Simple email validator (structure + domain)
"""

Descripción:
Valida si una dirección de correo tiene un formato básico correcto:
- Contiene exactamente un '@'.
- Después del '@' debe haber al menos un '.'.
- No contiene espacios en blanco.
Si el correo es válido, también muestra el dominio (la parte después de '@').

Entradas:
- email_text (string).

Salidas:
- "Valid email: true" o "Valid email: false"
- Si es válido: "Domain: <domain_part>"

Validaciones:
- email_text no vacío tras strip().
- Contar cuántas veces aparece '@'.
- Verificar que no haya espacios (no debe haber " " en email_text).

Operaciones clave sugeridas: strip(), count(), find(), slicing, in, not in.


"""

# solucion problema 2
email_text = input("Enter email: ").strip()

# Validación 1: No debe estar vacío
if len(email_text) == 0:
    print("Valid email: false")
    exit()

# Validación 2: No debe contener espacios
if " " in email_text:
    print("Valid email: false")
    exit()

# Validación 3: Debe contener exactamente un '@'
if email_text.count("@") != 1:
    print("Valid email: false")
    exit()

# Obtener posición del '@'
at_index = email_text.find("@")

# Validación 4: Debe haber un punto después del '@'
dot_index = email_text.find(".", at_index + 1)
if dot_index == -1:
    print("Valid email: false")
    exit()

# Si todas las validaciones pasan → correo válido
print("Valid email: true")

# Dominio = todo lo que está después de '@'
domain = email_text[at_index + 1:]
print("Domain:", domain)

"""
1) Normal Case
Enter email:   xavier123@gmail.com
Valid email: true
Domain: gmail.com
2) Border Case (caso límite)
Enter email:     admin@empresa.org    
Valid email: true
Domain: empresa.org
3) Error Case
Enter email: pedro@@mail.com
Valid email: false


"""


# Problem 3: Palindrome checker (ignoring spaces and case)

"""
Descripción:
Determina si una frase es un palíndromo, es decir, se lee igual de izquierda a derecha y de derecha a izquierda, ignorando espacios y mayúsculas/minúsculas.

Ejemplos:
- "Anita lava la tina" -> palíndromo.
- "Hola mundo" -> no palíndromo.

Entradas:
- phrase (string).

Salidas:
- "Is palindrome: true" o "Is palindrome: false"
- (Opcional) Mostrar también la versión normalizada de la frase.

Validaciones:
- phrase no vacía tras strip().
- Longitud mínima razonable después de limpiar espacios (por ejemplo, al menos 3 caracteres).

Operaciones clave sugeridas: lower(), replace(" ", ""), slicing inverso text[::-1], comparación ==.

"""
# solucion problema 3
phrase = input("Enter a phrase: ").strip()

# Validación 1: No debe estar vacía
if len(phrase) == 0:
    print("Is palindrome: false")
    exit()

# Normalización: convertir a minúsculas y eliminar espacios
normalized = phrase.lower().replace(" ", "")

# Validación 2: Longitud mínima razonable
if len(normalized) < 3:
    print("Is palindrome: false")
    exit()

# Evaluar si es palíndromo usando slicing inverso
is_palindrome = (normalized == normalized[::-1])

# Salidas
print("Is palindrome:", "true" if is_palindrome else "false")
print("Normalized phrase:", normalized)

"""
    1) Normal Case (frase palíndroma válida)
   
Enter a phrase: Anita lava la tina
Is palindrome: true
Normalized phrase: anitalavalatina
    2) Border Case (caso límite)
 
Enter a phrase: oso
Is palindrome: true
Normalized phrase: oso
   3) Error Case

Enter a phrase: hola mundo
Is palindrome: false
Normalized phrase: holamundo



"""
# Problem 4: Sentence word stats (lengths and first/last word)


""""
Descripción:
Dada una oración, el programa debe:
1) Normalizar espacios (quitar espacios al principio y al final).
2) Separar las palabras por espacios.
3) Mostrar:
   - Número total de palabras.
   - Primera palabra.
   - Última palabra.
   - Palabra más corta y más larga (por longitud).

Entradas:
- sentence (string).

Salidas:
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"

Validaciones:
- Oración no vacía tras strip().
- Debe contener al menos una palabra válida después de split().

"""


sentence = input("Enter a sentence: ").strip()

# Validación 1: No debe estar vacía
if len(sentence) == 0:
    print("Error: Sentence cannot be empty.")
    exit()

# Separar palabras (split elimina espacios extra automáticamente)
words = sentence.split()

# Validación 2: Debe haber al menos una palabra real
if len(words) == 0:
    print("Error: No valid words found.")
    exit()

# Datos solicitados
word_count = len(words)
first_word = words[0]
last_word = words[-1]

# Encontrar palabra más corta y más larga
shortest_word = min(words, key=len)
longest_word  = max(words, key=len)

# Salidas
print("Word count:", word_count)
print("First word:", first_word)
print("Last word:", last_word)
print("Shortest word:", shortest_word)
print("Longest word:", longest_word)


"""
    1) Normal Case (oración válida)
Enter a sentence: hola este es un ejemplo
Word count: 5
First word: hola
Last word: ejemplo
Shortest word: es
Longest word: ejemplo

2) Border Case (caso límite: una sola palabra)

Word count: 1
First word: hola
Last word: hola
Shortest word: hola
Longest word: hola

3) Error Case (entrada vacía)
Enter a sentence:
Error: Sentence cannot be empty.
"""


    

# Problem 5: Password strength classifier
"""

Descripción:
Clasifica una contraseña como "weak", "medium" o "strong" según reglas mínimas (puedes afinarlas, pero documéntalas en los comentarios).

Ejemplo de reglas:
- Weak: longitud < 8 o todo en minúsculas o muy simple.
- Medium: longitud >= 8 y mezcla de letras (mayúsculas/minúsculas) o dígitos.
- Strong: longitud >= 8 y contiene al menos:
  - una letra mayúscula,
  - una letra minúscula,
  - un dígito,
  - un símbolo no alfanumérico (por ejemplo, !, @, #, etc.).

Entradas:
- password_input (string).

Salidas:
- "Password strength: weak"
- "Password strength: medium"
- "Password strength: strong"

Validaciones:
- No aceptar contraseña vacía.
- Verificar longitud con len().

Operaciones clave sugeridas:
- Recorrer carácter por carácter.
- Métodos: isupper(), islower(), isdigit(), isalnum().
- Uso de banderas booleanas (has_upper, has_lower, etc.).

"""

password_input = input("Enter password: ")

# Validación 1: No vacía
if len(password_input) == 0:
    print("Password strength: weak")
    exit()

length = len(password_input)

# Bandera para cada categoría de carácter
has_upper = False
has_lower = False
has_digit = False
has_symbol = False

# Recorrer la contraseña carácter por carácter
for ch in password_input:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif not ch.isalnum():   # símbolo
        has_symbol = True

# Clasificación

# Caso 1: Weak
if length < 8:
    print("Password strength: weak")
    exit()

# Caso 2: Strong (cumple todas las condiciones)
if has_upper and has_lower and has_digit and has_symbol:
    print("Password strength: strong")
    exit()

# Caso 3: Medium (cumple algunas, pero no todas)
print("Password strength: medium")
"""
1) Normal Case (contraseña fuerte)

Enter password: Abc333!@
Password strength: strong

2) Border Case (caso límite: longitud = 8 pero sin símbolos → medium)

Enter password: Abc12345
Password strength: medium

3) Error Case (contraseña vacía → weak)

ESnter password:
Password strength: weak



"""

# Problem 6: Product label formatter (fixed-width text)
"""

Descripción:
Dado el nombre de un producto y su precio, genera una etiqueta en una sola línea con el siguiente formato:

Product: <NAME> | Price: $<PRICE>

La cadena completa debe tener exactamente 30 caracteres:
- Si es más corta, rellena con espacios al final.
- Si es más larga, recorta hasta 30 caracteres.

Entradas:
- product_name (string).
- price_value (puede leerse como string o número; conviértelo a string para mostrarlo).

Salidas:
- "Label: <exactly 30 characters>"
(Puedes mostrar la etiqueta entre comillas para que se vean los espacios.)

Validaciones:
- product_name no vacío tras strip().
- price_value debe poder convertirse a un número positivo.

Operaciones clave sugeridas:
- Uso de f-strings o concatenación para formar la etiqueta base.
- len() para medir la longitud.
- slicing para recortar: label[:30].
- Relleno con espacios hasta alcanzar 30 caracteres.

"""

product_name = input("Enter product name: ").strip()


if len(product_name) == 0:
    print("Error: Product name cannot be empty.")
    exit()


price_input = input("Enter price: ").strip()

# Validación 2: Debe poder convertirse a número positivo
try:
    price_value = float(price_input)
    if price_value <= 0:
        print("Error: Price must be positive.")
        exit()
except:
    print("Error: Invalid price format.")
    exit()

# Convertir precio a string sin formato especial
price_str = str(price_value)

# Formar la etiqueta base
label = f"Product: {product_name} | Price: ${price_str}"

# Ajuste a exactamente 30 caracteres
if len(label) < 30:
    # Rellenar con espacios a la derecha
    label = label + " " * (30 - len(label))
else:
    # Recortar a 30 caracteres
    label = label[:30]

print("Label:", f"'{label}'")  # Entre comillas para mostrar espacios
"""
1) Normal Case (producto y precio válidos)
Enter product name: Galletas
Enter price: 12.5
Label: 'Product: Galletas | Price: $12.5   '

2) Border Case (etiqueta exactamente de 30 caracteres)
Enter product name: Pan
Enter price: 10
Label: 'Product: Pan | Price: $10      '

3) Error Case (precio inválido)
Enter product name: Refresco
Enter price: abc
Error: Invalid price format.


"""

# El manejo de strings es fundamental porque casi toda la entrada y salida de datos
# del usuario llega en forma de texto y debe ser procesada correctamente.
# Funciones como lower(), strip(), split() y join() permiten limpiar, organizar
# y transformar cadenas según el objetivo del programa.
# Normalizar el texto antes de compararlo evita errores por mayúsculas, espacios
# o variaciones que no deberían afectar la lógica.
# Un buen diseño de validaciones previene datos basura, fallos y comportamientos
# inesperados en el programa.
# Además, aprender sobre la inmutabilidad de los strings y el uso de slices facilita
# manipular texto de forma segura y eficiente, creando nuevas versiones sin alterar
# la original.

"""
    # References:
# 1) Python Documentation – Built-in Types: Text Sequence Type — str.
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Python Tutorial – Strings and Text Processing.
#    https://docs.python.org/3/tutorial/introduction.html#strings
# 3) “Automate the Boring Stuff with Python” – Al Sweigart, capítulos sobre manipulación de texto.
# 4) Apuntes de Programación Básica y Algoritmos – manejo de cadenas y validaciones de entrada.
# 5) Artículos sobre buenas prácticas de sanitización y normalización de texto en software.
# 6) W3Schools Python String Methods – Resumen de funciones comunes: strip(), split(), replace(), etc.


"""

""""
https://github.com/XavierAmando/metodologias_de_la_programacion.git
"""