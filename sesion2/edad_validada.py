def pedir_edad():
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            if 0 <= edad <= 120:
                return edad
            print("La edad debe estar entre 0 y 120")
        except ValueError:
            print("Eso no es un número entero")

print("Edad ingresada:", pedir_edad())