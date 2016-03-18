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
		if clean.group(2).rstrip() not in final_map:
			final_map[clean.group(2).rstrip()] = {clean.group(1).rstrip() : clean.group(3).rstrip()}
		if clean.group(1).rstrip() not in final_map:
			final_map[clean.group(1).rstrip()] = {clean.group(2).rstrip() : clean.group(3).rstrip()}
		else:
			final_map[clean.group(1).rstrip()].update({clean.group(2).rstrip() : clean.group(3).rstrip()})
			final_map[clean.group(2).rstrip()].update({clean.group(1).rstrip() : clean.group(3).rstrip()})
file.close()
#print(final_map["  "])
def task_1(city):
	i = 0
	for node in final_map[city]: 
		i += 1;
	print(i)
#this works
print 'task 1'
city = raw_input('Enter the city: ')
task_1(city)

def task_2(city1, city2):
	if city2 in final_map[city1]:
		print("Yes")
	else:
		print("No")
#this works

print 'task 2'
city1 = raw_input('Enter the city: ')
city2 = raw_input('Enter the city: ')
task_2(city1, city2)
#Task 3 is below function
def find_connections(start, end, d, path=[]):
	path = path + [start]
	if start == end:
		return path
	if start not in final_map:
		return None
	for node in final_map[start]:
		if node not in path:
			newpath = find_path(node, end, path)
			if newpath:
				return newpath
	return None

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
				return newpath
	return None
d = 0
path = find_path('Bozeman  ', 'Billings  ')
for index in range(len(path)):
	if index >= 1:
		d += int(final_map[path[index-1]][path[index]])
print(path)
print(d)
