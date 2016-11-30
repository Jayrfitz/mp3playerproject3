import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import pygame
import sys
from pygame.locals import *

import os, shutil

LARGE_FONT = ("Verdana", 12)
filePath = []
filelist = []
radio = []
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
            pygame.mixer.music.play()

        def Pause():
            print("Pause")
            pygame.mixer.music.pause()

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
            #     radio.append(Radiobutton(self,value = i,variable = i))
            # for j in radio:
            #     j.place(x = 180, y = 250+(x*30))
            #     x = x + 1
            for j in filePath:
                j.place(x = 200, y = 250+(x*30))
                x = x + 1
            print (filePath)
            print (filelist)
            print('\n\n')

            labelM = tk.Label(self, text = "Pick a song: ", font = LARGE_FONT)
            labelM.place(x = 40, y = 280)

            SpinBox  = Spinbox( self,from_ = 0, to = len(filePath),textvariable = filePath, wrap = TRUE, state = 'readonly', width = 5 )
            SpinBox.place (x = 120, y = 280)


        tk.Frame.__init__(self,parent)

        labelStartStop = tk.Label(self, text = "Press start to play audio. Press pause to stop audio.", font = LARGE_FONT)
        labelStartStop.place(x = 20, y = 20)

        labelList = tk.Label(self, text = "Music Play List: ", font = LARGE_FONT)
        labelList.place(x = 40, y = 220)

        play = tk.Button(self,text = "Play", command = Play)
        play.place(x = 40, y = 60)

        pause = tk.Button(self,text = "Pause", command = Pause)
        pause.place(x = 160, y = 60)

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

        emo = tk.Button(self,text = "Emo", command = Emo)
        emo.place(x = 400, y = 190)

        label = tk.Label(self,text = "Volume", font = LARGE_FONT)
        label.place(x = 350, y = 20)

        Slider1 = Scale(self, orient = HORIZONTAL, length = 100,width = 10, sliderlength = 10, from_ = 0, to = 100)
        Slider1.place (x = 350, y = 40)



        # background_image = PhotoImage('/Users/jasonfitzgerald/Desktop/cst205/project3/backgroundImage.jpg')
        # background = Label(self, image=background_image, bd=0)
        # background.place(x=0, y=0, relwidth=1, relheight=1)

        # self.image = tk.PhotoImage('/Users/jasonfitzgerald/Desktop/cst205/project3/backgroundImage.jpg')
        # label = tk.Label(self,image=self.image)
        # label.place(x=0, y=0, relwidth=1.0, relheight=1.0, anchor="nw")

        # im = Image.open('/Users/jasonfitzgerald/Desktop/cst205/project3/backgroundImage.jpg')
        # tkimage = ImageTk.PhotoImage(im)
        # myvar = tk.Label(self,image = tkimage)
        # myvar.place(x=0, y=0, relwidth=1, relheight=1)

def Audio():
    pygame.init()  # turn all of pyGame on.
    # According to documentation, you should use OGG or WAV sound files.
    pygame.mixer.init(44100, -16,2,2048)
    # pygame.mixer.pre_init(44100, 16, 2, 2048)
    #  frequency, size, channels, bufferSize
    # pygame.mixer.music.load('C:/tmp/MediaPLayer/BMA.wav')
    pygame.mixer.music.load('/Users/jasonfitzgerald/Desktop/cst205/project3/bma.mp3')
    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
        pygame.mixer.music.set_volume(vol)
app = MP3Player()
app.geometry("800x400")
app.mainloop()

