# Declarando variaveis e dando o comando de saida
nota1 = float(input("Insira a primeira nota:"))
nota2 = float(input(" Segunda nota:"))

# Calculo da media do aluno
media = (nota1 + nota2)/2
print(" A média entre {:.1f} e {:.1f} ficou com a média de {:.1f}".format(nota1, nota2, media))