import numpy as np
import csv
from matplotlib import pyplot as plt

#Get data
data = np.loadtxt('postProcessing/surfaces/3000/T_canopy.raw',dtype='float',delimiter=' ',skiprows=2,usecols=[0,1,3])

#Define limits
H = 0.1
W = 0.1
xlims = np.array([15*H+i*W for i in range(6)])
ylims = np.array([15*H+i*W for i in range(6)])

#Evaluate average canopy temperature in each of the twelve canyons
canopy = np.zeros(12) #12 canyons to store mean temperature

#Canopy 1
x = 1 #left x-limit
y = 4 #lower y-limit
xcondition = np.logical_and(data[:,0]>xlims[x],data[:,0]<xlims[x+1])
ycondition = np.logical_and(data[:,1]>ylims[y],data[:,1]<ylims[y+1])
canopy[0] = np.mean(data[np.logical_and(xcondition,ycondition),2])

#Canopy 2
x = 3 #left x-limit
y = 4 #lower y-limit
xcondition = np.logical_and(data[:,0]>xlims[x],data[:,0]<xlims[x+1])
ycondition = np.logical_and(data[:,1]>ylims[y],data[:,1]<ylims[y+1])
canopy[1] = np.mean(data[np.logical_and(xcondition,ycondition),2])

#Canopy 3
x = 0 #left x-limit
y = 3 #lower y-limit
xcondition = np.logical_and(data[:,0]>xlims[x],data[:,0]<xlims[x+1])
ycondition = np.logical_and(data[:,1]>ylims[y],data[:,1]<ylims[y+1])
canopy[2] = np.mean(data[np.logical_and(xcondition,ycondition),2])

#Canopy 4
x = 2 #left x-limit
y = 3 #lower y-limit
xcondition = np.logical_and(data[:,0]>xlims[x],data[:,0]<xlims[x+1])
ycondition = np.logical_and(data[:,1]>ylims[y],data[:,1]<ylims[y+1])
canopy[3] = np.mean(data[np.logical_and(xcondition,ycondition),2])

#Canopy 5
x = 4 #left x-limit
y = 3 #lower y-limit
xcondition = np.logical_and(data[:,0]>xlims[x],data[:,0]<xlims[x+1])
ycondition = np.logical_and(data[:,1]>ylims[y],data[:,1]<ylims[y+1])
canopy[4] = np.mean(data[np.logical_and(xcondition,ycondition),2])

#Canopy 6
x = 1 #left x-limit
y = 2 #lower y-limit
xcondition = np.logical_and(data[:,0]>xlims[x],data[:,0]<xlims[x+1])
ycondition = np.logical_and(data[:,1]>ylims[y],data[:,1]<ylims[y+1])
canopy[5] = np.mean(data[np.logical_and(xcondition,ycondition),2])

#Canopy 7
x = 3 #left x-limit
y = 2 #lower y-limit
xcondition = np.logical_and(data[:,0]>xlims[x],data[:,0]<xlims[x+1])
ycondition = np.logical_and(data[:,1]>ylims[y],data[:,1]<ylims[y+1])
canopy[6] = np.mean(data[np.logical_and(xcondition,ycondition),2])

#Canopy 8
x = 0 #left x-limit
y = 1 #lower y-limit
xcondition = np.logical_and(data[:,0]>xlims[x],data[:,0]<xlims[x+1])
ycondition = np.logical_and(data[:,1]>ylims[y],data[:,1]<ylims[y+1])
canopy[7] = np.mean(data[np.logical_and(xcondition,ycondition),2])

#Canopy 9
x = 2 #left x-limit
y = 1 #lower y-limit
xcondition = np.logical_and(data[:,0]>xlims[x],data[:,0]<xlims[x+1])
ycondition = np.logical_and(data[:,1]>ylims[y],data[:,1]<ylims[y+1])
canopy[8] = np.mean(data[np.logical_and(xcondition,ycondition),2])

#Canopy 10
x = 4 #left x-limit
y = 1 #lower y-limit
xcondition = np.logical_and(data[:,0]>xlims[x],data[:,0]<xlims[x+1])
ycondition = np.logical_and(data[:,1]>ylims[y],data[:,1]<ylims[y+1])
canopy[9] = np.mean(data[np.logical_and(xcondition,ycondition),2])

#Canopy 11
x = 1 #left x-limit
y = 0 #lower y-limit
xcondition = np.logical_and(data[:,0]>xlims[x],data[:,0]<xlims[x+1])
ycondition = np.logical_and(data[:,1]>ylims[y],data[:,1]<ylims[y+1])
canopy[10] = np.mean(data[np.logical_and(xcondition,ycondition),2])

#Canopy 12
x = 3 #left x-limit
y = 0 #lower y-limit
xcondition = np.logical_and(data[:,0]>xlims[x],data[:,0]<xlims[x+1])
ycondition = np.logical_and(data[:,1]>ylims[y],data[:,1]<ylims[y+1])
canopy[11] = np.mean(data[np.logical_and(xcondition,ycondition),2])

#Plot
farfield = 300
plt.grid(color='gray', linestyle='dashed',zorder=0)
plt.bar(range(1,13,1),canopy-farfield,color='#4A4A4A',align='center',zorder=3)
plt.xticks(range(1,13,1))
plt.xlabel('Canopy Number')
plt.ylabel('Heat Island Intensity ($^\circ$C)')
plt.show()

#Write data
w = csv.writer(open('canopydata.csv','w'))

for key,val in enumerate(canopy):
	w.writerow([key+1,val])
