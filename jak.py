#!/bin/env python3
import subprocess, time, datetime
log= "/usr/share/hassio/homeassistant/pyscript/jak.csv"
ahora = datetime.datetime.now()


def repite():

    with open("/home/ha/jak_log.txt", "r") as c:
        resultado = int(c.read()[-2])
    
    with open('/home/ha/jak.txt', 'r') as d:
        actual = d.read()

    episodios=0
    while resultado > 0:
        episodios+=1
        #almacena la proxima busqueda en txt
        siguiente = int(actual)+1
        #y modifica los archivos
        with open('/home/ha/jak.txt', 'w') as h:
            h.write(str(siguiente))
        with open('/home/ha/jak.sh', 'w') as f:
            f.write(f'raincoat "jak {str(siguiente)}"')

        time.sleep(2)
        subprocess.Popen(['sh','/home/ha/jak.sh'])
        time.sleep(10)

        with open('/home/ha/jak.txt', 'r') as d:
            actual = d.read()
        with open("/home/ha/jak_log.txt", "r") as c:
            resultado = int(c.read()[-2])
    with open(log, "a") as o:
        o.write(f'{ahora.strftime("%d/%m")}, {episodios} nuevo(s): {int(actual)-1}\n')
        
def main():
    subprocess.Popen(['sh','/home/ha/jak.sh'])
    time.sleep(10)
    repite()


if __name__== "__main__" :
    main()
