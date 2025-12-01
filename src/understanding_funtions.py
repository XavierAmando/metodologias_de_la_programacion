### funciones
# las funciones son bloques de codigo para realizar
# una tarea especifica

# cuando queremos realiza la tarea que se ha definido
# en la fucion,tenemos que llamar el nombre de la
# funcion que reakizae la accion}

"""
  sintaxis de una funcion

  def nombre_de_la_funcion():
      acciones


  ejemplo: vamoa a definir una funcion que salude que de un 
  saludo al cristopher

"""
def gretting_cristopher():
    """
    funcion que saluda a una persona llamada cristopher
    """
    for i in range(0,5):
      print("hello cristopher")


gretting_cristopher()

# ejemplo de una funcion que genere el nombre completo
# de una persona y lo regrese
# parametros posicionales
def create_full_name(first_name, middle_name, last_name=""):
    """
    funcion que recibe el nombre y apellido de una persona
    y regresa el nombre completo
    """
    full_name = f"{first_name.strip ()}\
    {middle_name.strip()} {last_name.strip()}"
    return full_name.title()
   
first_name = input("ingresa tu primer nombre: ") 
middle_name = input("ingresa tu segundo nombre:si no tienes deja en blanco ") 
last_name = input("ingresa tu apellido: ")  
# Argumentos posicionales
generated_full_name = create_full_name(
    first_name.strip().lower(), 
    last_name.strip().lower(),
    middle_name.strip().lower())

print(generated_full_name)

# Argumentos llave
generated_full_name_2 = create_full_name(
  middle_name = user_middle_name, 
  first_name = user_first_name, 
  last_name = user_last_name
)

# args en funciones
# kwargs en funciones
# manejo de datos (.txt, .csv, .json, excel, works,)
# args via consola (sys)
# cli en python - comand line interface
# testing - casos de pruebas (borde,casos, validos)