import pyautogui
from time import sleep

# 1 - clicar e digitar usuário
pyautogui.click(966, 538, duration=2)
pyautogui.write('livo')
sleep(1)

# 2 - clicar e digitar senha
pyautogui.click(975, 571, duration=2)
pyautogui.write('1234')
sleep(1)

# 3 - clicar no botão de login
pyautogui.click(878, 602, duration=2)
sleep(2)  # Espera a tela carregar

# 4 - abrir arquivo e registrar produtos
with open('produtos.txt', 'r') as file:
    for linha in file:
        # Separar e limpar os dados
        dados = linha.strip().split(',')
        if len(dados) < 3:
            continue  # ignora linhas inválidaslivo

        produto = dados[0].strip()
        quantidade = dados[1].strip()
        preco = dados[2].strip()

        # 1 - clicar e digitar o produto
        pyautogui.click(689, 526, duration=1)
        pyautogui.write(produto)
        sleep(0.5)

        # 2 - clicar e digitar a quantidade
        pyautogui.click(680, 553, duration=1)
        pyautogui.write(quantidade)
        sleep(0.5)

        # 3 - clicar e digitar o preço
        pyautogui.click(683, 576, duration=1)
        pyautogui.write(preco)
        sleep(0.5)

        # 4 - clicar em registrar
        pyautogui.click(587, 736, duration=1)
        sleep(1)  # espera registrar antes de ir para o próximo
