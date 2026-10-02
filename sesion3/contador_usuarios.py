class User:
    contador = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.contador += 1

u1 = User("Ana", "ana@example.com")
u2 = User("Luis", "luis@example.com")
u3 = User("Carlos", "carlos@example.com")

print("Usuarios creados:", User.contador)  # 3