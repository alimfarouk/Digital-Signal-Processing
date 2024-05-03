from tkinter import *
import utils as util
from tkinter import filedialog
import tkinter as tk
import numpy as np
import matplotlib as plt
import CompareSignal as compare
def Filtering(SamplingFreq,StopAttenuation,CutOffFreq,TransitionWidth,F1Freq,F2Freq,filter_type,ysignal):
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
        N = 0.9/deltaF #49.5
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
            value = 0.5+(0.5*np.cos(2*np.pi*i/(N)))
            deltaW.append(value)
       
        
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
                    
    # filter
    
    if(filter_type == 0):
        Fc = 0
        Fc = (CutOffFreq + (TransitionWidth/2))/SamplingFreq
        for i in range (int(0-((N-1)/2)),int(((N-1)/2)+1)):
            indeces.append(i)
            if (i == 0):
                deltaH.append(2 * Fc)
                continue
            deltaH.append(2*Fc *((np.sin(i*2*np.pi*Fc))/(i*2*np.pi*Fc)))
            
            
            
    elif(filter_type == 1):
        Fc = 0
        Fc = (CutOffFreq - (TransitionWidth/2))/SamplingFreq
        for i in range (int(0-((N-1)/2)),int(((N-1)/2)+1)):
            indeces.append(i)
            if(i ==0):
                deltaH.append(1-(2 * Fc))
                continue
            deltaH.append(-2*Fc *(np.sin(i*2*np.pi*Fc)/(i*2*np.pi*Fc)))
        
    elif(filter_type == 2):
        F1c = 0
        F2c = 0
        F1c = (F1Freq - (TransitionWidth/2))/SamplingFreq
        F2c = (F2Freq + (TransitionWidth/2))/SamplingFreq
        for i in range (int(0-((N-1)/2)),int(((N-1)/2)+1)):
            indeces.append(i)
            if(i == 0):
                deltaH.append(2 * (F1c- F2c))
                continue
            deltaH.append((2*F2c*(np.sin(i*2*np.pi*F2c)/(i*2*F2c*np.pi))) - (2*F1c*(np.sin(i*2*np.pi*F1c)/(i*2*F1c*np.pi))))
        
    elif(filter_type == 3):
        F1c = 0
        F2c = 0
        F1c = (F1Freq + (TransitionWidth/2))/SamplingFreq
        F2c = (F2Freq - (TransitionWidth/2))/SamplingFreq
        for i in range (int(0-((N-1)/2)),int(((N-1)/2)+1)):
            indeces.append(i)
            if(i ==0):
                deltaH.append(1 - (2 * (F1c- F2c)))
                continue
            deltaH.append((2*F1c*(np.sin(i*2*np.pi*F1c)/(i*2*F1c*np.pi))) - (2*F2c*(np.sin(i*2*np.pi*F2c)/(i*2*F2c*np.pi))))
            
    filterArr = util.mult(deltaH,deltaW)
    if(len(ysignal) != 0):
            filteredSignal = util.fast_convolution(ysignal,filterArr)
    if(filter_type == 0):
        if(len(ysignal) != 0):
            compare.Compare_Signals("FIR test cases\Testcase 2\ecg_low_pass_filtered.txt",indeces,filteredSignal)
            return filteredSignal
        else : 
            compare.Compare_Signals("FIR test cases\Testcase 1\LPFCoefficients.txt",indeces,filterArr)
            return filterArr
    elif(filter_type == 1):
        if(len(ysignal) != 0):
            compare.Compare_Signals("FIR test cases\Testcase 4\ecg_high_pass_filtered.txt",indeces,filteredSignal)
        else : 
            compare.Compare_Signals("FIR test cases\Testcase 3\HPFCoefficients.txt",indeces,filterArr)
            return filterArr
    elif(filter_type == 2):
        if(len(ysignal) != 0):
            compare.Compare_Signals("FIR test cases\Testcase 6\ecg_band_pass_filtered.txt",indeces,filteredSignal)
            print(filteredSignal)
        else : 
            compare.Compare_Signals("FIR test cases\Testcase 5\BPFCoefficients.txt",indeces,filterArr)
            print(filterArr)
            return filterArr
    elif(filter_type == 3):
        if(len(ysignal) != 0):
            compare.Compare_Signals("FIR test cases\Testcase 8\ecg_band_stop_filtered.txt",indeces,filteredSignal)
            print(filteredSignal)
            
        else : 
            compare.Compare_Signals("FIR test cases\Testcase 7\BSFCoefficients.txt",indeces,filterArr)
            print(filterArr)
            return filterArr
    

        
    



