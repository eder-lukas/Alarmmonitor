from .mail import Mail
from load_env import load_mail, load_password, load_imap_server_address
import imaplib
import email

def get_unseen_mails() -> list[Mail]:
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