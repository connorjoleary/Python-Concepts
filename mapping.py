# Connor O'Leary
# Joe Pagani
import re

final_map = {}
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
		#print(clean.group(1))
		if clean.group(1) not in final_map:
			final_map[clean.group(1)] = {clean.group(2) : clean.group(3)}
		else:
			final_map[clean.group(1)].update({clean.group(2) : clean.group(3)})
file.close()

def task_1(city):
	i = 0
	for node in final_map[city]:
		if node != city: 
			i += 1;
	print(i)
#this works
task_1("Bozeman  ")

def task_2(city1, city2):
	if city2 in final_map[city1]:
		print("Yes")
	else:
		print("No")
#this works
task_2("Bozeman  ", "Billings  ")

#Task 4 is below function
def find_path(start, end, path=[]):
	path = path + [start]
	if start == end:
		return path
	if start not in final_map:
		return None
	for node in final_map[start]:
		if node not in path:
			newpath = find_path(node, end, path)
			if newpath:
				print(newpath)
				return newpath
	return None

print(find_path("Bozeman  ", "Billings  "))
