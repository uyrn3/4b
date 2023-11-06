quantidade = int(input("Informe a quantidade de numeros a serem digitados: "))
contador = 1
lista = []
lista_impar = []
lista_par = []

for i in range(1, quantidade+1):
    numero = int(input(f"Informe o {contador}º numero: "))
    contador += 1
    lista.append(numero)
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
        
print(f"Numeros informado: {lista}")
print(f"Numeros pares: {lista_par}")
print(f"Numeros impares: {lista_impar}")