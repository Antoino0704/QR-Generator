import tkinter as tk
from tkinter import filedialog as fd
import pyqrcode
import png

class QrGenerator:
    def __init__(self, sito):
        self.codeQR = pyqrcode.create(sito)

    def save(self):
        path = fd.asksaveasfilename(defaultextension='.png')
        self.codeQR.png(path, scale=6)

class Win:
    def __init__(self, win):

        self.initVariable()
        
        lab = tk.Label(win, text='inserisci indirizzo sito')
        lab.grid(row=1, column=1)

        lab2 = tk.Label(win, textvariable=self.stato)
        lab2.grid(row=2, column=2, padx=10)

        entry = tk.Entry(win, textvariable=self.site)
        entry.grid(row=2, column=1, pady=10)

        button = tk.Button(win, text='genera codice QR', command=self.generator)
        button.grid(row=3, column=1, pady=10)

        self.sponsor(win)

    def generator(self):
        qr = QrGenerator(str(self.site.get()))
        qr.save()
        self.stato.set('QR code generato')

    def initVariable(self):
        self.site = tk.StringVar()
        self.stato = tk.StringVar()
        self.stato.set('QR code non generato')

    def sponsor(self, win):
        lab_sponsor = tk.Label(win, text='By Buscarino Antonino', font=('', 15))
        lab_sponsor.place(x=60, y=150)


win = tk.Tk()
win.geometry('300x200')
win.title('QR GENERATOR')
win.resizable(False, False)
win.iconbitmap('Images/icon.ico')

window = Win(win)

win.mainloop() 
