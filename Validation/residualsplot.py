import numpy as np
import matplotlib.pyplot as plt

iter,p_rgh = np.loadtxt('logs/p_rgh_0',delimiter='\t',dtype=np.float,unpack=True)
iter,Ux = np.loadtxt('logs/Ux_0',delimiter='\t',dtype=np.float,unpack=True)
iter,Uy = np.loadtxt('logs/Uy_0',delimiter='\t',dtype=np.float,unpack=True)
iter,Uz = np.loadtxt('logs/Uz_0',delimiter='\t',dtype=np.float,unpack=True)
iter,T = np.loadtxt('logs/T_0',delimiter='\t',dtype=np.float,unpack=True)
iter,k = np.loadtxt('logs/k_0',delimiter='\t',dtype=np.float,unpack=True)
iter,epsilon = np.loadtxt('logs/epsilon_0',delimiter='\t',dtype=np.float,unpack=True)

plt.semilogy(iter,p_rgh,label='Pressure')
plt.semilogy(iter,Ux,label='X-Velocity')
plt.semilogy(iter,Uy,label='Y-Velocity')
plt.semilogy(iter,Uz,label='Z-Velocity')
plt.semilogy(iter,T,label='Temperature')
plt.semilogy(iter,k,label='TKE')
plt.semilogy(iter,epsilon,label='TKE Dissipation')
plt.xlabel('Iteration')
plt.ylabel('Residual')
plt.legend()
plt.grid(True)
plt.show()
