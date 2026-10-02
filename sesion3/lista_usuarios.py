class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        return f"{self.name} - {self.email}"

users = [
    User("Ana", "ana@example.com"),
    User("Luis", "luis@example.com"),
    User("Carlos", "carlos@example.com"),
]

for user in users:
    print(user.display())