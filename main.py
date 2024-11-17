from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re

buscador = input("Digite o produto que procura: ")



navegador = webdriver.Chrome()
navegador.maximize_window()

# Pesquisa no Google
navegador.get("https://www.google.com/")
pesquisar = navegador.find_element(By.CLASS_NAME, "gLFyf")
pesquisar.send_keys(buscador)
pesquisar.send_keys(Keys.ENTER)
time.sleep(2)

# Captura os elementos de produtos
produtos = navegador.find_elements(By.XPATH, "//div[contains(@class, 'mnr-c c3mZkd pla-unit')]//a[@aria-label]")

lista = []

# Extração de informações de cada produto
for item in produtos:
    nome_preco = item.get_attribute('aria-label')  # Nome e preço do produto
    link = item.get_attribute('href')  # Link do produto
    lista.append(nome_preco)
    lista.append(link)

for i in range(0, len(lista), 2):
    produto = lista[i]
    link = lista[i + 1]

    if "por R$" in produto:
        nome = produto.split(" por R$")[0].strip()
        valor = produto.split(" por R$")[1].strip()
        
        print(f'{valor},\n{link}\n{'-----'*40}')


navegador.quit()
