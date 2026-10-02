def get_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None

numeros = [10, 20, 30]
print(get_item(numeros, 1))   # 20
print(get_item(numeros, 10))  # None