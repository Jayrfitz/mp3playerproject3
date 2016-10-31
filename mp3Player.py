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
            print("play")

        def Pause():
            print("Pause")

        def Browse():
            global filePath
            filename = filedialog.askopenfilename()
            filePath = filename
            file_label = ttk.Label(self,text = filePath, font = LARGE_FONT)
            file_label.place(x = 0, y = 325)

            print(filePath)

        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "MP3 Player", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        play = ttk.Button(self,text = "Play", command = Play)
        play.place(x = 40, y = 40)

        pause = ttk.Button(self,text = "Pause", command = Pause)
        pause.place(x = 160, y = 40)

        pg = ttk.Progressbar(self, orient='horizontal',length=300, mode='determinate')
        pg.place(x = 40, y = 70)



        FileBrowse = ttk.Button(self,text = "Browse",command = Browse)
        FileBrowse.place(x = 40, y= 100)





app = MP3Player()
app.geometry("500x200")
app.mainloop()
