from tkinter import *
import tkinter as tk
from tkinter import filedialog
import utils as util
import Resampling as R

root = Tk()
root.title("Resampling")
root.geometry("500x500")

def Resampling_Gui():

   sf = int(SamplingFreq.get(1.0,"end"))
   stop = int(StopAttenuation.get(1.0,"end"))
   CutOff = int(CutOffFreq.get(1.0,"end"))
   TransitionWidth = int(TransitionBand.get(1.0,"end"))
   MFactor = int(DownSampleFactor.get(1.0,"end"))
   LFactor = int(upSampleFactor.get(1.0,"end"))
   R.Resampling(sf,stop,CutOff,TransitionWidth,MFactor,LFactor)
   

SamplingLabel = LabelFrame(root,text = "Sampling Frequency")
SamplingFreq = Text(SamplingLabel, width=50, height=2)

StopLabel = LabelFrame(root,text = "Stop Attenuation")
StopAttenuation = Text(StopLabel, width=50, height=2)

CutOffLabel = LabelFrame(root,text = "CutOff Frequency")
CutOffFreq = Text(CutOffLabel, width=50, height=2)

TransLabel = LabelFrame(root,text = "Transition Band")
TransitionBand = Text(TransLabel, width=50, height=2)

MLabel = LabelFrame(root,text = "DownSampleFactor")
DownSampleFactor = Text(MLabel, width=50, height=2)

LLabel = LabelFrame(root,text = "upSampleFactor")
upSampleFactor = Text(LLabel, width=50, height=2)

ButtonSignal = Button(root,text="Resample Signal",command = Resampling_Gui)

SamplingLabel.pack()
CutOffLabel.pack()
StopLabel.pack()
TransLabel.pack()
MLabel.pack()
LLabel.pack()

SamplingFreq.pack()
CutOffFreq.pack()
StopAttenuation.pack()
TransitionBand.pack()
DownSampleFactor.pack()
upSampleFactor.pack()
ButtonSignal.pack()

root.mainloop()    