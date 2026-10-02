cart = [
    {"item": "pan", "price": 1.5},
    {"item": "leche", "price": 2.0},
    {"item": "huevos", "price": 3.25},
]

total = 0
for product in cart:
    total += product["price"]
    print(product["item"], "->", product["price"])

print("Total:", total)