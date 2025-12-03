user_input= input("Set your numbers term: ")

if not user_input.isdigit():
    print("Is not a valid character")
    exit()

n = int(user_input)

if n<1 or n>50:
    print("Number is not in the range")
    exit()
elif n==1:
    print("Fibonacci: 0")
    exit()
elif n==2:
    print("Fibonacci: 0, 1")
    exit()

fibo=[0,1]

for i in range(2, n):
    next_term=fibo[i-1]+fibo[i-2]
    fibo.append(next_term)

fibo_text=", ".join(str(x) for x in fibo)

print(f"Fibonacci: {fibo_text}")

