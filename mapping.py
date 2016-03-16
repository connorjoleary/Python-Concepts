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
data = [re.split('[ ]{2,}', item) for item in file if item.find("---")]
print data[18]

#for line in data:
    #if '-------'

for line in data:
    data.append([line[1],line[0],line[2]])
