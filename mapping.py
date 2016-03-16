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
bar = [re.split('[ ]{2,}', item) for item in file]
print bar[18]
