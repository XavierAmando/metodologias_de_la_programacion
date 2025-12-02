# ==================================================
# PROBLEM 1: Shopping list basics (LIST operations)
# ==================================================

initial_items_text = "apple, banana, orange"
new_item = "grape"
search_item = "banana"

if not initial_items_text.strip():
    print("Error: invalid input")
    items_list = []
else:
    items_list = [item.strip() for item in initial_items_text.split(",") if item.strip()]

if not new_item.strip() or not search_item.strip():
    print("Error: invalid input")
else:
    items_list.append(new_item)

print("Items list:", items_list)
print("Total items:", len(items_list))
print("Found item:", search_item in items_list)


# ==================================================
# PROBLEM 2: Points and distances with TUPLES
# ==================================================

try:
    x1, y1 = 2.0, 3.0
    x2, y2 = 5.0, 7.0

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)
except:
    print("Error: invalid numeric input")


# ==================================================
# PROBLEM 3: Product catalog with DICTIONARY
# ==================================================

product_prices = {
    "apple": 10.0,
    "banana": 8.5,
    "peach": 15.0
}

product_name = "apple"
quantity = 2

if not product_name.strip() or quantity <= 0:
    print("Error: invalid input")
elif product_name in product_prices:
    unit_price = product_prices[product_name]
    total_price = unit_price * quantity
    print("Unit price:", unit_price)
    print("Quantity:", quantity)
    print("Total:", total_price)
else:
    print("Error: product not found")


# ==================================================
# PROBLEM 4: Student grades with DICT + LIST
# ==================================================

grades = {
    "Alice": [90, 85, 88],
    "Bob": [70, 72, 68],
    "Carol": [100]
}

student_name = "Alice"

if not student_name.strip():
    print("Error: invalid input")
elif student_name not in grades:
    print("Error: student not found")
else:
    grades_list = grades[student_name]
    if len(grades_list) == 0:
        print("Error: empty grade list")
    else:
        average = sum(grades_list) / len(grades_list)
        is_passed = a_
