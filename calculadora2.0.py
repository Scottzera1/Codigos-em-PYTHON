#declaraçoes de variaveis e saída de dados#
nome = input("Digite seu nome:\n")
n1 = int(input("Digite o primeiro numero:"))
n2 =  int(input("Digite o segundo numero:"))

# soma entre dois valores inseridos pelo usuario
soma = n1 + n2

# subtração de dois valores inseridos pelo usuario
sub = n1 - n2

# Multiplicação de valores inseridos pelo usuario
mult = n1 * n2

# Divisão dos valores inseridos pelo usuario
div = n1 / n2

# Exponenciação dos valores entrados pelo usuario
expo = n1 ** n2

# Mostrando o resultado Final ao Usuario
print("Olá",nome,"aqui em baixo estao seus resultados!")
print(" A soma é {}, \n A subtração é {},\n O produto da multiplicação é {}\n A divisão é {:.3f}\n Exponeciação é {}".format(soma, sub, mult, div, expo))