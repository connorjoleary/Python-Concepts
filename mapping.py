# Connor O'Leary
# Joe Pagi
import numpy as np


file = open('city1.txt', 'r')
file.readline()
file.readline()
file.readline()
file.readline() #reads in line titles
file.readline()
i=1
file.readline()
data = file.readline().split('\t')

for line in file:
    if(len(line.split('\t'))==1):
        i=i+1
        j=0
    else:
        data[i].append(line.split('\t'))
        j=j+1
        print data[i][j]
file.close()
