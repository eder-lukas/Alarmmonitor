from mailClient.mail import Mail
from mailClient.getMails import getUnseenMails
from gui.app import App
import time


def main():
    if __name__ == "__main__":
        app = App()
        app.start_application("Alarmmonitor Anzeige")
        time.sleep(2)
        app.update_content("Test1234")

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


#namenskonvention