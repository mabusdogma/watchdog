#!/bin/env python3

import http.client as httplib
from urllib.request import urlopen
import time, os

def restart_router():
    import pyautogui
    import time
    pyautogui.FAILSAFE = False

    #entra a firefox
    pyautogui.click(90, 755)
    time.sleep(2)

    #ip del router
    pyautogui.typewrite('http://192.168.1.1/')
    time.sleep(0.1)
    pyautogui.press('right')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(2)

    #se entra a pagina del router
    pyautogui.press('down')
    time.sleep(.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('tab', presses=2)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(2.5)

    # va a pagina para reiniciar el router
    pyautogui.press('tab', presses=2)
    time.sleep(0.2)
    pyautogui.press('tab', presses=2)
    time.sleep(0.2)
    pyautogui.press('tab', presses=2)
    time.sleep(0.2)
    pyautogui.press('tab')
    pyautogui.typewrite('http://192.168.1.1/getpage.gch?pid=1002&nextpage=manager_dev_conf_t.gch')
    pyautogui.press('enter')
    time.sleep(1)

    #activa el reinicio
    pyautogui.press('tab')
    time.sleep(0.1)
    pyautogui.press('tab')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.press('left')
    time.sleep(0.1)
    pyautogui.press('enter')
    print('     -- Se reinicia router')  

def restart_server():
    print ('     --Se reinicia servicio de HA')
    os.system('systemctl restart hassio-supervisor.service')
    time.sleep(10) 
    try:
        urlopen("http://localhost:8123")
        print('     -- HA vuelve a su normalidad!')
    except Exception:
        print('     --Intento fallido, se reinicia servidor...')
        os.system('reboot')

def main():

#se revisa si HA esta funcionando
    try:
        urlopen("http://localhost:8123")
        print('     -- HA OK')
    except Exception:
        print('     -- No HA!')
        restart_server()

#se revisa conexión a internet
    conn = httplib.HTTPSConnection("8.8.8.8", timeout=5)
    try:
        conn.request("HEAD", "/")
        print('     -- Internet OK')
        exit()
    except Exception:
        print('     -- No internet!')
        restart_router()
        exit()
        
if __name__== "__main__" :
    main()