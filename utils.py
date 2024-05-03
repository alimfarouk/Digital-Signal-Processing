import numpy as np
import cmath as math
import matplotlib as plt
def DCT(signal):
    result = []
    N = len(signal)
    for k in range(0, N):
        summation = 0
        for n in range(0, N):
            summation += signal[n] * math.cos((math.pi / (4 * N) * (2 * n - 1) * (2 * k - 1)))
        result.append(math.sqrt(2 / N) * summation)
    return result

def remove_dc_component(signal):
    dc_component = np.mean(signal)
    signal_without_dc = signal - dc_component
    return signal_without_dc

def normalization(Signal):

    # a = int(txt1.get(1.0, "end"))
    # b = int(txt2.get(1.0, "end"))
    a = -1
    b = 1

    yMin = np.min(Signal)
    yMax = np.max(Signal)

    yNormalized = []

    for j in Signal:
        yNormalized.append(a + (Signal[j] - yMin) * (b - a) / (yMax - yMin))
    return yNormalized
def auto_corr(Signal):
    yOfk = []
    yOfn = []
    N = len(Signal)

    xOfk = DFT(Signal)

    for i in range(0, N):
        yOfk.append(xOfk[i] * np.conj(xOfk[i]))

    tmp = IDFT(yOfk)
    
    yOfn.clear()
    for i in tmp:
        yOfn.append(i / N)
    return yOfn
def correlation(ysignal1, ysignal2):
    r = []
    correlationsignal = []

    N = len(ysignal1)
    r.clear()

    for j in range(0, N):
        value = 0
        for n in range(0, N):
            d = n + j
            if (d >= N):
                d -= N
            value += (ysignal1[n] * ysignal2[d])
        r.append(value / N)

    denominator = 0
    y1square = 0
    y2square = 0

    for i in range(0, N):
        y1square += np.power(ysignal1[i], 2)
        y2square += np.power(ysignal2[i], 2)

    denominator = (np.sqrt(y1square * y2square)) / N

    correlationsignal.clear()
    for i in r:
        correlationsignal.append(i / denominator)

    return correlationsignal

def Template_matching(signal,classOneAvg,classTwoAvg):
    classOneCorr = correlation(signal,classOneAvg)
    classTwoCorr = correlation(signal,classTwoAvg)
    if(max(classOneCorr)>max(classTwoCorr)):
        return "Class A"
    elif(max(classOneCorr)<max(classTwoCorr)):
        return "Class B"
    
    
def ClassA(Signal):
    classTwoAvg = []
    B1 = np.loadtxt("Task2 Cases\B\BSeg1.txt")
    B2 = np.loadtxt("Task2 Cases\B\BSeg2.txt")
    B3 = np.loadtxt("Task2 Cases\B\BSeg3.txt")
    B4 = np.loadtxt("Task2 Cases\B\BSeg4.txt")
    B5 = np.loadtxt("Task2 Cases\B\BSeg5.txt")
    B6 = np.loadtxt("Task2 Cases\B\BSeg6.txt")
    for i in range (len(Signal)):
        classTwoAvg.append(((B1 + B2 + B3 + B4 + B5 + B6) / 6))
    return classTwoAvg

def ClassB(Signal):
    classOneAvg = []
    A1 = np.loadtxt("Task2 Cases\A\ASeg1.txt")
    A2 = np.loadtxt("Task2 Cases\A\ASeg2.txt")
    A3 = np.loadtxt("Task2 Cases\A\ASeg3.txt")
    A4 = np.loadtxt("Task2 Cases\A\ASeg4.txt")
    A5 = np.loadtxt("Task2 Cases\A\ASeg5.txt")
    A6 = np.loadtxt("Task2 Cases\A\ASeg6.txt")
    for i in range (len(Signal)):
        classOneAvg.append(((A1 + A2 + A3 + A4 + A5 + A6) / 6))
    return classOneAvg
    
def mult(Signal1,Signal2):
    xOfk1 = []
    xOfk2 = []
    yOfk = []
    convsignal = []

    N1 = len(Signal1)
    N2 = len(Signal2)
    for i in range(N1):
        yOfk.append(Signal1[i] * Signal2[i])

    
    return yOfk
def DFT(Signal,freq):
        xOfn = Signal
        xOfk = []
        amplitude = []
        phase = []
        sigma = []
        N = len(Signal)
        
        j = 1j

        for k in range (0, N):
            harmonic_value = 0
            for n in range (0, N):
                harmonic_value += xOfn[n] * np.exp((-j * 2 * np.pi * k * n) / N)
            xOfk.append(harmonic_value)
            amplitude.append(np.sqrt(np.power(np.real(harmonic_value), 2) + np.power(np.imag(harmonic_value), 2)))
            phase.append(np.arctan2(np.imag(harmonic_value), np.real(harmonic_value)))

        fund_freq = 0
        fs = freq

        for i in range(0, len(amplitude)):
            fund_freq += (2 * np.pi * fs) / N
            sigma.append(fund_freq)
        return xOfk
def IDFT(xOfk):
    N = len(xOfk)
    j = 1j
    xOfn =[]
    for n in range (0, N):
        harmonic_value = 0
        for k in range (0, N):
            harmonic_value += (1 / N) * xOfk[k] * np.exp((j * 2 * np.pi * n * k) / N)
        xOfn.append(np.real(harmonic_value))
    return xOfn
def fast_convolution(Signal1,Signal2):
    xOfk1 = []
    xOfk2 = []
    yOfk = []
    convsignal = []
    N1 = len(Signal1)
    N2 = len(Signal2)
    j =1j
    N3 = N1 + N2 - 1

    for i in range(N3 - len(Signal1)):
        Signal1.append(0)
    for i in range(N3 - len(Signal2)):
        Signal2.append(0)
    #DFT
    for k in range(0, N3):
        harmonic_value = 0
        for n in range(0, N3):
            harmonic_value += (Signal1[n] * np.exp((-j * 2 * np.pi * k * n) / N3))
        xOfk1.append(harmonic_value)

    for k in range(0, N3):
        harmonic_value = 0
        for n in range(0, N3):
            harmonic_value += (Signal2[n] * np.exp((-j * 2 * np.pi * k * n) / N3))
        xOfk2.append(harmonic_value)

    #Convolution
    for i in range(N3):
        yOfk.append(xOfk1[i] * xOfk2[i])

    #IDFT
    N = len(yOfk)
    for n in range(0, N3):
        harmonic_value = 0
        for k in range(0, N3):
            harmonic_value += (1 / N3) * (yOfk[k] * np.exp((j * 2 * np.pi * n * k) / N3))
        #print(harmonic_value)
        convsignal.append(np.real(harmonic_value))
    return convsignal