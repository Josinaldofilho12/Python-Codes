# Passo 1: Instalar o pyautogui
import pyautogui
import time
# Importar a base de dados
import pandas
tabela = pandas.read_csv('produtos.csv')
print(tabela)
# Passo 2: Abrir o navegador
pyautogui.PAUSE = 0.8
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(x=686, y=605)
# Passo 3: Fazer login no sistema
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
pyautogui.click(x=699, y=606)
time.sleep(2)
pyautogui.write('pythoneirotreinamento@outlook.com.br')
pyautogui.press('tab')
pyautogui.write('python')
pyautogui.press('tab')
pyautogui.press('enter')
# Passo 4: Cadastrar 1 produto
pyautogui.click(x=733, y=444)
linha = 0
# Para cada linha da minha tabela
for linha in tabela.index:
    # Para selecionar o 1º campo
    pyautogui.click(x=733, y=444)
    # codigo
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    # marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')
    # tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')
    # categoria
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    # preco unitario
    preco = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco))
    pyautogui.press('tab')
    # custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')
    # obs
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')
    # Clicar no botão enviar
    pyautogui.press('enter')
    pyautogui.scroll(5000)
# Passo 5: Repetir o processo de cadastro para todos os produtos