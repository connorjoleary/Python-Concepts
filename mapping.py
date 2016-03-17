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
			final_map[clean.group(1)] = list()
		else:
			final_map[clean.group(1)].append(clean.group(2))
file.close()
#for debugging
"""
l = sorted(final_map.keys())
for i in l:
	print(i)
"""
def task_1(graph, city):
	i = 0
	for node in graph[city]:
		i += 1;
	print(i)
#this works
task_1(final_map, "Bozeman  ")

def task_2(graph, city1, city2):
	if city2 in graph[city1]:
		print("Yes")
	else:
		print("No")
#this works
task_2(final_map, "Bozeman  ", "Billings  ")

#Task 4 is below function
def find_path(graph, start, end, path = []):
	if start == end:
		return path
	if not graph.has_key(start):
		return None
	for node in graph[start]:
		if node not in path:
			newpath = find_path(graph, node, end, path)
			if newpath:
				return newpath
	return None
