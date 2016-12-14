import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
import tkinter.messagebox

from PIL import Image, ImageTk
import numpy as np
import pygame
import sys
import os, shutil
from pygame.locals import *


LARGE_FONT = ("Verdana", 12)
fileLabel = []
filelist = []
filebase = []
radio = []
value = 0
x = 0
song = 0
vol = 0


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

    def __init__(self,parent,root):
        pygame.init()
        global value
        global song
        global fileLabel
        global filelist
        global filebase
        global x

        def Play():
            print("play")

            pygame.mixer.music.play()
            pg.start()
            pg.configure( mode='determinate', value = pygame.mixer.music.get_pos())

        def Resume():
            print("Resume")
            pygame.mixer.music.unpause()
            pg.start()

        def Pause():
            print("Pause")
            pygame.mixer.music.pause()
            pg.stop()

        def Horror():
            print("Prepare for the horror")
            # pygame.mixer.music.load("Requiem For A Dream Original Song.wav")

        def Happy():
            print("Prepare to for an uplifting happy tune.")
            # pygame.mixer.music.load("Curtis Mayfield - Move On Up.wav")

        def Blues():
            print("Prepare for some blues.")
            # pygame.mixer.music.load("Santana - Blues Latino.wav")

        def Sad():
            print("Prepare for some emo tunes.")
            # pygame.mixer.music.load("Stan [Live].wav")

        def Choice(event):
            song = int(entry.get())
            print(song)
            print(filelist)
            pygame.mixer.music.load(filelist[song])
        def MakeRadio(filebase,filelist,fileLabel):
            global song
            global radio
            global x

            x = 0
            for i in filebase:
                pg.stop()
                pygame.mixer.music.pause()
                fileLabel.append(Label(self,text=i, font=LARGE_FONT))
                radio.append(Radiobutton(self,value=filelist,variable=song))

            #     r = Radiobutton(self,text=filebase,variable=song,value=filelist)
            #     r.bind("<Button-1>",Choice)
            # for t in r:
            #     t.place(x = 180, y = 250+(x*30))
            #     x = x + 1

            for t in radio:
                t.place(x = 180, y = 250+(x*30))
                x = x + 1
            x = 0
            for j in fileLabel:
                j.place(x = 210, y = 250+(x*30))
                x = x + 1
        def Browse():
            global fileLabel
            global filelist
            global filebase

            # del filelist[:]
            del filebase[:]
            filename = filedialog.askopenfilename()
            filelist.append(filename)
            base = os.path.basename(filename)
            filebase.append(base)
            MakeRadio(filebase,filelist,fileLabel)


        def Mute():
            print("mute")
            pygame.mixer.music.set_volume(0)

        def Unmute():
           print("mute")
           pygame.mixer.music.set_volume(100)

        tk.Frame.__init__(self,parent)
        labelStartStop = tk.Label(self, text = "Press start to play audio.    Press pause to stop audio.", font = LARGE_FONT)
        labelStartStop.place(x = 20, y = 20)

        labelList = tk.Label(self, text = "Music Play List: ", font = LARGE_FONT)
        labelList.place(x = 40, y = 220)

        play = tk.Button(self,text = "Play", command = Play)
        play.place(x = 40, y = 60)

        pause = tk.Button(self,text = "Pause", command = Pause)
        pause.place(x = 200, y = 60)

        resume = tk.Button(self,text = "Resume", command = Resume)
        resume.place(x = 110, y = 60)

        mute =  tk.Button(self, text = "Mute", command = Mute)
        mute.place(x = 270, y = 60)

        unmute = tk.Button(self, text = "Unmute", command = Unmute)
        unmute.place(x = 340, y = 60)

        pg = ttk.Progressbar(self, orient='horizontal',length=300, mode='determinate')
        pg.place(x = 40, y = 110)

        FileBrowse = tk.Button(self,text = "Browse for Music",command = Browse)
        FileBrowse.place(x = 40, y = 250)

        labelChoose = tk.Label(self,text = "Choose a theme: ", font = LARGE_FONT)
        labelChoose.place(x = 40, y = 150)

        horror = tk.Button(self,text = "Horror", command = Horror)
        horror.place(x = 40, y = 190)

        happy = tk.Button(self,text = "Happy", command = Happy)
        happy.place(x = 160, y = 190)

        blues = tk.Button(self,text = "Blues", command = Blues)
        blues.place(x = 280, y = 190)

        sad = tk.Button(self,text = "Sad", command = Sad)
        sad.place(x = 400, y = 190)

        labelChooses = tk.Label(self,text = "Pick a song: ", font = LARGE_FONT)
        labelChooses.place(x = 30, y = 300)

        ok = tk.Button(self,text = "submit")
        ok.bind("<Button-1>",Choice)
        ok.place(x = 30, y = 320)

        entry = Entry(self, width = 1)
        entry.place(x = 100, y = 320)







app = MP3Player()
app.geometry("600x400")
app.mainloop()
