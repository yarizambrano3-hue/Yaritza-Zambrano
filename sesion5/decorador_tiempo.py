import time

def timer(function):
    def wrapper():
        inicio = time.time()
        resultado = function()
        fin = time.time()
        print(f"Tardó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@timer
def tarea_lenta():
    time.sleep(1)
    print("Tarea completada")

tarea_lenta()