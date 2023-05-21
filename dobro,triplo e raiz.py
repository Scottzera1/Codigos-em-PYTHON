# Declaraçao de variavel e a saida 
num = int(input("\tDigite um valor:"))

# Como será feito e mostrar o resultado final

dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

print("O dobro de {}, vale {}\n".format(num, dobro))
print("O triplo de {}, vale {}\n".format(num, triplo))
print("A raíz Quadrada de {}, é igual a {:.2f}\n".format(num, raiz))