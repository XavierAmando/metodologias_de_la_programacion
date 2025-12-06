# CRUD
# Xavier Armando Montoya Lerma
# 2530403
# 1-3

# resumen ejecutivo
"""
Un CRUD es un conjunto de operaciones básicas para gestionar datos: 
Create (crear), Read (leer), Update (actualizar) y Delete (eliminar). 
Para este programa elegí usar una lista de diccionarios porque permite almacenar varios registros, 
cada uno con sus propios campos, y es fácil recorrerlos o buscarlos. 
También facilita agregar o eliminar elementos sin complicaciones. 
El uso de funciones ayuda a separar cada operación del CRUD, 
haciendo el código más ordenado, reutilizable y fácil de mantener. 
Además, permite que el programa sea más claro y que cada parte tenga una responsabilidad específica.
Mi programa cubre todas las funciones principales de un gestor CRUD. Incluye un menú principal que permite al usuario seleccionar acciones de forma interactiva. Implementa la creación de elementos, donde se validan los datos y se evita registrar IDs duplicados. También incorpora la lectura de un ítem específico usando su id, mostrando sus datos si existe.
 Además, permite la actualización de un elemento, modificando nombre, precio y cantidad con validaciones apropiadas. Contiene la función de eliminación, que borra correctamente un ítem existente. Finalmente, incluye un listado completo de elementos, mostrando todos los registros almacenados en la estructura de datos. En conjunto, el programa implementa correctamente todo el ciclo CRUD.
"""

# comentarios
"""
Descripción: Programa que implementa un CRUD (Crear, Leer, Actualizar, Eliminar) simple para elementos almacenados en un diccionario y/o lista, usando funciones para cada operación y un menú de texto para interactuar con el usuario.

Inputs:
- User menu options (string or int).
- For CREATE/UPDATE: item_id, name, price, quantity (or the fields you define).
- For READ/DELETE: item_id.

Outputs:
- Messages indicating the result of each operation:
  - "Item created", "Item updated", "Item deleted", "Item not found", "Items list:", etc.

Validations:
- Menu option must be valid (for example, 0..4 o 0..5 según tu diseño).
- item_id must not be empty.
- Numeric fields must be valid numbers and greater than or equal to 0.
- Disallow creating an item with an id that is already in use (or document tu decisión).
- For READ/UPDATE/DELETE, if the id does not exist, show "Item not found".

Test cases:
1) Normal: create an item, read it, update it, delete it → expected messages and final state.
2) Border: attempt to create item with minimal valid data (e.g., quantity = 0) o usar un id muy corto/largo (documenta tus reglas).
3) Error: use invalid menu option, invalid id (empty), or non-numeric price → expected error messages.
"""

 # Problema 6.1: Gestor CRUD usando diccionarios y/o listas con funciones.
"""
Descripción:
Implementa un programa en Python que gestione un conjunto de "items" en memoria mediante operaciones CRUD. Cada ítem puede representar, por ejemplo, un producto de inventario con los siguientes campos sugeridos:

- id (string o int, único)
- name (string)
- price (float)
- quantity (int)

El programa debe:

1) Definir una estructura de datos principal:
   - Opción A: dict item_id -> dict con datos del ítem.
   - Opción B: list de dicts, cada dict con campos id, name, price, quantity.
   (En comentarios, explica cuál opción escogiste y por qué.)

2) Definir FUNCIONES separadas para cada operación CRUD:
   - create_item(data_structure, item_id, name, price, quantity) -> bool o dict
   - read_item(data_structure, item_id) -> dict o None
   - update_item(data_structure, item_id, new_name, new_price, new_quantity) -> bool
   - delete_item(data_structure, item_id) -> bool
   - list_items(data_structure) -> list o simplemente imprime
   Puedes ajustar nombres y parámetros, pero debe quedar claro qué hace cada función y qué regresa.

3) Implementar un MENÚ en el código principal (main loop):
   Ejemplo de opciones:
   - 1) Create item
   - 2) Read item by id
   - 3) Update item by id
   - 4) Delete item by id
   - 5) List all items
   - 0) Exit

4) En el bucle principal:
   - Mostrar el menú.
   - Leer la opción.
   - Según la opción, pedir los datos necesarios (id, name, price, quantity).
   - Llamar a la función correspondiente.
   - Mostrar mensajes claros de resultado.

Entradas:
- option (string o int; opción de menú).
- item_id (string o int).
- name (string).
- price (float).
- quantity (int).

Salidas:
- Mensajes tipo:
  - "Item created"
  - "Item updated"
  - "Item deleted"
  - "Item not found"
  - "Items list:" y luego la lista de elementos (formato libre pero legible).

Validaciones:
- option debe ser una de las opciones definidas (por ejemplo 0–5).
- item_id no vacío tras strip().
- price y quantity deben ser números válidos:
  - price >= 0.0
  - quantity >= 0
- Si falla alguna validación, mostrar "Error: invalid input" y NO realizar la operación.
- En CREATE:
  - Si el id ya existe, decide una política (por ejemplo, no permitir duplicados) y documenta tu elección.
- En READ/UPDATE/DELETE:
  - Si el id no existe, mostrar "Item not found".

Requisitos de funciones:
- Cada operación CRUD debe estar encapsulada en al menos una función.
- El código del menú principal NO debe contener toda la lógica; debe delegar a las funciones.
- Las funciones deben tener nombres descriptivos y usar parámetros/return en lugar de depender de variables globales (en lo posible).

Sugerencia de flujo:
- Un while principal que corre hasta que el usuario elija 0 (Exit).
- Dentro del while:
  - Mostrar menú.
  - Leer opción.
  - if/elif para decidir qué función llamar.
- Probar el programa con varios casos antes de entregar.
"""
"""
PROBLEMA 6.1 – CRUD con funciones y menú

Elegí la estructura:
Opción A: dict item_id -> dict con los datos del ítem.

Razón:
Usar un dict principal permite acceder rápidamente a los items por su id
(O(1) promedio). Además, garantiza que no existan ids duplicados y facilita
mucho las operaciones CRUD, porque no hay que recorrer listas completas.
"""

# -------------------------
#      CRUD FUNCTIONS
# -------------------------

def create_item(items, item_id, name, price, quantity):
    """Crea un item nuevo si el id no existe. Regresa True si se creó."""
    if item_id in items:
        return False  # ya existe -> política: no permitir duplicados

    items[item_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    return True


def read_item(items, item_id):
    """Regresa el item completo o None si no existe."""
    return items.get(item_id)


def update_item(items, item_id, new_name, new_price, new_quantity):
    """Actualiza un item existente. Regresa True si se actualizó."""
    if item_id not in items:
        return False

    items[item_id]["name"] = new_name
    items[item_id]["price"] = new_price
    items[item_id]["quantity"] = new_quantity
    return True


def delete_item(items, item_id):
    """Elimina un item por id. Regresa True si se eliminó."""
    return items.pop(item_id, None) is not None


def list_items(items):
    """Imprime todos los items en formato legible."""
    if not items:
        print("No items found")
        return
    print("Items list:")
    for i, (item_id, data) in enumerate(items.items(), start=1):
        print(f"{i}) id={item_id}, name={data['name']}, "
              f"price={data['price']}, quantity={data['quantity']}")


# -------------------------
#         MAIN MENU
# -------------------------

def main():
    items = {}  # estructura principal del CRUD

    while True:
        print("\n----- CRUD MENU -----")
        print("1) Create item")
        print("2) Read item")
        print("3) Update item")
        print("4) Delete item")
        print("5) List all items")
        print("0) Exit")

        option = input("Enter option: ").strip()

        if option not in {"0", "1", "2", "3", "4", "5"}:
            print("Error: invalid input")
            continue

        if option == "0":
            print("Goodbye!")
            break

        # --- CREATE ---
        if option == "1":
            item_id = input("Enter item id: ").strip()
            if not item_id:
                print("Error: invalid input")
                continue

            name = input("Enter name: ").strip()
            if not name:
                print("Error: invalid input")
                continue

            try:
                price = float(input("Enter price: "))
                quantity = int(input("Enter quantity: "))
                if price < 0 or quantity < 0:
                    print("Error: invalid input")
                    continue
            except ValueError:
                print("Error: invalid input")
                continue

            ok = create_item(items, item_id, name, price, quantity)
            print("Item created" if ok else "Error: id already exists")

        # --- READ ---
        elif option == "2":
            item_id = input("Enter item id: ").strip()
            if not item_id:
                print("Error: invalid input")
                continue

            result = read_item(items, item_id)
            if result is None:
                print("Item not found")
            else:
                print(f"Item: id={item_id}, name={result['name']}, "
                      f"price={result['price']}, quantity={result['quantity']}")

        # --- UPDATE ---
        elif option == "3":
            item_id = input("Enter item id: ").strip()
            if not item_id:
                print("Error: invalid input")
                continue

            if item_id not in items:
                print("Item not found")
                continue

            name = input("Enter new name: ").strip()
            if not name:
                print("Error: invalid input")
                continue

            try:
                price = float(input("Enter new price: "))
                quantity = int(input("Enter new quantity: "))
                if price < 0 or quantity < 0:
                    print("Error: invalid input")
                    continue
            except ValueError:
                print("Error: invalid input")
                continue

            ok = update_item(items, item_id, name, price, quantity)
            print("Item updated" if ok else "Item not found")

        # --- DELETE ---
        elif option == "4":
            item_id = input("Enter item id: ").strip()
            if not item_id:
                print("Error: invalid input")
                continue

            ok = delete_item(items, item_id)
            print("Item deleted" if ok else "Item not found")

        # --- LIST ---
        elif option == "5":
            list_items(items)


# Ejecutar programa
main()

# conclusiones
"""
El uso de funciones hizo que el CRUD fuera más claro y ordenado, ya que cada operación
quedó separada y fue más fácil de mantener y reutilizar. La estructura basada en un
diccionario permitió acceder rápidamente a los elementos por su id y evitó duplicados.
Durante la validación de entradas surgieron problemas como manejar datos vacíos o
convertir precios y cantidades a valores numéricos; estos se resolvieron usando try/except
y revisando condiciones como price >= 0. También noté que validar antes de ejecutar
cada operación evita errores más grandes. Este CRUD podría ampliarse guardando los datos
en archivos JSON, CSV o incluso en una base de datos para hacerlo persistente.
"""