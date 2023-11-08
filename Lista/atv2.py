lista = []
for i in range(1,4):
    d = int(input("Digite a sua idade: "))
    t = float(input("Digite a sua altura: "))
    lista.append(d)
    lista.append(t)
    lista.sort()
print(lista)