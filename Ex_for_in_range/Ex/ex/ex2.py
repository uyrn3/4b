# Exemplo 2: Faça um programa que leia um valor
# inteiro e mostre a tabuada de 1  a 10 do valor lido
n = int(input("Digite um nemero: "))

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")