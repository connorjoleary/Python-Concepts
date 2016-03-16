# Connor O'Leary
# Joe Pagani
import re

global final_map
file = open('city1.txt', 'r')
file.readline()
file.readline()
file.readline()
file.readline() #reads in line titles
file.readline()
file.readline()
for line in file:
	clean = re.match('(\w+\s\w*\s\w*)\s+(\w+\s\w*\s\w*)\s+(\d+)', line)
	if clean:
		print(clean.groups())
file.close()
