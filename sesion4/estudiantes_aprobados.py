students = [
    {"name": "Ana", "grade": 8},
    {"name": "Luis", "grade": 5},
    {"name": "Carlos", "grade": 9},
]

aprobados = [s["name"] for s in students if s["grade"] >= 7]
print(aprobados)  # ['Ana', 'Carlos']