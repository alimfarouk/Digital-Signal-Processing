import matplotlib as plt
import numpy as np
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import Resampling as Res
import utils as util
def Task2(SamplingFreq,MinFreq,MaxFreq,newFreq,Signal):
    Atten = 50
    TransitionWidth = 500
    M = newFreq/SamplingFreq
    L = SamplingFreq/newFreq
    classA = []
    classB = []
    OriginalSignal = []
    OriginalSignal = Signal
    
    #Get Each ECG Segment
    classA = util.ClassA
    classB = util.ClassB
    
    #Signal Filtering
    Signal = BPF(SamplingFreq,Atten,TransitionWidth,MinFreq,MaxFreq,Signal)
    classA = BPF(SamplingFreq,Atten,TransitionWidth,MinFreq,MaxFreq,classA)
    classB = BPF(SamplingFreq,Atten,TransitionWidth,MinFreq,MaxFreq,classB)
    Fmax1 = max(classA)
    Fmax2 = max(classB)
    if(Fmax1>Fmax2):
        Fmax = Fmax1
    else:
        Fmax = Fmax2
    #Resampling
    if(newFreq < 2*Fmax):
        raise ValueError("Invalid new Frequency, It's gonna destroy the signal")
    else:
        Signal = Res.Resampling(SamplingFreq,Atten,newFreq,TransitionWidth,M,L)
        classA = Res.Resampling(SamplingFreq,Atten,newFreq,TransitionWidth,M,L)
        classB= Res.Resampling(SamplingFreq,Atten,newFreq,TransitionWidth,M,L)
       
    #Remove DC
    Signal = util.remove_dc_component(Signal)
    classA = util.remove_dc_component(classA)
    classB = util.remove_dc_component(classB)
    #Normalization
    Signal = util.normalization(Signal)
    classA = util.normalization(classA)
    classB = util.normalization(classB) 
    
    #Auto Correlation for each ECG Segment
    Signal = util.auto_corr(Signal)
    classA = util.auto_corr(classA)
    classB = util.auto_corr(classB)
    SignalAfterAutoCorr = Signal
    
    #Preserve !!!
    PreserveArr = []
    PreserveA = []
    PreserveB = []
    for i in range (0,99):
        PreserveArr.append(Signal[i])
    for i in range (0,99):
        PreserveA.append(classA[i])
    for i in range (0,99):
        PreserveB.append(classB[i])
    
    
    #Compute DCT 
    ArrAfterDct = util.DCT(PreserveArr)
    AAfterDct = util.DCT(PreserveA)
    BAfterDCT = util.DCT(PreserveB)
    
    
    #Template Matching
    RightClass = ""
    RightClass = util.Template_matching(ArrAfterDct,AAfterDct,BAfterDCT)
    
    plt.show()
    plt.plot(OriginalSignal,Label = "Original Signal")
    plt.plot(SignalAfterAutoCorr,Label = "After Auto Correlation")
    plt.plot(PreserveArr,Label = "Signal After Preserving")
    plt.plot(ArrAfterDct,Label = "Signal After DCT") 
    plt.grid(True)
    
    

def BPF(SamplingFreq,StopAttenuation,TransitionWidth,MinFreq,MaxFreq,Signal):
    xFilterSignal = []
    yFilterSignal = []
    windowType = ""
    filterArr = []
    filteredSignal = []
    deltaF = 0
    indeces = []
    N = 0
    deltaH = []
    deltaW = []
    
    if(StopAttenuation <= 21):
        windowType = "Rectangular"
        deltaF = TransitionWidth/SamplingFreq
        N = 0.9/deltaF
        N = np.ceil(N)
        if(N%2 == 0):
            N += 1
        for i in range (int(0-((N-1)/2)),int(((N-1)/2)+1)):
            deltaW.append(1)
            
        
    
    elif(StopAttenuation <= 44):
        windowType = "Hanning"
        deltaF = TransitionWidth/SamplingFreq
        N = 3.1/deltaF
        N = np.ceil(N)
        if(N%2 == 0):
            N += 1
        for i in range (int(0-((N-1)/2)),int(((N-1)/2)+1)):
            deltaW[i] = (0.5+(0.5*np.cos(2*np.pi*i/(N))))
       
        
    elif(StopAttenuation <= 53):
        windowType = "Hamming"
        deltaF = TransitionWidth/SamplingFreq
        N = 3.3/deltaF
        N = np.ceil(N)
        N = int(N)
        if(N%2 ==0):
            N = N + 1

        for i in range(int(0-((N-1)/2)), int(((N-1)/2)+1)):
            deltaW.append(0.54+(0.46*np.cos((2*np.pi*i)/(N))))
        
    elif(StopAttenuation <= 74):
        windowType = "Blackman"
        deltaF = TransitionWidth/SamplingFreq
        N = 5.5/deltaF
        N = np.ceil(N)
        if(N%2 ==0):
            N += 1
        for i in range (int(0-((N-1)/2)),int(((N-1)/2)+1)):
            deltaW.append(0.42+(0.5*np.cos(2*np.pi*i/(N-1)))+(0.08*np.cos(4*np.pi*i/(N-1))))
    
    F1c = 0
    F2c = 0
    F1c = (MinFreq - (TransitionWidth/2))/SamplingFreq
    F2c = (MaxFreq + (TransitionWidth/2))/SamplingFreq
    for i in range (int(0-((N-1)/2)),int(((N-1)/2)+1)):
        indeces.append(i)
        if(i == 0):
            deltaH.append(2 * (F1c- F2c))
            continue
        deltaH.append((2*F2c*(np.sin(i*2*np.pi*F2c)/(i*2*F2c*np.pi))) - (2*F1c*(np.sin(i*2*np.pi*F1c)/(i*2*F1c*np.pi))))
    filterArr = util.mult(deltaH,deltaW)
    filteredSignal = util.fast_convolution(Signal,filterArr)
    return filteredSignal
