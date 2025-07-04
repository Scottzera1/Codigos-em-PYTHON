# fluxo de caixa
# Este programa permite adicionar entradas e saídas de dinheiro, 
# calcular o total e exibir um relatório de fluxo de caixa.
# O usuário pode adicionar entradas e saídas, e o programa calcula o total.
# Fluxo de Caixa
fluxo_caixa = []

def adicionar_entrada():
    nome = input("Digite seu nome: ")
    valor = float(input("Digite o valor da entrada: "))
    fluxo_caixa.append(valor)
    print(f"Entrada de R$ {valor:.2f} adicionada com sucesso!")

def adicionar_saida():
    nome = input("Digite seu nome: ")
    valor = float(input("Digite o valor da saída: "))
    fluxo_caixa.append(-valor)  # saída é negativa
    print(f"Saída de R$ {valor:.2f} registrada com sucesso!")

# Loop principal
while True:
    print("\n--------------------------")
    print("@ Fluxo de Caixa")
    print("--------------------------")
    print("1 - Adicionar entrada")
    print("2 - Adicionar saída")
    print("3 - Encerrar")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar_entrada()
    elif opcao == '2':
        adicionar_saida()
    elif opcao == '3':
        break
    else:
        print("Opção inválida. Tente novamente.")

# Relatório final
print("\n=== RELATÓRIO FINAL ===")
total = 0
for valor in fluxo_caixa:
    print(f"{'Entrada' if valor >= 0 else 'Saída '} de R$ {abs(valor):.2f}")
    total += valor

print(f"\nSaldo final: R$ {total:.2f}")
