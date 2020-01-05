import numpy as np
import scipy
import matplotlib.pyplot as plt

#declare variables
tic = 'HMCIQ'
DCGRa = 0.00100
DCGRsd = 0.04500
initial = 10.00

#initialize arrays
index = []
zeroLine = 10*np.ones(101)
trend = [initial]
mc1 = [initial]
mc2 = [initial]
mc3 = [initial]
mc4 = [initial]

#populate arrays
index = np.arange(101)
for x in range(1,101):
    trend.append(trend[x-1]*np.exp(DCGRa))
    mc1.append(mc1[x-1]*np.exp(DCGRa+DCGRsd*np.random.normal(loc=0.0, scale=1.0, size=None)))
    mc2.append(mc2[x-1]*np.exp(DCGRa+DCGRsd*np.random.normal(loc=0.0, scale=1.0, size=None)))
    mc3.append(mc3[x-1]*np.exp(DCGRa+DCGRsd*np.random.normal(loc=0.0, scale=1.0, size=None)))
    mc4.append(mc4[x-1]*np.exp(DCGRa+DCGRsd*np.random.normal(loc=0.0, scale=1.0, size=None)))

#plot
plt.plot(index,zeroLine, 'k--', label='Orignial Share Price')
plt.plot(index,trend, label='Trend')
plt.plot(index,mc1, label = 'Monte Carlo Simulation 1')
plt.plot(index,mc2, label = 'Monte Carlo Simulation 2')
plt.plot(index,mc3, label = 'Monte Carlo Simulation 3')
plt.plot(index,mc4, label = 'Monte Carlo Simulation 4')
plt.title('Monte Carlo Simulation of Share Prices')
plt.ylabel('Share Price')
plt.xlabel('Day')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()


