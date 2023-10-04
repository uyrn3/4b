p = 0 
ip = 0
for i in range(10):
    n = int(input("Digite um nemero: "))
    if n % 2 == 0:
        p = p + 1
    else:
        ip = ip + 1
print(f"Pares = {p}")
print(f"Impares = {ip}")