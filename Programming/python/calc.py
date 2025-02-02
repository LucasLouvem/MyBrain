import math

n1 = int(input("Digite um numero positivo:"))
while n1 < 0:
    if n1 > 0:
        print(math.sqrt(n1))
    else:
        print("Digite um numero valido!")
    break
