# trabajando con lista
"""
recorrer una lista sin importar la cantidad de elementos que tenga

"""
magicians = ["ron", "hermione", "harry", "hagrid", "cedrik"]

print(magicians[0], magicians[1], magicians[2])

for magician in magicians:
    print(magician)
    print(magician.upper())
    print(f"{magician.title()} ese fue un gran hechizo.")
    print(f"\t{magician.lower()}no podemos esperar tu siguiente hechizo")

print("gracias a todos,fue un gran espectatucolo")
print(magicians)

"""
identacion:

python utiliza la indentacion para determinar 
cuando una linea de codigo esta conectada a la linea de codigo anterior.

basicamente,se utilizan 4 espacios en blanc para obligarnos a escribir codigo
ordenado y estructaro
"""
# no olvidemos identar
magicians = ["alice", "david", "caroline"]
for magician in magicians
   print(magician)
print(f"i cant wait to see your next trick, {magician.title()}")   

# identacion innceccesaria
message= "hola python"
print(message)
