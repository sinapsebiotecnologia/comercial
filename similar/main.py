import json
dict = json.load(open('teste.json'))

print(dict)
print(len(dict))

op = input("produto x ou y?: ")

produto = input("codigo produto: ")

if op == "x":
    for i in range(len(dict)):
        if dict[i]["x"] == produto:
            resultado = dict[i]["y"]
            break
else:
    for i in range(len(dict)):
        if dict[i]["y"] == produto:
            resultado = dict[i]["x"]
            break

print(f"O produto {produto}, e similar ao produto {resultado}")