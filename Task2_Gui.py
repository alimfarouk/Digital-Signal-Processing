import matplotlib as plt
import numpy as np
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import Task2 as t2
root = Tk()
root.title("Task2")
root.geometry("400x400")
    
def Task2_Gui():

   
    Signal1 = []
    SF = int(SamplingFreq.get(1.0,"end"))
    NewF = int(NewFreq.get(1.0,"end"))
    MinF = int(MinFreq.get(1.0,"end"))
    MaxF = int(MaxFreq.get(1.0,"end"))
    
    Signal1 = filedialog.askopenfilename(
    initialdir="Task2 Cases\Test Folder", title="Which Signal?")
      
    t2.Task2(SF,MinF,MaxF,NewF,Signal1)      
            
SamplingLabel = LabelFrame(root,text = "Sampling Frequency")
SamplingFreq = Text(SamplingLabel, width=50, height=2)

NewLabel = LabelFrame(root,text = "New Frequency")
NewFreq = Text(NewLabel, width=50, height=2)

MinLabel = LabelFrame(root,text = "Minimum Frequency")
MinFreq = Text(MinLabel, width=50, height=2)

MaxLabel = LabelFrame(root,text = "Maximum Frequency")
MaxFreq = Text(MaxLabel, width=50, height=2)

button = Button(root,text="Proceed",command=Task2_Gui)

SamplingLabel.pack()
SamplingFreq.pack()

MinLabel.pack()
MinFreq.pack()

MaxLabel.pack()
MaxFreq.pack()

NewLabel.pack()
NewFreq.pack()

button.pack()

root.mainloop()