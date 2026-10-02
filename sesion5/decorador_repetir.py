def repetir(function):
    def wrapper():
        for _ in range(3):
            function()
    return wrapper

@repetir
def saludar():
    print("Hola")

saludar()