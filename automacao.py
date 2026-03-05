import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla000251  hashtag
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 1

# Passo 1: Abrir o navegador e entrar no site de login
pyautogui.hotkey("command", "space")
time.sleep(0.5)
pyautogui.write("safari")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Passo 2: Fazer login
time.sleep(4)
pyautogui.click(x=728, y=365)
pyautogui.write("devpython@hashtag.com")
pyautogui.press("tab")
pyautogui.write("python123")
pyautogui.press("enter")

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

time.sleep(2)

# Passo 4: Cadastrar os produtos
for linha in tabela.index:
    pyautogui.click(x=726, y=254)

    # Código do produto
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Marca do produto
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    # Tipo de produto
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # Categoria do produto
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # Preço do produto
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    # Custo do produto
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    # Observações do produto
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.scroll(5000)
    pyautogui.click(x=837, y=904)

    # Enviar o produto cadastrado
    pyautogui.scroll(5000)