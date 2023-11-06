q = int(input("Informe a quant de numeros da lista: "))
lista = []
a = 0
for i in range(q):
    n = int(input("Informe: "))
    lista.append(n)
    a = a + n
print(lista)
print(f"Media = {(a/q):.1f}")