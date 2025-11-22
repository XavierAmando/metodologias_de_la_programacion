"""

    Un string es una manera sencilla una serie 
    de caracteres. En python , todo lo que se encuentre 
    dentro de las comillas (' ') o dobles (" ")
    sera considerado un string.

    Ejemplo:
    "Esto es un string"
    'Esto es un string'

    'Le dije a un amigo "python es mi lenguaje favorito"'
    "El lenguaje 'python' lleva el nombre por Monty Python , no por ser la serpiente"

"""

name = "clase de programacion"
print(name)


#title
print(name.title())

print(name)

"""
Un metodo es una accion que python
puede realizar en un fragmento de datos
o sobre la variable.

    El punto . despues de una variable 
seguido del metodo title() dice que 
se tiene que ejecutar el metodo title()
de la variable name.

    Todos los metodos van seguidos del parentesis 
    por que en ocaciones neccesita informacion adicional
    para funcionar, la cual iria dentro de los parentesis.
    En esta ocacion, el metodo .title() no requiere informacion 
    adicional para funcionar.

"""

print("metodo upper:", name.upper())
print("metodo lower:", name.lower())


# Concatenacion de STRINGS

first_name = "charly"
last_name = "mercury"
full_name = first_name + " " + last_name
print(full_name)
print(full_name .title())


# whitespaces

""" 
un whitespaces se refiere a cualquier caracter que no se imprime,es decir,un espacio,tabuladores
y finales

eejmplo:
-tabulador: \t
-salto de linea: \n
"""
print("whitespace tabulador")
print("python")
print("\tpython")
print("\t\tpython")

print("whitespace salto de linea")
print("lenguaje: \n\tpython\tc\n\tjavascripts " )


# Eliminacion de espacio en blanco

print("\nEliminacion de espacios en blanco")
progaming_languajes = " python "

print(progaming_languajes)
print(progaming_languajes.rstrip())
print(progaming_languajes.lstrip())
print(progaming_languajes.strip())

# sintax error con String
message = "una fortaleza de python en su comunidad"
print(message)



# f-strings

famous_person = "taylor Swift"
message =f"{famous_person} una vez dijo me voy al oxxo en avion"
print(message)

print(f"{famous_person.upper()} una vez dijo me voy al oxxo en avion")

# Actividad
"""
elige el nombre de una persona famosa(quien tu quieras)
elige una cita famosa de esa persona
iguala ambos strings a una variable

1) Realiza la concantenacion utilizando el signo de suma
2) realiza la cocatenacion utilizando fstrings

"""
famous_person ="cristiano Ronaldo"
print(famous_person)
first_name = "Cristiano"
last_name = "Ronaldo"
full_name = first_name + " " + last_name
print(full_name)

message =f"{famous_person} SIUUUUU"
print(message)

famous_person = "Cristiano Ronaldo"
qoute = "SIUUUUUU"
famous_message = famous_person+" "+Qoute
print(famous_person+" "+qoute)
print(famous_message)

f_strings_message = f"{famous_person} {qoute}"
print(f_strings_message)



