import matplotlib as plt
import numpy as np
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import Filtering as FIR
import utils as util
import CompareSignal2 as compare
def Resampling(SamplingFrequency,StopAttenuation,CutOffFrequency,TransitionWidth,M,L):
    global N
    xsignal = []
    ysignal = []
    upSampledX = []
    upSampledY = []
    downSampledX = []
    downSampledY = []
    indeces = []
    upSamplingFactor = 0
    downSamplingFactor = 0
    Filtered_Signal = []
    if(M==0 and L ==0):
        raise ValueError("Can't Have L and M Equal To Zero")
        
    signal1 = filedialog.askopenfilename(
        initialdir="Sampling test cases", title="Which Signal?")

    with open(signal1, 'r') as f:
        for i in range(3):
            next(f)
        for line in f:
            parts = line.strip().split()
            xsignal.append(float(parts[0]))
            ysignal.append(float(parts[1]))
    upSampledY = ysignal
    downSampledY = ysignal
    if(M == 0 and L!= 0):
        upSamplingFactor = L
        upSampledY = []
        temp = []
        for i in range(len(ysignal)):
            temp.append(ysignal[i])
            for i in range(0,int(upSamplingFactor-1)):
                temp.append(0)
        for i in temp[:-2]:
            upSampledY.append(i)
        Filtered_Signal = LPF(SamplingFrequency,StopAttenuation,CutOffFrequency,TransitionWidth,upSampledY)
        for i in range(int(((N - 1) / 2) + 1), int(len(Filtered_Signal) - ((N - 1) / 2))):
            indeces.append(i)
        test(upSamplingFactor,downSamplingFactor,downSampledY)
        print(upSampledY)
        return Filtered_Signal
    elif(M!= 0 and L == 0):
        downSamplingFactor = M
        Filtered_Signal = LPF(SamplingFrequency,StopAttenuation,CutOffFrequency,TransitionWidth,downSampledY)
        downSampledY[:]= Filtered_Signal[::int(downSamplingFactor)]
        for i in range(int(((N - 1) / 2) + 1), int(len(downSampledY) - ((N - 1) / 2))):
            indeces.append(i)
        
        test(upSamplingFactor,downSamplingFactor,downSampledY)
        print(downSampledY)
        return downSampledY
    else:
        upSamplingFactor = L
        downSamplingFactor = M
        downSampledY = []
        temp = []
        for i in range(len(ysignal)):
            temp.append(ysignal[i])
            for i in range(0,int(upSamplingFactor-1)):
                temp.append(0)
        for i in temp[:-2]:
            upSampledY.append(i)
        Filtered_Signal = LPF(SamplingFrequency,StopAttenuation,CutOffFrequency,TransitionWidth,upSampledY)
        downSampledY[:]= Filtered_Signal[::int(downSamplingFactor)]
        for i in range(int(((N - 1) / 2) + 1), int(len(downSampledY) - ((N - 1) / 2))):
            indeces.append(i)
        test(upSamplingFactor,downSamplingFactor,downSampledY)
        print(downSampledY)
        return downSampledY
def LPF(SamplingFrequency,StopAttenuation,CutOffFrequency,TransitionWidth,ysignal):
    global N
    filterArr = []
    filteredSignal = []
    deltaF = 0
    indeces = []
    N = 0
    deltaH = []
    deltaW = []
    
    if(StopAttenuation <= 21):
        deltaF = TransitionWidth/SamplingFrequency
        N = 0.9/deltaF
        N = np.ceil(N)
        if(N%2 == 0):
            N += 1
        for i in range (int(0-((N-1)/2)),int(((N-1)/2)+1)):
            indeces.append(i)
            deltaW.append(1)
            
        
    
    elif(StopAttenuation <= 44):
        deltaF = TransitionWidth/SamplingFrequency
        N = 3.1/deltaF
        N = np.ceil(N)
        if(N%2 == 0):
            N += 1
        for i in range (int(0-((N-1)/2)),int(((N-1)/2)+1)):
            indeces.append(i)
            deltaW[i] = (0.5+(0.5*np.cos(2*np.pi*i/(N))))
       
        
    elif(StopAttenuation <= 53):
        deltaF = TransitionWidth/SamplingFrequency
        N = 3.3/deltaF
        N = np.ceil(N)
        N = int(N)
        if(N%2 ==0):
            N = N + 1

        for i in range(int(0-((N-1)/2)), int(((N-1)/2)+1)):
            indeces.append(i)
            deltaW.append(0.54+(0.46*np.cos((2*np.pi*i)/(N))))
        
    elif(StopAttenuation <= 74):
        deltaF = TransitionWidth/SamplingFrequency
        N = 5.5/deltaF
        N = np.ceil(N)
        if(N%2 ==0):
            N += 1
        for i in range (int(0-((N-1)/2)),int(((N-1)/2)+1)):
            indeces.append(i)
            
            deltaW.append(0.42+(0.5*np.cos(2*np.pi*i/(N-1)))+(0.08*np.cos(4*np.pi*i/(N-1))))
            
    Fc = 0
    Fc = (CutOffFrequency + (TransitionWidth/2))/SamplingFrequency
    for i in range (int(0-((N-1)/2)),int(((N-1)/2)+1)):
        if (i == 0):
            deltaH.append(2 * Fc)
            continue
        deltaH.append(2*Fc *((np.sin(i*2*np.pi*Fc))/(i*2*np.pi*Fc)))
    filterArr = util.mult(deltaH,deltaW)
    filteredSignal = util.fast_convolution(ysignal,filterArr)
    return filteredSignal

def test(upSampleFactor,downSampleFactor,values):
    if(upSampleFactor == 0 and downSampleFactor != 0 ):
        compare.SignalSamplesAreEqual("Sampling test cases\Testcase 1\Sampling_Down.txt",values)
    elif(upSampleFactor != 0 and downSampleFactor == 0):
        compare.SignalSamplesAreEqual("Sampling test cases\Testcase 2\Sampling_Up.txt",values)
    else:
        compare.SignalSamplesAreEqual("Sampling test cases\Testcase 3\Sampling_Up_Down.txt",values)