
import pyautogui

import time

""" pyautogui.alert('O código vai começar.Não utiliza nada do computador')

pyautogui.PAUSE = 0.5

pyautogui.press("Winleft")

#Abrir pagina do senai zerbini

pyautogui.write('https://campinaszerbini.sp.senai.br/')
pyautogui.press('enter')
time.sleep(25)
pyautogui.alert("O código foi finalizado.Você já pode utilizar o computador normalmente") """

x,y = pyautogui.position()
time.sleep(2)
print('posição atual do mouse : ')
print("x = "+str(x) + " y = "+str(y))