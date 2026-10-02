def find_user_by_email(users, email):
    return next((u for u in users if u["email"] == email), None)

users = [
    {"name": "Ana", "email": "ana@example.com"},
    {"name": "Luis", "email": "luis@example.com"},
]

print(find_user_by_email(users, "luis@example.com"))
print(find_user_by_email(users, "no-existe@example.com"))  # None