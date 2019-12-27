import numpy as np
import matplotlib.pyplot as plt

t,Cm,Cd,Cl,Clf,Clr = np.loadtxt('postProcessing/forceCoeffs1/0/forceCoeffs.dat',delimiter='\t',dtype=np.float,skiprows=9,unpack=True)

plt.subplot(2,1,1)
plt.plot(t,Cd,'r')
plt.xlabel('Iteration')
plt.ylabel('Cd')

plt.subplot(2,1,2)
plt.plot(t,Cl,'r')
plt.xlabel('Iteration')
plt.ylabel('Cl')

plt.show()
