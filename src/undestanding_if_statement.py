cars = ["audi", "bmw", "chevrolet", "corvette", "tesla"]

for car in cars:
    if car == "bmw" or car=="tesla" or car=="audi":
        print(car.upper())
    else:
        print(car)   


# condicionales:El condicional es el corazon de un if
# condicional true
car = "bmw"
print(car == "bmw") # salida true
# condicional false    
car_2 = "audi"
print(car_2 == "audi") # salida false

# condicional fa|lse
car_2 = "audi"
print(car_2.lower() == "Audi")

# condicional != para determinar desigualdad
requested_topping = "mushrooms" # --> string
if requested_topping != "anchovies":# -->
    print("Hold the anchovies")

# comparaciones numericos
age = 18 # --> int
print(age == 18) # --> true

answer = 17
if answer != 42:
    print("Esa no es la respuesta correcta. Intenta de nuevo!")

age = 19
print(age < 21) # --> true
print(age <= 21) # --> true
print(age > 21) # --> false|
print(age >= 21) # --> false

# multiple conditions

age_0 = 22
age_1 = 18

print("multiple conditions")
print("operacion and - pseint (y)")
print(age_0 >= 21 and age_1 >= 21) 
print(age_0 >= 21 and  age_1 >= 18)

age_0 = 22
age_1 = 18
print("multiple conditions")
print("operacion or - pseint (o)")
print(age_0 >= 21 or age_1 >= 21) # true 
print(age_0 >= 21 or  age_1 >= 18) # false


#¿como nos preguntar si un valor esta en una lista?
print("\nA value is in a list")
requested_toppings = ["mushrooms", "onions", "pineapple"]   
print("mushrooms" in requested_toppings) # true
print("pepperoni" in requested_toppings) # false

# A value is not in a list
banned_users = ["Gabriel", "Max", "Andrik", "Quevedo", "Chris", "Angel"]
user = "Pedro"
print(user not in banned_users) # true

# Variables de tipo booleano
game_active = True
can_edit = False

"""
if statements

if condition:
    do something

if condition:
    do something(true)
else
    do something(false)
"""

# preguntar la edad a un usuario
# y decirle si tiene la edad
# suficiente para votar
# input("") --> str
age = int(input("\n\nEscribe tu edad: "))
print(f"\ntu edad es: {age}")


if age>= 18:
    print("tu tienes la edad suficiente para votar")
else:
    print("lo siento,tu eres muy joven para votar")

