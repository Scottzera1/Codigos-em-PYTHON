from math import sqrt 
from math import trunc
from math import factorial

num = int(input("Digite um número: "))
raiz = sqrt(num)
print("A raiz de {} é igual a {:.2f}\n".format(num, raiz))

pont = trunc(num)
print("O número é {} e ele vai ficar assim {}\n.".format(num, pont))

frec = factorial(num)
print("O valor recebido é {} e pela fatoração fica assim {}.".format(num, frec))