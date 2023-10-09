tab = int(input("Montar a tabuada de: "))
c = int(input("Começar em: "))
t = int(input("Terminar: "))
if t < c:
    print("O final não pode ser maior")
else:
    for i in range(c,t+1):
        print(f"{tab} x {i} = {tab*i}")