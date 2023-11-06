nome = input("Informe o nome do(a) atleta: ")
lista = []
soma = 0

for i in range(1, 6) :
    nota = float(input(f"Informe o {i} salto: "))
    lista.append(nota)
    soma += nota
    
print(f"Atleta: {nome}.")
print(f"Saltos: {lista}")
print(f"A média dos saltos: {(soma/5):.2f}m")