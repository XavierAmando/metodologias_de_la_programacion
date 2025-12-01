"""
  vamos a realizar un programa que defina un pin
  para dar acceso a un usuario

  si usario va a tener un maximo de itentos oara
  colocar bien el pin

  si usuario  sobrepa este maximoi de intentos
  se le va a bloquear la cuenta y el acceso


"""
CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
attempts = 0

while attempts < MAX_ATTEMPTS:
    user_pin = input("Por favor ingresa tu PIN: ")

    if user_pin == CORRECT_PIN:
        print("Acceso concedido. Bienvenido!")
        break
    else:
        attempts += 1
        remaining_attempts = MAX_ATTEMPTS - attempts
        if remaining_attempts > 0:
            print("ingresa un pin no valido")
            print(f"PIN incorrecto. Te quedan {remaining_attempts} intentos.")
        else:
            print("cuenta bloqueada por demasiados intentos fallidos.")