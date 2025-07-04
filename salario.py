salario = float(input("Informe o seu salário: "))

if salario <= 3000:
    print("Programador Júnior")

elif salario > 3000 and salario <= 6000:
    print("Programador Pleno")

elif salario > 6000 and salario <= 10000:
    print("Programador Sênior")

else:
    print("Programador Master")
# O código acima classifica o salário de um programador em diferentes níveis
# de acordo com os valores informados. Se o salário for menor ou igual a 3000,
# o programador é classificado como Júnior. Se estiver entre 3000 e 6000,
# é classificado como Pleno. Se estiver entre 6000 e 10000, é classificado como Sênior.
# Se o salário for maior que 10000, é classificado como Master.
# Essa estrutura condicional permite categorizar os programadores com base em seus salários.
