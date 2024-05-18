# Alarmierungsmail Aufbau
Die Alarmierungsmail muss wie Folgt aufgebaut sein:

Keyword; Inhalt
Keyword; Inhalt
...

Dieser Aufbau wird dann in einer tabellarischen Übersicht dargestellt.


# Alarmmonitor Environment
Es muss eine alarmmonitor.env Datei im Root-Verzeichnis geben (selbe Ebene wie main.py).
Die Datei wird nicht über das Git-Repo mit verteilt und muss somit manuell nach dem folgenden Muster erstellt und angepasst werden.

> EMAIL_ADDRESS=deine.email@beispiel.com
> EMAIL_PASSWORD=deinpasswort
> IMAP_SERVER_ADDRESS=imap.beispiel.net
> 
> FILTER_EMAIL_SENDER=@beispiel2.com
> FILTER_EMAIL_SUBJECT=Alarmierung

Filter Werte können auch leer sein. Dafür einfach neben dem '=' nichts ausfüllen
Die Filter-Werte müssen nicht genau mit den tatsächlichen Werten übereinstimmen. 
Es wird also bei einem Filter für @beispiel2.com eine Mail von asdf@beispiel2.com und auch eine Mail von asdf@beispiel2.comm akzeptiert. Analog ist das Verfahren mit dem Betreff.


# Raspberry setup
Im Terminal: 
sudo apt-get update && sudo apt-get upgrade

Klone das Git-Repo

Lege alarmmonitor.env in dem Ordner an und befülle die Datei (siehe oben)

## Virtuelle Umgebung erstellen: 
Im Terminal:
cd /root-folder-of-alarmmonitor
python -m venv venv
source venv/bin/activate
pip install python-dotenv tkintermapview
python main.py

Anwendung sollte gestartet haben
-> kann wieder beendet werden

Im Terminal:
deactivate

## Autostart für Alarmmonitor
Im Terminal: 
Touch ~/Desktop/Alarmmonitor.sh
chmod +x Alarmmonitor.sh

# noch ändern!!
Datei bearbeiten:  
#!/bin/bash

sleep 10

LOGFILE=/home/FFSinning/Desktop/cronjob.log
echo "Cronjob started at $(date)" >> LOGFILE

export PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
export DISPLAY=:0

xhost +SI:localuser:FFSinning (brauchts evtl garnich)

source /Path-to-Alarmmonitor/venv/bin/activate
python /Path-to-Alarmmonitor/main.py
deactivate


Im Terminal:
crontab -e

Zeile hinzufügen:

@reboot ~/Desktop/Alarmmonitor.sh &


Fertig :)