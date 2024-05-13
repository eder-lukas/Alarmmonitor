from mailClient.mail import Mail
from mailClient.getMails import getUnseenMails
import time


def main():
    while True:
        mails = getUnseenMails()
        for mail in mails: 
            print("-----------------------------------")
            print("Sender:", mail.sender)
            print("Betreff:", mail.subject)
            print("Inhalt:", mail.content)
            print("-----------------------------------")
        time.sleep(10)  # Warten Sie 10 Sekunden, bevor Sie erneut überprüfen


main()