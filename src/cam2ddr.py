import pandas as pd
import numpy as np

data = np.array(pd.read_excel('C:/Users/missa/Desktop/BIRST/t1-stratoarcade/src/pixycam_file.xlsx'))
ball = data[:,1]
x = data[:,2]
y = data[:,3]
new_file = open('C:/Users/missa/Desktop/BIRST/t1-stratoarcade/src/ddr_file.txt','w')
new_file.write(str(int(ball[0])) + str(int(ball[1])))
lis = np.linspace(0,len(data)-2,int((len(data))/2))
lis = [int(lis) for lis in lis]
last1 = 0
last2 = 0
for i in lis:
    if x[i]>=0 and y[i]>=0:
        ddr1 = 1
    if x[i]<0 and y[i]>=0:
        ddr1 = 2
    if x[i]<0 and y[i]<0:
        ddr1 = 3
    if x[i]>=0 and y[i]<0:
        ddr1 = 4
    if x[i+1]>=0 and y[i+1]>=0:
        ddr2 = 1
    if x[i+1]<0 and y[i+1]>=0:
        ddr2 = 2
    if x[i+1]<0 and y[i+1]<0:
        ddr2 = 3
    if x[i+1]>=0 and y[i+1]<0:
        ddr2 = 4
    if ddr1 != last1 or ddr2 != last2:
        new_file.write(str(ddr1) + str(ddr2))
    last1 = ddr1 
    last2 = ddr2
new_file = open('C:/Users/missa/Desktop/BIRST/t1-stratoarcade/src/ddr_file.txt')
