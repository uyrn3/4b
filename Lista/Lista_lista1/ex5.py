c = int(input("Informe o começo: "))
f = int(input("Informe o fim: ")) 

lista = []
for i in range(f,c-1,-1):
    lista.append(i)
print(lista)