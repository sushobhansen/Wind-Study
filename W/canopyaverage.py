import numpy as np
import csv
from matplotlib import pyplot as plt

#Get data
dataT = np.loadtxt('postProcessing/surfaces/4000/T_canopy.raw',dtype='float',delimiter=' ',skiprows=2,usecols=[0,1,3]) #x,y,T
dataU = np.loadtxt('postProcessing/surfaces/4000/U_canopy.raw',dtype='float',delimiter=' ',skiprows=2,usecols=[0,1,3,4,5]) #x,y,Ux,Uy,Uz

#Define limits
H = 5.0
W = 5.0
xlims = np.array([15*H+i*W for i in range(6)])
ylims = np.array([15*H+i*W for i in range(6)])

#Evaluate average canopy temperature in each of the twelve canyons
canopyT = np.zeros(12) #12 canyons to store mean temperature
canopyU = np.zeros(12) #12 canyons to store mean wind speed


#Canopy 1
x = 1 #left x-limit
y = 4 #lower y-limit
xcondition = np.logical_and(dataT[:,0]>xlims[x],dataT[:,0]<xlims[x+1])
ycondition = np.logical_and(dataT[:,1]>ylims[y],dataT[:,1]<ylims[y+1])
canopyT[0] = np.mean(dataT[np.logical_and(xcondition,ycondition),2])

xcondition = np.logical_and(dataU[:,0]>xlims[x],dataU[:,0]<xlims[x+1])
ycondition = np.logical_and(dataU[:,1]>ylims[y],dataU[:,1]<ylims[y+1])
canopyU[0] = np.mean(np.sqrt(np.sum(np.square(dataU[np.logical_and(xcondition,ycondition),2:4]),axis=1)))

#Canopy 2
x = 3 #left x-limit
y = 4 #lower y-limit
xcondition = np.logical_and(dataT[:,0]>xlims[x],dataT[:,0]<xlims[x+1])
ycondition = np.logical_and(dataT[:,1]>ylims[y],dataT[:,1]<ylims[y+1])
canopyT[1] = np.mean(dataT[np.logical_and(xcondition,ycondition),2])

xcondition = np.logical_and(dataU[:,0]>xlims[x],dataU[:,0]<xlims[x+1])
ycondition = np.logical_and(dataU[:,1]>ylims[y],dataU[:,1]<ylims[y+1])
canopyU[1] = np.mean(np.sqrt(np.sum(np.square(dataU[np.logical_and(xcondition,ycondition),2:4]),axis=1)))

#Canopy 3
x = 0 #left x-limit
y = 3 #lower y-limit
xcondition = np.logical_and(dataT[:,0]>xlims[x],dataT[:,0]<xlims[x+1])
ycondition = np.logical_and(dataT[:,1]>ylims[y],dataT[:,1]<ylims[y+1])
canopyT[2] = np.mean(dataT[np.logical_and(xcondition,ycondition),2])

xcondition = np.logical_and(dataU[:,0]>xlims[x],dataU[:,0]<xlims[x+1])
ycondition = np.logical_and(dataU[:,1]>ylims[y],dataU[:,1]<ylims[y+1])
canopyU[2] = np.mean(np.sqrt(np.sum(np.square(dataU[np.logical_and(xcondition,ycondition),2:4]),axis=1)))

#Canopy 4
x = 2 #left x-limit
y = 3 #lower y-limit
xcondition = np.logical_and(dataT[:,0]>xlims[x],dataT[:,0]<xlims[x+1])
ycondition = np.logical_and(dataT[:,1]>ylims[y],dataT[:,1]<ylims[y+1])
canopyT[3] = np.mean(dataT[np.logical_and(xcondition,ycondition),2])

xcondition = np.logical_and(dataU[:,0]>xlims[x],dataU[:,0]<xlims[x+1])
ycondition = np.logical_and(dataU[:,1]>ylims[y],dataU[:,1]<ylims[y+1])
canopyU[3] = np.mean(np.sqrt(np.sum(np.square(dataU[np.logical_and(xcondition,ycondition),2:4]),axis=1)))

#Canopy 5
x = 4 #left x-limit
y = 3 #lower y-limit
xcondition = np.logical_and(dataT[:,0]>xlims[x],dataT[:,0]<xlims[x+1])
ycondition = np.logical_and(dataT[:,1]>ylims[y],dataT[:,1]<ylims[y+1])
canopyT[4] = np.mean(dataT[np.logical_and(xcondition,ycondition),2])

xcondition = np.logical_and(dataU[:,0]>xlims[x],dataU[:,0]<xlims[x+1])
ycondition = np.logical_and(dataU[:,1]>ylims[y],dataU[:,1]<ylims[y+1])
canopyU[4] = np.mean(np.sqrt(np.sum(np.square(dataU[np.logical_and(xcondition,ycondition),2:4]),axis=1)))

#Canopy 6
x = 1 #left x-limit
y = 2 #lower y-limit
xcondition = np.logical_and(dataT[:,0]>xlims[x],dataT[:,0]<xlims[x+1])
ycondition = np.logical_and(dataT[:,1]>ylims[y],dataT[:,1]<ylims[y+1])
canopyT[5] = np.mean(dataT[np.logical_and(xcondition,ycondition),2])

xcondition = np.logical_and(dataU[:,0]>xlims[x],dataU[:,0]<xlims[x+1])
ycondition = np.logical_and(dataU[:,1]>ylims[y],dataU[:,1]<ylims[y+1])
canopyU[5] = np.mean(np.sqrt(np.sum(np.square(dataU[np.logical_and(xcondition,ycondition),2:4]),axis=1)))

#Canopy 7
x = 3 #left x-limit
y = 2 #lower y-limit
xcondition = np.logical_and(dataT[:,0]>xlims[x],dataT[:,0]<xlims[x+1])
ycondition = np.logical_and(dataT[:,1]>ylims[y],dataT[:,1]<ylims[y+1])
canopyT[6] = np.mean(dataT[np.logical_and(xcondition,ycondition),2])

xcondition = np.logical_and(dataU[:,0]>xlims[x],dataU[:,0]<xlims[x+1])
ycondition = np.logical_and(dataU[:,1]>ylims[y],dataU[:,1]<ylims[y+1])
canopyU[6] = np.mean(np.sqrt(np.sum(np.square(dataU[np.logical_and(xcondition,ycondition),2:4]),axis=1)))

#Canopy 8
x = 0 #left x-limit
y = 1 #lower y-limit
xcondition = np.logical_and(dataT[:,0]>xlims[x],dataT[:,0]<xlims[x+1])
ycondition = np.logical_and(dataT[:,1]>ylims[y],dataT[:,1]<ylims[y+1])
canopyT[7] = np.mean(dataT[np.logical_and(xcondition,ycondition),2])

xcondition = np.logical_and(dataU[:,0]>xlims[x],dataU[:,0]<xlims[x+1])
ycondition = np.logical_and(dataU[:,1]>ylims[y],dataU[:,1]<ylims[y+1])
canopyU[7] = np.mean(np.sqrt(np.sum(np.square(dataU[np.logical_and(xcondition,ycondition),2:4]),axis=1)))

#Canopy 9
x = 2 #left x-limit
y = 1 #lower y-limit
xcondition = np.logical_and(dataT[:,0]>xlims[x],dataT[:,0]<xlims[x+1])
ycondition = np.logical_and(dataT[:,1]>ylims[y],dataT[:,1]<ylims[y+1])
canopyT[8] = np.mean(dataT[np.logical_and(xcondition,ycondition),2])

xcondition = np.logical_and(dataU[:,0]>xlims[x],dataU[:,0]<xlims[x+1])
ycondition = np.logical_and(dataU[:,1]>ylims[y],dataU[:,1]<ylims[y+1])
canopyU[8] = np.mean(np.sqrt(np.sum(np.square(dataU[np.logical_and(xcondition,ycondition),2:4]),axis=1)))

#Canopy 10
x = 4 #left x-limit
y = 1 #lower y-limit
xcondition = np.logical_and(dataT[:,0]>xlims[x],dataT[:,0]<xlims[x+1])
ycondition = np.logical_and(dataT[:,1]>ylims[y],dataT[:,1]<ylims[y+1])
canopyT[9] = np.mean(dataT[np.logical_and(xcondition,ycondition),2])

xcondition = np.logical_and(dataU[:,0]>xlims[x],dataU[:,0]<xlims[x+1])
ycondition = np.logical_and(dataU[:,1]>ylims[y],dataU[:,1]<ylims[y+1])
canopyU[9] = np.mean(np.sqrt(np.sum(np.square(dataU[np.logical_and(xcondition,ycondition),2:4]),axis=1)))

#Canopy 11
x = 1 #left x-limit
y = 0 #lower y-limit
xcondition = np.logical_and(dataT[:,0]>xlims[x],dataT[:,0]<xlims[x+1])
ycondition = np.logical_and(dataT[:,1]>ylims[y],dataT[:,1]<ylims[y+1])
canopyT[10] = np.mean(dataT[np.logical_and(xcondition,ycondition),2])

xcondition = np.logical_and(dataU[:,0]>xlims[x],dataU[:,0]<xlims[x+1])
ycondition = np.logical_and(dataU[:,1]>ylims[y],dataU[:,1]<ylims[y+1])
canopyU[10] = np.mean(np.sqrt(np.sum(np.square(dataU[np.logical_and(xcondition,ycondition),2:4]),axis=1)))

#Canopy 12
x = 3 #left x-limit
y = 0 #lower y-limit
xcondition = np.logical_and(dataT[:,0]>xlims[x],dataT[:,0]<xlims[x+1])
ycondition = np.logical_and(dataT[:,1]>ylims[y],dataT[:,1]<ylims[y+1])
canopyT[11] = np.mean(dataT[np.logical_and(xcondition,ycondition),2])

xcondition = np.logical_and(dataU[:,0]>xlims[x],dataU[:,0]<xlims[x+1])
ycondition = np.logical_and(dataU[:,1]>ylims[y],dataU[:,1]<ylims[y+1])
canopyU[11] = np.mean(np.sqrt(np.sum(np.square(dataU[np.logical_and(xcondition,ycondition),2:4]),axis=1)))

#Plot
plt.subplot(1,2,1)
farfield = 304.15
plt.grid(color='gray', linestyle='dashed',zorder=0)
plt.bar(range(1,13,1),canopyT-farfield,color='#4A4A4A',align='center',zorder=3)
plt.xticks(range(1,13,1))
plt.xlabel('Canopy Number')
plt.ylabel('Heat Island Intensity ($^\circ$C)')

plt.subplot(1,2,2)
plt.grid(color='gray', linestyle='dashed',zorder=0)
plt.bar(range(1,13,1),canopyU,color='#4A4A4A',align='center',zorder=3)
plt.xticks(range(1,13,1))
plt.xlabel('Canopy Number')
plt.ylabel('Average wind speed (m/s)')

plt.show()

#Write data
f = open("./0/includes/Tair.txt","w")
f.write(str(np.mean(canopyT)))
f.close()

f = open("./0/includes/U.txt","w")
f.write(str(np.mean(canopyU)))
f.close()
