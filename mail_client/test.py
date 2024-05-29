from mail import Mail, parse_string_to_dict

def test_parse_content():
    content = """Schlagwort; #T2410#Rettung#Wohnung öffnen akut
Stichwort; RD 1/THL P EINGESCHLOSSEN
Bemerkung; MTT ist der Nachbar
schreit um Hilfe
laut MTT sonst anscheinend niemand bei ihr zuHause

Strasse; Böhmerwaldstraße
Hausnummer; 4
PLZ; 86697
Ort; Oberhausen bei Neuburg a d Donau
Ortsteil; Sinning - Oberhausen b Neuburg a d Donau
Abschnitt;
Einsatzmittel; Florian Oberhausen 40/1
Mitteiler; Taubert, Koordinate: (11:6:40,48:42:9)
Mitteiler Kontakt;
Alarmdatum; 28.05.2024 23:03:46
Objekt; 23:04:01 28.05.2024


*** Dies ist eine automatisch generierte Nachricht, eine Antwort darauf ist nicht möglich! ***"""

    mail = Mail("noreply@fitt-gmbh.de", "PowerAlarmMeldung", content)
    content_dict = mail.parse_content_2()
    print(content_dict)


test_parse_content()