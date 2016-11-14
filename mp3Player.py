import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from tkinter import *
import os, shutil

LARGE_FONT = ("Verdana", 12)
filePath = []
filelist = []
value = 0
x = 0

class MP3Player(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        tk.Tk.wm_title(self,"MP3 Player")
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

        def Horror():
            print("Prepare for the horror")

        def Happy():
            print("Prepare to for an uplifting happy tune.")

        def Blues():
            print("Prepare for some blues.")

        def Emo():
            print("Prepare for some emo tunes.")
        def Browse():
            global filePath
            global x
            x = 0
            del filelist[:]
            filename = filedialog.askopenfilename()
            filelist.append(filename)
            for i in filelist:
                filePath.append(Label(self,text= i, font = LARGE_FONT))
            for j in filePath:
                j.place(x = 200, y = 250+(x*30))
                x = x + 1
            print (filePath)
            print('\n\n')

        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "Volume", font = LARGE_FONT)
        label.pack(pady = 20, padx = 10)

        labelStartStop = ttk.Label(self, text = "Press start to play audio. Press pause to stop audio.", font = LARGE_FONT)
        labelStartStop.place(x = 20, y = 20)

        labelList = ttk.Label(self, text = "Music Play List: ", font = LARGE_FONT)
        labelList.place(x = 40, y = 220)

        play = ttk.Button(self,text = "Play", command = Play)
        play.place(x = 40, y = 60)

        pause = ttk.Button(self,text = "Pause", command = Pause)
        pause.place(x = 160, y = 60)

        pg = ttk.Progressbar(self, orient='horizontal',length=300, mode='determinate')
        pg.place(x = 40, y = 110)


        FileBrowse = ttk.Button(self,text = "Browse for Music",command = Browse)
        FileBrowse.place(x = 40, y = 250)

        labelChoose = ttk.Label(self,text = "Choose a theme: ", font = LARGE_FONT)
        labelChoose.place(x = 40, y = 150)


        horror = ttk.Button(self,text = "Horror", command = Horror)
        horror.place(x = 40, y = 190)


        happy = ttk.Button(self,text = "Happy", command = Happy)
        happy.place(x = 160, y = 190)

        blues = ttk.Button(self,text = "Blues", command = Blues)
        blues.place(x = 280, y = 190)

        emo = ttk.Button(self,text = "Emo", command = Emo)
        emo.place(x = 400, y = 190)

        Slider1 = Scale(self, orient = HORIZONTAL, length = 100,width = 10, sliderlength = 10, from_ = 0, to = 100).pack()
        #Slider1.place (x = 250, y = 40)


app = MP3Player()
app.geometry("1000x400")
app.mainloop()

