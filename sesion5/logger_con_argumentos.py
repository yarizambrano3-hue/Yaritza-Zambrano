def logger(function):
    def wrapper(*args, **kwargs):
        print("Function executed")
        return function(*args, **kwargs)
    return wrapper

@logger
def sumar(a, b):
    return a + b

print(sumar(3, 5))