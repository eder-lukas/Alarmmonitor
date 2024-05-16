# Alarmierungsmail Aufbau
Die Alarmierungsmail muss wie Folgt aufgebaut sein:

Keyword: Inhalt
Keyword: Inhalt
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