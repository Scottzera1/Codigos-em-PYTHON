# Lista de produtos Apple e seus preços
produtos = [
    {"nome": "iPhone 15", "preco": 7299.00},
    {"nome": "MacBook Air M2", "preco": 10999.00},
    {"nome": "iPad 10ª geração", "preco": 4999.00},
    {"nome": "Apple Watch Series 9", "preco": 3999.00},
    {"nome": "AirPods Pro 2", "preco": 1899.00}
]

# Métodos de pagamento populares no Brasil
pagamentos = ["Pix", "Cartão de Crédito", "Boleto"]

# Exibir lista de produtos
print("=== Lista de Produtos Apple ===")
for i, produto in enumerate(produtos):
    print(f"{i + 1} - {produto['nome']} - R$ {produto['preco']:.2f}")

# Escolher produto
escolha_produto = int(input("Escolha o número do produto que deseja comprar: ")) - 1

# Verifica se o número é válido
if escolha_produto < 0 or escolha_produto >= len(produtos):
    print("Produto inválido.")
    exit()

produto_escolhido = produtos[escolha_produto]

# Exibir métodos de pagamento
print("\n=== Formas de Pagamento ===")
for i, metodo in enumerate(pagamentos):
    print(f"{i + 1} - {metodo}")

escolha_pagamento = int(input("Escolha o número da forma de pagamento: ")) - 1

# Verifica se a forma de pagamento é válida
if escolha_pagamento < 0 or escolha_pagamento >= len(pagamentos):
    print("Forma de pagamento inválida.")
    exit()

metodo_escolhido = pagamentos[escolha_pagamento]
valor = produto_escolhido['preco']

# Processamento de pagamento
print("\n=== Resumo da Compra ===")
print(f"Produto: {produto_escolhido['nome']}")
print(f"Preço: R$ {valor:.2f}")
print(f"Forma de Pagamento: {metodo_escolhido}")

# Parcelamento para Cartão ou Boleto
if metodo_escolhido == "Cartão de Crédito":
    parcelas = int(input("Deseja parcelar em quantas vezes? (1 a 16): "))
    if parcelas < 1 or parcelas > 16:
        print("Número de parcelas inválido.")
        exit()
    juros_mensal = 0.02
    parcela_com_juros = (valor * (1 + juros_mensal) ** parcelas) / parcelas
    total_com_juros = parcela_com_juros * parcelas
    print(f"\nParcelado em {parcelas}x de R$ {parcela_com_juros:.2f} (com juros de 2% ao mês)")
    print(f"Total com juros: R$ {total_com_juros:.2f}")

elif metodo_escolhido == "Boleto":
    parcelas = int(input("Deseja parcelar em quantas vezes? (1 a 24): "))
    if parcelas < 1 or parcelas > 24:
        print("Número de parcelas inválido.")
        exit()
    parcela = valor / parcelas
    print(f"\nParcelado em {parcelas}x de R$ {parcela:.2f} (sem juros)")
    print(f"Total: R$ {valor:.2f}")

else:
    print("\nPagamento à vista via Pix.")
    print(f"Total: R$ {valor:.2f}")
