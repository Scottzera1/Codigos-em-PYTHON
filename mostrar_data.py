dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

data_formatada = "{:02d}/{:02d}/{:04d}".format(dia, mes, ano)
print("você nasceu na data de:", data_formatada)