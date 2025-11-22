# lists
"""
las listas son elemntos mutables


las listas nos permiten almacenar informacion en un lugar,la cantidad que tengas
ya seab pocos elementos o millones de elementos

se recomienda nombrar una variable del tipo lista en plural
en python los corchetes[]definen una lista,sus elemntos van separdos por comas.

ejemplo
"""
bycycles=["trek", "canondale", "redline", "specialized", "giant"  ]   
print(bycycles)

print(bycycles[0].title())

# los indices comienzan en 0 y terminan en n-1, onde n es el numero de elementos

print(bycycles[4].title())

# accediendo al ultimo elemnto

print(bycycles[-1].title()) # ultimo elemnto
print(bycycles[-2].title()) # penultimo elemntos
print(bycycles[-5].title()) # primer elemento

# utilizando valores de la lista
message = "mi primer bicicleta fue una " + bycycles[4].title() + ","
print(message)
message_f = f"mi primer bicicleta fue una {bycycles[4].title()} "
print(message_f)

# agregas elemtos a una lista

print("\n")
print("agregar elemntos a una lista")
print(bycycles)

print("metodo de las listas para agregar elemtos: list_name.append(elemnt)")
bycycles.append("ducatti")
print(bycycles)

"""
# listas 
Agrega elemntos al final de una lista
- append(): agrega un elemnto el final de la lista

"""
print("\n-- agregar elemntos a una lista metodo append()---"  )
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # salida: ["honda", "yamaha", "suzuki" ]
motorcycles.append("ducatti")
print(motorcycles) # salida: ["honda", "yamaha", "suzuki", "ducatti" ]
"""
agregar elemntos a una lista en una pocision especifica
- insert(): agrega un elemnto en una pocision especifica de la lista
""" 
print("\n-- agregar elemntos a una lista metodo insert()---"  )
motorcycles = ["honda", "yamaha", "suzuki"] 
print(motorcycles) # salida: ["honda", "yamaha", "suzuki" ]
motorcycles.insert(1, "ducatti")
print(motorcycles) # salida: ["ducatti", "honda", "yamaha", "suzuki" ]

"""
eliminar elemntos de una lista
- del: elimina un elemnto de una lista en una pocision especifica
"""
print("\n-- eliminar elemntos de una lista metodo del---"  )
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # salida: ["honda", "yamaha", "suzuki" ]
del motorcycles[0]
print(motorcycles) # salida: ["honda", "suzuki" ]

""" 
Eliminar elemntos de una lista y usar el valor eliminado
- pop(): elimina y devuelve el ultimo elemnto de una lista
""" 
print("\n-- eliminar elemntoos de una lista y usar el valor eliminado metodo pop()---"  )
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # salida: ["honda", "yamaha", "suzuki" ]
last_motorcycle = motorcycles.pop(1)
print(motorcycles) # salida: ["honda", "yamaha" ]
print(f"la ultima motocicleta que compre fue una {last_motorcycle},")


"""
Eliminar un elemnto especifico de una lista por valor
- remove(): elimina un elemnto especifico de una lista por valor
"""
print("\n-- eliminar un elemnto especifico de una lista por valor metodo remove()---"  )
motorcycles = ["honda", "yamaha", "suzuki", "ducatti"]
print(motorcycles) # salida: ["honda", "yamaha", "suzuki", "ducatti" ]
motorcycles.remove("ducatti")
print(motorcycles) # salida: ["honda", "yamaha", "suzuki" ]
print("\n")

"""
# listas
organizar una lista
- sort(): organiza una lista de forma permanente en orden alfabetico
"""

print("\n-- organizar una lista metodo sort()---"  )
motorcycles = ["honda", "yamaha", "suzuki", "ducatti"]
print(motorcycles) # salida: ["honda", "yamaha", "suzuki", "ducatti" ]
motorcycles.sort()
print(motorcycles) # salida: ["ducatti", "honda", "suzuki", "yamaha" ]
print("\n")
motorcycles.sort(reverse=True)
print(motorcycles) # salida: ["yamaha", "suzuki", "honda", "ducatti" ]

"""
ejmplo
"""
students = ["josue", "victor", "ana", "mike", "paulo", "gerardo"  ] 
print(students)
desired_student = input("¿que estudiante deseas borrar de la lista?: ")
students.remove(desired_student.strip().lower())
print(students)
print("tu has eliminado :", desired_student)
students.reverse()
print(students)

print(len(students))

cars =["kia", "ford", "tesla", "volvo", "chevrolet"]
print(cars)
printed(sorted(cars))
sorted_list =  sorted(cars)
print("lista original:", cars)

