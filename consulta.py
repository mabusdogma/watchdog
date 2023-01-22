#!/bin/env python3
import os, re, time, pyautogui, datetime, pyperclip

ahora = datetime.datetime.now()
log= "/usr/share/hassio/homeassistant/pyscript/consulta.csv"
nie='Y0841924T'
exp='R519486'
year='2021'
resp1='error'
resp2='error'

pyautogui.FAILSAFE = False

try:
    pyautogui.click(90, 755)
    time.sleep(8)
    pyautogui.typewrite('https://sede.mjusticia.gob.es/eConsultas/inicioNacionalidad')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.typewrite(nie)
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.typewrite(exp)
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.typewrite(year)
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(275, 580)
    time.sleep(0.2)
    pyautogui.dragTo(1000, 620, button='left')
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    resp=pyperclip.paste()
    pyautogui.hotkey('alt', 'f4')
    resp = resp.split("\n\n")
    resp1=resp[0].replace('.', '').strip()
    resp2=resp[1].replace('.', '').replace('Su expediente se encuentra ', '').strip()
    print(f'{ahora.strftime("%d/%m/%Y")},{resp1},{resp2}\n')
    with open(log, "a") as o:
        o.write(f'{ahora.strftime("%d/%m/%Y")},{resp1},{resp2}\n')   
except:
    pyautogui.hotkey('alt', 'f4')
    time.sleep(8)
    pyautogui.click(90, 755)
    time.sleep(8)
    pyautogui.typewrite('https://sede.mjusticia.gob.es/eConsultas/inicioNacionalidad')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.typewrite('04')
    time.sleep(0.1)
    pyautogui.typewrite('29')
    time.sleep(0.1)
    pyautogui.typewrite('1984')
    time.sleep(0.1)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.typewrite(nie)
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.typewrite(exp)
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.typewrite(year)
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(275, 580)
    time.sleep(0.2)
    pyautogui.dragTo(1000, 620, button='left')
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    resp=pyperclip.paste()
    pyautogui.hotkey('alt', 'f4')
    time.sleep(0.2)
    pyautogui.hotkey('alt', 'f4')
    resp = resp.split("\n\n")
    resp1=resp[0].replace('.', '').strip()
    resp2=resp[1].replace('.', '').replace('Su expediente se encuentra ', '').strip()
    with open(log, "a") as o:
        o.write(f'{ahora.strftime("%d/%m")},{resp1},{resp2}\n')
