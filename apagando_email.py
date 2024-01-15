#importando biblioteca
from ssl import CERT_OPTIONAL
import pyautogui
import time


# pausa de 1 segundo
pyautogui.PAUSE = 1

# pressionar tecla win do teclado
pyautogui.press('Win')

# escrever chrome
pyautogui.write('chrome')

# pressionar enter
pyautogui.press('Enter')

# variavel com o endereco que acessaremos
link = "https://mail.google.com/mail/u/0/#inbox"

# escrevendo o link = "https://dlp.hashtagtreinamentos.com/ da pagina
pyautogui.write(link) 

#pressionando enter
pyautogui.press('Enter')

#esperar 3 segundos
time.sleep(3)

for i in range(1,50):
    time.sleep(2)
    #clicando e selecionando emails
    pyautogui.click(x=839, y=528)

    #excluindo emails
    pyautogui.click(x=1302, y=524)