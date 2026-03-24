users = [
{'id': 345324, 'name': 'Alice', 'age': 25},
{'id': 1232, 'name': 123, 'age': 30},
{'id': 7854, 'name': 'Bob', 'age': 22},
{'id': 33412, 'name': None, 'age': 35},
{'id': 78845, 'name': 'Charlie', 'age': 28},
{'id': 45325, 'name': 'Eve', 'age': 40},
{'id': 745633, 'name': True, 'age': 19},
{'id': 64364, 'name': 'Frank', 'age': 33}
]

ids = []

for i in users:
    if type(i['name']) != str:
        ids.append(i['id'])

print(ids)