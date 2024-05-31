from .mail import Mail
from .connection_check import connected_to_internet
from load_env import load_mail, load_password, load_imap_server_address
from datetime import datetime
import imaplib
import email


connection_established = False # variable to store connection status to avoid fleeding the log file

def get_mails_from_server():
    global connection_established
    mails = None
    if (connected_to_internet()):
        try: # get mails in try except -> otherwise program will crash when the internet connection is interrupted
            mails = _get_unseen_mails()
        except:
            if connection_established == True:
                print("Failed to get Mails on " + datetime.now().strftime("%d.%m.%Y at %H:%M:%S"))
                connection_established = False
    else:
        if (connection_established == True):
            print("Lost internet connection on " + datetime.now().strftime("%d.%m.%Y at %H:%M:%S"))
            connection_established = False
        
    if (mails != None and connection_established == False): # connection was lost and is there again or first connection after program start
        print("Connected to Internet on " + datetime.now().strftime("%d.%m.%Y at %H:%M:%S"))
        connection_established = True

    return mails


def _get_unseen_mails() -> list[Mail]:
    # Verbindung zum IMAP-Server herstellen
    mail = imaplib.IMAP4_SSL(load_imap_server_address())
    mail.login(load_mail(), load_password())  
    
    # Postfach auswählen
    mail.select('inbox')

    # Suche nach neuen ungelesenen E-Mails
    result, data = mail.search(None, 'UNSEEN')

    # Liste der ungelesenen E-Mail-IDs erhalten
    unread_emails = data[0].split()
    mails = []

    if unread_emails:
        for email_id in unread_emails:
            # E-Mail abrufen
            reuslt, data = mail.fetch(email_id, "(RFC822)")
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)

            subject, sender, content = _get_email_content(msg)
            message = Mail(sender, subject, content)
            mails.append(message)

    # Verbindung trennen
    mail.logout()
    return mails


def _get_email_content(msg):
    subject = msg["Subject"]
    sender = msg["From"]
    
    # Inhalte der E-Mail extrahieren
    if msg.is_multipart():
        # Falls es sich um eine multipart-Nachricht handelt (z.B. mit Anhängen)
        content = ""
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                content += part.get_payload(decode=True).decode("utf-8")
    else:
        # Wenn es sich um eine einfache Nachricht handelt
        content = msg.get_payload(decode=True).decode("utf-8")
    
    return subject, sender, content