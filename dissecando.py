#Declaracao de variavel(is)#
mostre = input("Digite algo aqui:")

#Aqui só mostra#
print(mostre)

#Verifica o tipo#
print("Qual é o tipo primitivo desse algo:", type(mostre))

#Verifica a posssibilidade de espaço#
print("tem espaços?!", mostre.isspace())

#Verifica se ele é numerico#
print("É um número?", mostre.isnumeric())

#Verifica se ele alfabetico#
print("O algo digitado é albetico?", mostre.isalpha())

#Verifica se é Alfanumerico#
print("É Alfanumerico?", mostre.isalnum())

#Vericando se está em Maiúscula
print("Está em caixas Altas ou em Maiúsculas?", mostre.isupper())

#Verificando agora se está em Minúscula
print(" Estão em caixas pequenas ou Minúsculas?", mostre.islower())

#Verifica se esta tudo em Maiúsculo ou em Minúsculo senao estiver vai dar que está capitalizada#
print("Está capitalizada o algo?", mostre.istitle())