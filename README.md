
# Watchdog / Restart weekly

Python scripts for Linux. They check Home Assistant supervised and internet connection, to restart server / router if necessary, and make a weekly restart of the server and router.

Scripts de python para Linux. Revisan la conexión de Home Assistant supervised y de internet, para reiniciar el router o el servidor si es necesario, y reinician semanalmente el servidor y el router.

Watchdog revisa periodicamente la conexión a internet y que se pueda acceder a Home Assistant. En caso necesario, intentará reiniciar (en este orden) el servicio de Home Assistant, el servidor, o la conexión a internet (es decir, reiniciar el router).

Weekly restart realiza un reinicio del router y, con un minuto de pausa, reinicia el servidor de Home asistant, para limpiar memoria.

Los archivo watchdog.py y weekly_restart.py se pueden programar con crontab para usarse automáticamente.

Los archivo watchdog.csv y weekly_restart.csv guardan toda la información creada cada vez que crontaba los activa.

En este ejemplo de crontab, watchdog se activa cada hora y weekly restart a las 5hrs del sábado:

```
XAUTHORITY=/home/<user>/.Xauthority
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
DISPLAY=:0

0 * * * * watchdog.py >> watchdog.csv
* 5 * * 6 weekly_restart.py >> log_weekly_restart.csv
```

Si se colocan los csv como se indica aqui https://www.home-assistant.io/integrations/file/#sensor se tendrá la información actualizada en Home Assistant.

Debido a que los scripts utilizan pyautogui, es necesario incluir en el archivo crontab al menos Xauthority, PATH y DISPLAY (cambiar <user> por usuario), si no se incluye esta información, no funcionará el reinicio del router.

Se deja un ejemplo de los archivos bash que se utilizarán para ejecutar las órdenes de crontab, también es necesario en ellos cambiar <user> por usuario de Linux.

Se puede utizar el archivo clics.py para crear una "macro", y saber donde dar clics para entrar a la página del router y reiniciarlo (por si telnet está bloqueado en el router).
