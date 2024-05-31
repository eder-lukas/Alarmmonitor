# Alarmierungsmail Aufbau
Die Alarmierungsmail muss wie Folgt aufgebaut sein:

Keyword; Inhalt
Keyword; Inhalt
...

Dieser Aufbau wird dann in einer tabellarischen Übersicht dargestellt.

# Aufbau, um Adresse in Karte anzuzeigen
Um die Adresse der Alamierung in der Karte anzuzeigen müssen die folgenden Keywords in der genannten Reihenfolge vorhanden sein.
Es dürfen dabei andere Keywords dazwischen vorkommen.

Strasse; ...
Hausnummer; ...
PLZ; ...
Ort; ...

Wenn dieser Aufbau bei Ihnen nicht zutrifft, kann die Verarbeitung der Inhalts zur Adresse in der Datei mail.py -> get_address_from_content angepasst werden.
Falls die Adresse nicht aufgelöst werden kann, ändert sich an der Karte nichts. Der Text wird dennoch angezeigt.

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

## Bildschirmschoner deaktivieren:
Im Terminal mit 
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
Datei /etc/xdg/lxsession/LXDE-pi/autostart öffenen und folgende Zeilen hinzufügen:

@xset s off
@xset -dpms
@xset s noblank


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

->Datei bearbeiten:  
#!/bin/bash

sleep 15

LOGFILE=/home/FFSinning/Desktop/alarmmonitor.log
echo "Cronjob started at $(date)" >> LOGFILE

export PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
export DISPLAY=:0

xhost +SI:localuser:FFSinning (eventuell nicht benötigt)

source /Path-to-Alarmmonitor/venv/bin/activate >> $LOGFILE 2>&1
python -u /Path-to-Alarmmonitor/main.py >> $LOGFILE 2>&1
deactivate
echo "Cronjob ended at $(date)" >> $LOGFILE


Im Terminal:
crontab -e

Zeile hinzufügen:

@reboot ~/Desktop/Alarmmonitor.sh &


Fertig :)