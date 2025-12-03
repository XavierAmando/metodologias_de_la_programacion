# numeros y boleanos
# Xavier Armando Montoya Lerma
# 2530403
# 1-3 


#resumen ejecutivo
""""
En Python, int representa números enteros y float representa números con decimales;
 se diferencian en que los floats permiten mayor precisión al manejar valores fraccionados.
 Un booleano (True o False) es un tipo lógico que se obtiene al hacer comparaciones
 como >, <, ==, != y sirve para decidir si una condición se cumple o no.
 Es importante validar rangos para evitar datos inválidos y evitar divisiones entre cero,
 ya que eso provoca errores en la ejecución del programa.
 El documento cubrirá: explicación general de cada problema, diseño de entradas y salidas,
 validaciones aplicadas a los datos y cómo se usan ints, floats y booleanos
 para controlar decisiones dentro de cada solución.
"""

# comentarios
"""
 Se recomienda usar tipos apropiados: int para contadores o cantidades enteras
 y float para valores que requieren decimales, como precios o promedios.
 Para evitar repetir expresiones largas, es mejor guardar resultados intermedios
 en variables con nombres descriptivos que hagan el código más claro.
 Siempre se deben validar los datos antes de operar, por ejemplo verificar que
 horas, salarios o cantidades no sean negativos para evitar errores lógicos.
 Es importante usar nombres de variables entendibles y mostrar mensajes claros
 para que el usuario sepa qué debe ingresar.
 También se debe documentar cómo se interpretan los booleanos en cada problema:
 cuándo un resultado True significa que una condición se cumple
 y cuándo un False indica que no se cumple.
"""

# Problem 1: Temperature converter and range flag
"""
 Description:

Descripción:
Convierte una temperatura en grados Celsius (float) a Fahrenheit y Kelvin. Además, determina un valor booleano is_high_temperature que sea true si la temperatura en Celsius es mayor o igual que 30.0 y false en caso contrario.

Entradas:
- temp_c (float; temperatura en °C).

Salidas:
- "Fahrenheit:" <temp_f>
- "Kelvin:" <temp_k>
- "High temperature:" true|false

Validaciones:
- Verificar que temp_c pueda convertirse a float.
- No permitir temperaturas físicas imposibles en Kelvin (por ejemplo, temp_k < 0.0).

Operaciones clave sugeridas:
- Conversión: temp_f = temp_c * 9 / 5 + 32
- Conversión: temp_k = temp_c + 273.15
- Comparación: is_high_temperature = (temp_c >= 30.0)

"""
# solucion de problema 1
try:
    temp_c = float(input("Enter temperature in Celsius: "))
    temp_k = temp_c + 273.15
    if temp_k < 0.0:
        print("Error: invalid input")
    else:
        temp_f = temp_c * 9/5 + 32
        is_high_temperature = (temp_c >= 30.0)
        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", is_high_temperature)
except:
    print("Error: invalid input")


# casos de pruebas
# caso 1
""""
Entrada simulada:

25


Proceso esperado:

temp_c = 25

temp_k = 298.15 (≥ 0, válido)

temp_f = 77.0

is_high_temperature = False (25 < 30)

Salida esperada:

Fahrenheit: 77.0
Kelvin: 298.15
High temperature: False
"""

# 2. Caso Borde
"""
Entrada simulada:

-273.15


Proceso esperado:

temp_c = -273.15

temp_k = 0.0 (límite mínimo, válido)

temWS
is_high_temperature = False

Salida esperada:

Fahrenheit: -459.66999999999996
Kelvin: 0.0
High temperature: False
"""

# 3. Caso Error
"""
A) Error físico (Kelvin negativo)

Entrada simulada:

-300


Proceso esperado:

temp_k = -26.85 → no válido

El programa debe mostrar error antes de convertir a Fahrenheit.

Salida esperada:

Error: invalid input

# Error de formato (cae en el except)

Entrada simulada:

hola


Salida esperada:

Error: invalid input

"""



# Problem 2: Work hours and overtime payment
"""
Description:
Calcula el pago total semanal de un trabajador. Hasta 40 horas se pagan a hourly_rate (float). Las horas extra (> 40) se pagan al 150% de la tarifa normal. Además, genera un booleano has_overtime que indique si el trabajador hizo horas extra.

Entradas:
- hours_worked (float; horas trabajadas en la semana).
- hourly_rate (float; pago por hora).

Salidas:
- "Regular pay:" <regular_pay>
- "Overtime pay:" <overtime_pay>
- "Total pay:" <total_pay>
- "Has overtime:" true|false

Validaciones:
- hours_worked >= 0
- hourly_rate > 0
- Si alguno no cumple, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Uso de min() y max() para separar horas regulares y extra.
- Cálculo: overtime_pay = overtime_hours * hourly_rate * 1.5
- Booleano: has_overtime = (hours_worked > 40)


"""
# solucion del problema 2
try:
    hours_worked = float(input("Hours worked: "))
    hourly_rate = float(input("Hourly rate: "))

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        overtime_hours = max(0.0, hours_worked - 40.0)
        regular_hours = min(hours_worked, 40.0)
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = (hours_worked > 40.0)

        print("Regular pay:", regular_pay)
        print("Overtime pay:", overtime_pay)
        print("Total pay:", total_pay)
        print("Has overtime:", has_overtime)
except:
    print("Error: invalid input")

# casos de pruebas 1
# caso 1
""" 
Hours worked: 45
Hourly rate: 20

Proceso esperado:

regular_hours = 40

overtime_hours = 5

regular_pay = 40 × 20 = 800

overtime_pay = 5 × 20 × 1.5 = 150

total_pay = 950

has_overtime = True

# salida 
Regular pay: 800.0
Overtime pay: 150.0
Total pay: 950.0
Has overtime: True



"""
# caso 2 borde 
"""
Hours worked: 40
Hourly rate: 15
Proceso esperado:

overtime_hours = 0

regular_pay = 600

overtime_pay = 0

total_pay = 600

has_overtime = False
# salida
Regular pay: 600.0
Overtime pay: 0.0
Total pay: 600.0
Has overtime: False



"""
# caso 3 error 
"""
Hours worked: -5
Hourly rate: 18
Salida esperada:

Error: invalid input


"""




# Problem 3: Discount eligibility

""""
 Description:
Determina si un cliente obtiene un descuento en su compra. La regla es:
- Tiene descuento si:
  - is_student es true OR
  - is_senior es true OR
  - purchase_total >= 1000.0
Calcula también el total a pagar aplicando un 10% de descuento cuando sea elegible.

Entradas:
- purchase_total (float; total de la compra).
- is_student_text (string; "YES" o "NO").
- is_senior_text (string; "YES" o "NO").

Salidas:
- "Discount eligible:" true|false
- "Final total:" <final_total>

Validaciones:
- purchase_total >= 0.0
- Normalizar is_student_text e is_senior_text a mayúsculas y convertir a booleanos is_student, is_senior.
- Si el texto no es "YES" ni "NO", mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Conversión a bool por comparación de strings.
- Booleanos: discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
- Cálculo: final_total = purchase_total * 0.9 si discount_eligible es true, si no, el mismo purchase_total.
"""
# solucion problema 3

try:
    purchase_total = float(input("Purchase total: "))
    is_student_text = input("Student (YES/NO): ").strip().upper()
    is_senior_text = input("Senior (YES/NO): ").strip().upper()

    if purchase_total < 0.0:
        print("Error: invalid input")
    elif is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
        print("Error: invalid input")
    else:
        is_student = (is_student_text == "YES")
        is_senior = (is_senior_text == "YES")

        discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
        final_total = purchase_total * 0.9 if discount_eligible else purchase_total

        print("Discount eligible:", discount_eligible)
        print("Final total:", final_total)
except:
    print("Error: invalid input")

# casos de pruebas
# cas0 1
"""
Entrada simulada:

Purchase total: 500
Student (YES/NO): YES
Senior (YES/NO): NO


Proceso esperado:

purchase_total = 500

is_student = True

is_senior = False

discount_eligible = True (porque es estudiante)

final_total = 500 * 0.9 = 450

Salida esperada:

Discount eligible: True
Final total: 450.0
"""
 #2. Caso Borde (límite)
"""
A) Justo en el límite del descuento por monto

Entrada simulada:

Purchase total: 1000
Student (YES/NO): NO
Senior (YES/NO): NO


Proceso esperado:

purchase_total = 1000

is_student = False

is_senior = False

discount_eligible = True (porque total ≥ 1000)

final_total = 1000 * 0.9 = 900

Salida esperada:

Discount eligible: True
Final total: 900.0
"""
# 3. Caso Error
"""
A) Monto inválido

Entrada simulada:

Purchase total: -50
Student (YES/NO): NO
Senior (YES/NO): NO


Salida esperada:

Error: invalid input

B) Texto inválido en YES/NO (cae en la validación)

Entrada simulada:

Purchase total: 500
Student (YES/NO): maybe
Senior (YES/NO): NO


Salida esperada:

Error: invalid input

C) Error de formato que activa el except

Entrada simulada:

Purchase total: hola
Student (YES/NO): YES
Senior (YES/NO): NO


Salida esperada:

Error: invalid input




"""



# Problem 4: Basic statistics of three integers
"""
Description:
Descripción:
Lee tres números enteros y calcula: suma, promedio (float), valor máximo, valor mínimo y un booleano all_even que indique si los tres números son pares.

Entradas:
- n1 (int)
- n2 (int)
- n3 (int)

Salidas:
- "Sum:" <sum_value>
- "Average:" <average_value>
- "Max:" <max_value>
- "Min:" <min_value>
- "All even:" true|false

Validaciones:
- Verificar que los tres valores se puedan convertir a int.
- No se requieren restricciones adicionales (se permiten negativos).

Operaciones clave sugeridas:
- sum_value = n1 + n2 + n3
- average_value = sum_value / 3
- max(), min()
- all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

"""
# solucion del problema 4
try:
    n1 = int(input("Enter integer 1: "))
    n2 = int(input("Enter integer 2: "))
    n3 = int(input("Enter integer 3: "))

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", all_even)
except:
    print("Error: invalid input")

# caso de pruebas
# cas0 1
"""
1. Caso Normal

Entrada simulada:

Enter integer 1: 4
Enter integer 2: 7
Enter integer 3: 10


Proceso esperado:

sum = 4 + 7 + 10 = 21

average = 21 / 3 = 7.0

max = 10

min = 4

all_even = False (solo 4 y 10 son pares)

Salida esperada:

Sum: 21
Average: 7.0
Max: 10
Min: 4
All even: False
"""
# 2. Caso Borde (con valores iguales)
"""
Entrada simulada:

Enter integer 1: 5
Enter integer 2: 5
Enter integer 3: 5


Proceso esperado:

sum = 15

average = 5.0

max = 5

min = 5

all_even = False (5 es impar)

Salida esperada:

Sum: 15
Average: 5.0
Max: 5
Min: 5
All even: False
"""
#3. Caso Error
"""
A) Formato inválido (cae en el except)

Entrada simulada:

Enter integer 1: hola
Enter integer 2: 8
Enter integer 3: 3


Salida esperada:

Error: invalid input

B) Otro error válido (número decimal cuando esperaba entero)

Entrada simulada:

Enter integer 1: 4.5
Enter integer 2: 2
Enter integer 3: 8


Salida esperada:

Error: invalid input


"""    

# Problem 5: Loan eligibility
"""
 Description:
Determina si una persona es elegible para un préstamo con base en:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)
La regla es:
- debt_ratio = monthly_debt / monthly_income
- eligible es true si:
  - monthly_income >= 8000.0 AND
  - debt_ratio <= 0.4 AND
  - credit_score >= 650

Entradas:
- monthly_income (float; ingreso mensual).
- monthly_debt (float; pagos mensuales de deuda).
- credit_score (int; puntaje de crédito).

Salidas:
- "Debt ratio:" <debt_ratio>
- "Eligible:" true|false

Validaciones:
- monthly_income > 0.0 (evitar división entre cero).
- monthly_debt >= 0.0
- credit_score >= 0
- Si no se cumple, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Cálculo de deuda relativa: debt_ratio = monthly_debt / monthly_income
- Booleano: eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)
"""
# solucion problema 5 

try:
    monthly_income = float(input("Monthly income: "))
    monthly_debt = float(input("Monthly debt: "))
    credit_score = int(input("Credit score: "))

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)

        print("Debt ratio:", debt_ratio)
        print("Eligible:", eligible)
except:
    print("Error: invalid input")


# casos de pruebas
# caso 1
"""
Entrada simulada:

Monthly income: 9000
Monthly debt: 2000
Credit score: 700


Proceso esperado:

debt_ratio = 2000 / 9000 = 0.222...

eligible = True

income ≥ 8000 ✔

debt_ratio ≤ 0.4 ✔

credit_score ≥ 650 ✔

Salida esperada:

Debt ratio: 0.2222222222222222
Eligible: True
"""
# 2. Caso Borde (límite exacto)
"""
Entrada simulada:

Monthly income: 8000
Monthly debt: 3200
Credit score: 650


Proceso esperado:

debt_ratio = 3200 / 8000 = 0.4

eligible = True

income ≥ 8000 ✔

debt_ratio ≤ 0.4 ✔

credit_score ≥ 650 ✔

Salida esperada:

Debt ratio: 0.4
Eligible: True
"""
# 3. Caso Error
"""
A) Valores inválidos

Entrada simulada:

Monthly income: 0
Monthly debt: 500
Credit score: 700


Salida esperada:

Error: invalid input

B) Formato inválido (cae en el except)

Entrada simulada:

Monthly income: hola
Monthly debt: 500
Credit score: 700


Salida esperada:

Error: invalid input

"""


#  Problem 6: BMI and category flag
""""
 Description:
Descripción:
Calcula el índice de masa corporal (BMI) de una persona con la fórmula:
- bmi = weight_kg / (height_m * height_m)
Además, genera booleanos para indicar:
- is_underweight (bmi < 18.5)
- is_normal (18.5 <= bmi < 25.0)
- is_overweight (bmi >= 25.0)

Entradas:
- weight_kg (float; peso en kilogramos).
- height_m (float; estatura en metros).

Salidas:
- "BMI:" <bmi_redondeado>
- "Underweight:" true|false
- "Normal:" true|false
- "Overweight:" true|false

Validaciones:
- weight_kg > 0.0
- height_m > 0.0
- Si no se cumple, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Cálculo de bmi como float.
- Uso de round(bmi, 2) para mostrar 2 decimales.
- Evaluación de rangos con condiciones encadenadas.
"""
# solucion problema 6
try:
    weight_kg = float(input("Weight (kg): "))
    height_m = float(input("Height (m): "))

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        bmi_r = round(bmi, 2)

        is_underweight = (bmi < 18.5)
        is_normal = (18.5 <= bmi < 25.0)
        is_overweight = (bmi >= 25.0)

        print("BMI:", bmi_r)
        print("Underweight:", is_underweight)
        print("Normal:", is_normal)
        print("Overweight:", is_overweight)
except:
    print("Error: invalid input")

# caso de pruebas
"""
1. Caso Normal (BMI dentro del rango saludable)

Entrada simulada:

Weight (kg): 70
Height (m): 1.75


Proceso esperado:

bmi = 70 / (1.75²) = 22.857…

bmi_r = 22.86

is_underweight = False

is_normal = True

is_overweight = False

Salida esperada:

BMI: 22.86
Underweight: False
Normal: True
Overweight: False
"""
# 2. Caso Borde (límite exacto entre normal y sobrepeso)
"""
Entrada simulada:

Weight (kg): 62
Height (m): 1.57


Cálculo:

bmi = 62 / (1.57²) ≈ 25.15 → ya entra en Overweight

Salida esperada:

BMI: 25.15
Underweight: False
Normal: False
Overweight: True


(Este es un caso borde porque está muy cerca del límite de 25.0)
"""
# 3. Caso Error
""" 
A) Peso inválido

Entrada simulada:

Weight (kg): -50
Height (m): 1.70


Salida esperada:

Error: invalid input

B) Formato inválido (cae en el except)

Entrada simulada:

Weight (kg): hola
Height (m): 1.70


Salida esperada:

Error: invalid input

"""

# conclusiones
""" 
Los enteros y flotantes suelen trabajar juntos en programas porque 
muchos cálculos reales mezclan cantidades exactas con valores decimales,
 como horas trabajadas o precios. 
 Las comparaciones producen valores booleanos que permiten decidir qué camino seguir mediante sentencias if. Validar rangos y evitar divisiones entre cero es clave para prevenir errores lógicos y fallos en la ejecución. Además, diseñar condiciones combinadas con and, or y not ayuda a expresar reglas más precisas y realistas. Todos estos patrones

 se repiten constantemente en problemas de nómina, cálculos de descuentos, intereses de préstamos y en general en
   cualquier sistema que tome decisiones basadas en datos numéricos.

Es importante usar validaciones y casos de prueba porque así evitamos que el programa falle cuando alguien mete datos raros o incorrectos. También nos ayuda a ver si todo funciona bien en situaciones normales y en límites. En pocas palabras, sirve para asegurarnos de que el código no haga cosas locas, dé resultados confiables y sea más fácil de usar sin errores.   
"""   
# referencias
"""
1) https://youtu.be/0wtQJX_YlGU?si=xi7OzluCpHfMp7zX
2)apuntes de clases aunque 
3)https://es.python-3.com/?p=269#google_vignette
4)https://ellibrodepython.com/booleano-python
5)https://youtu.be/VJadt5X0uzE?si=hG-vJ_nermfWRjK5
"""


# repo
"""
https://github.com/XavierAmando/metodologias_de_la_programacion.git
"""