from tkinter import *
import tkinter as tk
from tkinter import filedialog
import utils as util
import Filtering as t1

root = Tk()
root.title("Filtering")
root.geometry("500x500")

def Filtering_GUI():
   xsignal = []
   ysignal = []
   sf = int(SamplingFreq.get(1.0,"end"))
   filter_type = int(Filter.get(1.0,"end"))
   stop = int(StopAttenuation.get(1.0,"end"))
   CutOff = int(CutOffFreq.get(1.0,"end"))
   TransitionWidth = int(TransitionBand.get(1.0,"end"))
   f1f = int(f1.get(1.0,"end"))
   f2f = int(f2.get(1.0,"end"))
   t1.Filtering(sf,stop,CutOff,TransitionWidth,f1f,f2f,filter_type,ysignal)
def Read_signal():
   xsignal = []
   ysignal = []
   signal = filedialog.askopenfilename(
   initialdir="FIR test cases", title="Which Signal?")
    
   with open(signal, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            xsignal.append(int(parts[0]))
            ysignal.append(int(parts[1]))
   sf = int(SamplingFreq.get(1.0,"end"))
   filter_type = int(Filter.get(1.0,"end"))
   stop = int(StopAttenuation.get(1.0,"end"))
   CutOff = int(CutOffFreq.get(1.0,"end"))
   TransitionWidth = int(TransitionBand.get(1.0,"end"))
   f1f = int(f1.get(1.0,"end"))
   f2f = int(f2.get(1.0,"end"))
   t1.Filtering(sf,stop,CutOff,TransitionWidth,f1f,f2f,filter_type,ysignal)

SamplingLabel = LabelFrame(root,text = "Sampling Frequency")
SamplingFreq = Text(SamplingLabel, width=50, height=2)

Fifi = Label(root,text="LPF = 0, HPF = 1, BPF = 2,BRF = 3")

F1Label = LabelFrame(root,text = "F1 Frequency")
f1 = Text(F1Label, width=50, height=2)

F2Label = LabelFrame(root,text = "F2 Frequency")
f2 = Text(F2Label, width=50, height=2)

FilterLabel = LabelFrame(root,text = "Filter Type")
Filter = Text(FilterLabel, width = 50, height = 2)

StopLabel = LabelFrame(root,text = "Stop Attenuation")
StopAttenuation = Text(StopLabel, width=50, height=2)

CutOffLabel = LabelFrame(root,text = "CutOff Frequency")
CutOffFreq = Text(CutOffLabel, width=50, height=2)

TransLabel = LabelFrame(root,text = "Transition Band")
TransitionBand = Text(TransLabel, width=50, height=2)

Filtering_button = Button(root,text="Coefficient",command=Filtering_GUI)
ButtonSignal = Button(root,text="Filter Signal",command = Read_signal)

Fifi.pack()
SamplingLabel.pack()
CutOffLabel.pack()
StopLabel.pack()
FilterLabel.pack()
TransLabel.pack()
F1Label.pack()
F2Label.pack()
SamplingFreq.pack()
CutOffFreq.pack()
StopAttenuation.pack()
TransitionBand.pack()
Filter.pack()
f1.pack()
f2.pack()
ButtonSignal.pack()
Filtering_button.pack()


        
   
        
    
        
    
 




root.mainloop()    