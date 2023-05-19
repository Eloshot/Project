from tkinter import *
from tkinter import ttk
import qrcode
from PIL import ImageTk, Image, ImageChops
import os

# Seadistan akna
win = Tk()
win.title("Projekt - QR koodi generaator")
win.geometry("500x500")
win.eval('tk::PlaceWindow . center')
win.configure(bg='#212529')

stage = Canvas(win, width=500, height=500)
stage.pack()

win.update()


# QR koodi genereerimise funktsioon, mis jookseb, kui on vajutatud genereeri nuppu
def generateQR():
    data = inputValue.get()
    img = qrcode.make(data)
    img.save('QRkood.png')

    img = Image.open('QRkood.png')
    img = img.resize((200, 200), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    stage.create_image((stage.winfo_width() / 2, stage.winfo_height() / 1.5), image=img, anchor='center')
    stage.image = img


# Tekstkasti pealkiri
label = ttk.Label(win, text="Sisesta oma QR koodi link").place(relx=.5, rely=.2, anchor=CENTER)

# Tekstkast
inputValue = StringVar()
input = Entry(win, textvariable=inputValue, width=40, bg="#343A40").place(relx=.5, rely=.3, anchor=CENTER)

# Genereerimis nupp
generateButton = Button(win, text="Genereeri", command=generateQR, bg="#343A40").place(relx=.5, rely=.4, anchor=CENTER)

# QR Koodi pilt

if os.path.isfile('QRkood.png') == 1:
    img = Image.open('QRkood.png')
    img = img.resize((200, 200), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    stage.create_image((stage.winfo_width() / 2, stage.winfo_height() / 1.5), image=img, anchor='center')
    stage.image = img

win.mainloop()

