import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

LARGE_FONT = ("Verdana", 12)

class MP3Player(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        tk.Tk.wm_title(self,"CST-205-Project3")
        container.pack(side = "top", fill  = "both", expand = True)

        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)

        self.frames = {}
        f = StartPage
        frame = f(container, self)
        self.frames[f] = frame
        frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        def Play():
            global URLin
            URLin = url_entry.get()
            print(URLin)
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "MP3Player", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        size_label = ttk.Label(self,text = "Play", font = LARGE_FONT)
        size_label.place(x = 40, y = 20)

        submit1 = ttk.Button(self,text = "Play", command = Play)
        submit1.place(x = 40, y = 25)






app = MP3Player()
app.geometry("500x500")
app.mainloop()
