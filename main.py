from mail_client.mail import Mail
from mail_client.get_mails import get_mails_from_server
from load_env import load_sender_filter, load_subject_filter
from gui.app import App
from datetime import datetime
import time
import threading
import os

gui_thread = None
app = None


def main():
    # Start Gui Thread
    if __name__ == "__main__":
        app = App()
        gui_thread = threading.Thread(target=app.start_application)
        gui_thread.start()
        time.sleep(2) # Wait for GUI to start -> to avoid problems accessing app's attributes

    while True:
        mails = get_mails_from_server()

        if mails:
            for mail in mails: 
                printMail(mail)
                if (load_subject_filter() in mail.subject and load_sender_filter() in mail.sender):
                    app.update_content(mail.parse_content())

        if (gui_thread.is_alive()): # when gui is closed, kill the whole program
            time.sleep(10)
        else:
            print("Programm wird beendet, weil GUI beendet wurde am " + datetime.now().strftime("%d.%m.%Y um %H:%M:%S"))
            exit(1)


def printMail(mail):
    print()
    print("-----------------------------------")
    print("Neue Mail empfangen am " + datetime.now().strftime("%d.%m.%Y um %H:%M:%S"))
    print("-----------------------------------")
    print("Sender:", mail.sender)
    print("Betreff:", mail.subject)
    print("Inhalt:", mail.content)
    print("-----------------------------------")
    print()


main()
