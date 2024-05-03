fhand = open(input("Enter text file: "))

hours = dict()

for line in fhand:
    words = line.split()
    if len(words) < 7 or words[0] != 'From' : continue
    else:
        hour = words[-2].split(":")
        hours[hour[0]] = hours.get(hour[0], 0) + 1

#print(hours.items())
hours_lst = list()
for k,v in hours.items():
    hours_lst.append((k, v))

hours_lst.sort()
for hour in hours_lst:
    print(hour[0], hour[1])