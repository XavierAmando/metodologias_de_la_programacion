# 

try:
   age= int(input("escribe tu edad:"))
except:
    age = -1
    print("error:ingresaste uncaracter no valido")



    
#>< 
if age >= 100:
    print("tienes mas de un siglo")

elif age >= 18 and age < 100:
     print("eres mayor de edad")
elif age >= 0 and age < 18:
     print("eres menor de edad")
else: 
    print("tuviste un error")

print("holi charly")

"""
hacer un programa que pregunte la edad de una persona
y responde los sig
- si la edad es menor o igual a 4,entonces la entrada es gratuita
-si la edad es menor a 18,pero mayor que 4
entonces la entrada cuesta $200
-si la edad es mayor que 18,entonces la entrada cuesta $400
"""
try:
    age = int(input("escribe tu edad:"))    
except:
    age = -1
    print("error:ingresaste uncaracter no valido")
if age <= 4 and age >=0:
    print("la entrada es gratis")
elif age < 18 and age >4:
    print("la entrada cuesta $200")
elif age >= 18:
    print("la entrada cuesta $400")
else:
    print("no sirve eso")

# multiple i
guisos = ["deshebrada","asada","salsa verde","pozoles"]
if "asada" in guisos:
    print("si tenemos guiso de asada")
else :
    print("no tenemos guiso de asada")  
if "tamales" in guisos:
    print(" hay tenemos tamales")
else:
    print("no  tenemos tamales")
if "salsa verde" in guisos:
    print("si hay salsa verde")
else:
    print("no hay salsa verde")


# lista vacia
guisos = []
if guisos:
    print("hay guisos") 

# utilizandi varias listas
guisos_disponibles = ["salsa verde", "deshebrada", "mole"] 
guisos_a_ordenar = ["salsa verde", "cald0 de iguala"]          

print("¿que guisos te gustaria ordenar?")
for guiso in guisos_a_ordenar:
    print(f"deseo {guiso}")
    if guiso in guisos_disponibles:
        print(f"si tenemos {guiso} ")
    else:
        print("no tenemos ese guiso")
print("realizando el pedido ")        