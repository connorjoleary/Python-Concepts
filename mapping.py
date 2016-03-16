# Connor O'Leary
# Joe Pagi
import re

file = open('city1.txt', 'r')
file.readline()
file.readline()
file.readline()
file.readline() #reads in line titles
file.readline()
i=1
data = [re.split('[ ]{2,}', item) for item in file]
print data[17]

#for line in data:
    #remove '-------'
    #data.append([line[1],line[0],line[2]])
