def p(x):
    x = x*(b/100)+x-d
    return x

x = float(input("informe o salario: "))
b = int(input("informe o bonus: "))
d = float(input("informe o desconto: "))
print(f"Salario: R${p(x)}")