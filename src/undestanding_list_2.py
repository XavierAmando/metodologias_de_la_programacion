"""
  Slicing Lists

"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("lista original:",players)

print("slice de lista original", players[0:3])
print("slice de lista original", players[1:4])
print("slice de lista original", players[:4]) 
print("slice de lista original", players[2:]) 
print("slice de lista original", players[-3:])
print("slice de lista original", players[5:2])
print("slice de lista original", players[-3:-1])

"""
slicing en un for
"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("aqui se presentanmlos primeros 3 jugadores del equipo")
for player in players[0:3]
    print(player.title())

"""

copiando una lista
"""
my_foods = ["pizza", "tacos", "flautas", "gorditas"]
# my_foods_copy = my_foods_ # Error: esta no es la manera de copiar
my_foods_1 = my_foods[:]
my_foods_2 = my_foods.copy()
my_foods_3 = list(my_foods)
