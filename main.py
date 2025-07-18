from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import pygame  # Módulo para emitir sons no Windows

email = input("Digite seu email: ")
senha = input("Digite sua senha: ")

def beep():
    # Emitindo um aviso sonoro
    pygame.init()
    pygame.mixer.music.load("beep_sound.mp3")  # Arquivo de som de aviso
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue  # Aguarda o som terminar de ser reproduzido
    time.sleep(0.1)


# Função para verificar se a palavra "Esgotado" está presente na página
def verificar_pagina(url):
    # Configurando as opções do Chrome para o modo headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ativa o modo headless
    chrome_options.add_argument("--disable-gpu")  # Opcional, melhora estabilidade no modo headless

    # Configurando o driver do Chrome (ou o navegador de sua preferência)
    driver = webdriver.Chrome()
    driver.get(url)

    # Aguarda 1 segundo para a página carregar completamente
    time.sleep(1)

    if "Fazer login" in driver.page_source:
        driver.execute_script("btn_login()")
        txtEmail = driver.find_element(By.ID, "email_login")
        txtEmail.send_keys(email)
        txtSenha = driver.find_element(By.ID, "password_login")
        txtSenha.send_keys(senha)
        botaoAcesso = driver.find_element(By.LINK_TEXT, "Acessar")
        botaoAcesso.click()
    
    # Verifica se a palavra "Esgotado" está presente no corpo da página
    a = 0
    time.sleep(1)
    while True:
        if "Escolha uma opção" in driver.page_source:
            print("Aguardando você selecionar o dia na página...")
            # Aguarda até que 'Esgotado' apareça na página, sem dar refresh
            while "Esgotado" not in driver.page_source:
                time.sleep(1)
            print("Agora a opção 'Esgotado' apareceu!")

        if "Esgotado" in driver.page_source:
            if(a%2 == 0):
                print("Esgotado...")
            else:
                print("Esgotado..")
            a += 1
            driver.refresh()
        else:
            qtdIngressos = driver.find_element(By.ID, "EventoInscricaoCarrinho_0_quantidade")
            selecionar = Select(qtdIngressos)
            selecionar.select_by_value("1")

            driver.maximize_window()
            print("LIBEROU INGRESSO!!!")
            print("O site foi atualizado", a, "vezes...")

            botao = driver.find_element(By.XPATH, "//button[contains(@class, 'bt-submit')]")
            botao.click()

            while True:
                beep()

# URL da página a ser verificada
url = 'https://www.ingressolive.com/arquibancada_uberlandia'

verificar_pagina(url)