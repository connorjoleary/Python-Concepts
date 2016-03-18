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
        #sorts each line into three groups and skips lines with '-------'
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


#Task 1 is below function
def task_1(city):
        i = 0
        for node in final_map[city]: 
                i += 1;
        print(i)
print 'task 1'
#takes input
city = raw_input('Enter the city: ')
task_1(city)


#Task 2 is below function
def task_2(city1, city2):
        if city2 in final_map[city1]:
                print("Yes")
        else:
                print("No")
print 'task 2'
#takes input
city1 = raw_input('Enter the city: ')
city2 = raw_input('Enter the city: ')
task_2(city1, city2)


#Task 3 is below function
def find_connections(start, end, d, path=[]):
        path = path + [start]
        if start == end:
                return path
        if start not in final_map or len(path)>d:
                return None
        for node in final_map[start]:
                if node not in path:
                        newpath = find_connections(node, end, d, path)
                        if newpath:
                                return newpath
        return None
print 'task 3'
#takes input
n=raw_input('Enter the jumps: ')
city1 = raw_input('Enter the city: ')
city2 = raw_input('Enter the city: ')
d=0
path = find_connections(city1, city2, int(n))

#prints out info
if path is not None:
        print 'Yes'
        print(path)
        for index in range(len(path)):
                if index >= 1:
                        d += int(final_map[path[index-1]][path[index]])
        print(d)
else:
        print 'No'


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
print 'task 4'
#takes input
city1 = raw_input('Enter the city: ')
city2 = raw_input('Enter the city: ')
path = find_path(city1, city2)

#prints out info
if path is None:
        print 'No'
else:
        for index in range(len(path)):
                if index >= 1:
                        d += int(final_map[path[index-1]][path[index]])

        print(path)
        print(d)
