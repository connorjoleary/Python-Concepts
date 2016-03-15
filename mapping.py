# Connor O'Leary
# Joe Pagani
global final_map
file = open('city1.txt', 'r')
file.readline()
file.readline()
file.readline()
file.readline() #reads in line titles
file.readline()

for line in file:
    print(line)



file.close()
