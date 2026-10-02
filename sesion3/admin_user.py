class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        return f"{self.name} - {self.email}"

class Admin(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.role = "admin"

    def display(self):
        return f"{self.name} - {self.email} - Role: {self.role}"

admin1 = Admin("Carlos", "carlos@example.com")
print(admin1.display())