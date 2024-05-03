fhand = open(input("Enter text file: "))

submits = dict()

for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) < 3 or words[0] != 'From' : continue
    elif words[2] in submits:
        submits[words[2]] += 1
    else:
        submits[words[2]] = 1

    #print(words[2])

print(submits)