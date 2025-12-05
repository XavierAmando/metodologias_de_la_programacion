# --------------------------------------------------
# 7.1 Problem 1: Sum of range with for
# --------------------------------------------------

try:
    n = int(input("Enter n: "))

    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0

        # Recorremos de 1 a n usando for
        for number in range(1, n + 1):
            total_sum += number

            if number % 2 == 0:
                even_sum += number

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)

except:
    print("Error: invalid input")
