# boleanos



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
