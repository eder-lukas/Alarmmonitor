from mailClient.mail import Mail
from mailClient.getMails import getUnseenMails
from gui.app import App
import time
import threading

gui_thread = None
app = None



def main():
    if __name__ == "__main__":
        app = App()
        gui_thread = threading.Thread(target=app.start_application)
        gui_thread.start()
        time.sleep(2)

    test_counter = 1

    while True:
        mails = getUnseenMails()
        for mail in mails: 
            print("-----------------------------------")
            print("Sender:", mail.sender)
            print("Betreff:", mail.subject)
            print("Inhalt:", mail.content)
            print("-----------------------------------")
        app.update_content(str(test_counter))
        test_counter = test_counter + 1
        time.sleep(10)  # Warten Sie 10 Sekunden, bevor Sie erneut überprüfen


main()


#namenskonvention