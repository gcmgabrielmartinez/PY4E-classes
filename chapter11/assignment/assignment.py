import re

#fhandle = open("sample_sum_42.txt")
fhandle = open("test_sum_1874425.txt")
number = 0
    
for line in fhandle:
    line = line.rstrip()
    x = re.findall("([0-9]+)", line)
    if len(x) > 0:
        #print(x)
        x = map(int, x)
        number += sum(x) #re.findall returns a list

print(int(number))

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)