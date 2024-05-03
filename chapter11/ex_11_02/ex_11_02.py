import re

fhandle = open(input("Enter file: "))
number = 0
count = 0
    
for line in fhandle:
    line = line.rstrip()
    x = re.findall("^New Revision: ([0-9]+)", line)
    if len(x) > 0:
        #print(x)
        number += int(x[0]) #re.findall returns a list
        count += 1

print(int(number/count))