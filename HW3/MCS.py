import numpy as np
import matplotlib.pyplot as plt
import math

def trendarray():
    DCGRAlpha = 0.00100
    DCGRSD = 0.04500
    Initial = 10.0
    TrendArray = []
    TrendArray.append(Initial)
    for i in len(range(100)):
        nextvalue = TrendArray[i-1]*math.exp(DCGRAlpha+DCGRSD)
        TrendArray.append(nextvalue)
    return TrendArray

def simulator():
    DCGRAlpha = 0.00100
    DCGRSD = 0.04500
    Initial = 10.0
    MCS = []
    epsilon = np.random.normal()
    MCS.append(Initial)
    for i in range(1,len(100)):
        nextvalue = MCS[i-1]*math.exp(DCGRAlpha+DCGRSD*epsilon)
        MCS.append(nextvalue)

def main():
    TrendArray = trendarray()
    MCS = simulator()
    MCS1 = simulator()
    MCS2 = simulator()
    plt.plot(TrendArray)
    plt.plot(MCS)
    plt.plot(MCS1)
    plt.plot(MCS2)
    plt.show()
    