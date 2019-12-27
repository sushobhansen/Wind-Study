import numpy as np
import matplotlib.pyplot as plt

z,T,Ux,Uy,Uz = np.loadtxt('postProcessing/singleGraph/4000/line_T_Ux_Uy_Uz.xy',delimiter='\t',dtype=np.float,unpack=True)
zdata,Uueh,Tueh,Ukim,Tkim,Uxie,Txie = np.loadtxt('xie-2006-data.csv',delimiter=',',dtype=np.float,skiprows=1,unpack=True)

Tf = 309.68
Ta = 308.15
Uinf = 2.0
H = 5.0
theta = (T-Tf)/(Ta-Tf)
z0 = z/H
U0 = Ux/Uinf

plt.subplot(1,2,1)
plt.plot(theta,z0,'r',label='This study, Rb = -0.21')
plt.plot(Tueh,zdata,'bo',label='Uehara et al 2000, Rb = -0.21')
plt.plot(Tkim,zdata,'k^',label='Kim & Baik 2001, Rb = -0.27')
plt.plot(Txie,zdata,'gD',label='Xie et al 2006, Rb = -0.21')
plt.xlabel(r'$\theta$')
plt.ylabel('z/H')
plt.xlim((-0.1,1.2))
plt.ylim((0.0,2.0))
plt.legend(loc=2)

plt.subplot(1,2,2)
plt.plot(U0,z0,'r')
plt.plot(Uueh,zdata,'bo')
plt.plot(Ukim,zdata,'k^')
plt.plot(Uxie,zdata,'gD')
plt.xlabel('Ux/U0')
plt.ylabel('z/H')
plt.ylim((0.0,2.0))

plt.show()
