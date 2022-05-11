import json
dict = json.load(open('teste.json'))

print(dict)
print(len(dict))

op = input("produto ORIGINAL ou SIMILAR?: ")

produto = input("codigo produto: ")

if op == "ORIGINAL":
    for i in range(len(dict)):
        if dict[i]["ORIGINAL"] == produto:
            resultado = dict[i]["SIMILAR"]
            break
else:
    for i in range(len(dict)):
        if dict[i]["SIMILAR"] == produto:
            resultado = dict[i]["ORIGINAL"]
            break

print(f"O produto {produto}, e similar ao produto {resultado}")