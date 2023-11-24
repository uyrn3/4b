def p(x):
    x = x/n
    return x

x = float(input("informe o valor: "))
n = int(input("informe a quantidade de parcelas: "))

print(f"Valor total R${x}, parcela a se pagar: R${p(x)}")