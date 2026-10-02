users = [
    {"name": "Ana", "role": "student"},
    {"name": "Carlos", "role": "admin"},
    {"name": "Luis", "role": "student"},
]

unique_roles = []
for user in users:
    if user["role"] not in unique_roles:
        unique_roles.append(user["role"])

print(unique_roles)