attendance = [
    {"name": "Ana", "present": True},
    {"name": "Luis", "present": False},
    {"name": "Carlos", "present": False},
]

for student in attendance:
    if not student["present"]:
        print(student["name"])