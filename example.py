import time
import pyotp
import threading
from tkinter import Tk, Label

totp = pyotp.TOTP('{AUTH_CODE_APP}')
cotp = ""

window = Tk()
window.title("Your OTP Code")
window.geometry('250x100')

lbl = Label(window, text=totp.now(), font=("Consolas", 50), padx=10, pady=5)
lbl.grid(column=0, row=0)


def GET_OTP():
    while True:
        time.sleep(1)

        global cotp
        if cotp != totp.now():
            cotp = totp.now()
            lbl.configure(text=totp.now())


thread = threading.Thread(target=GET_OTP)
thread.setDaemon(True)
thread.start()

window.mainloop()
