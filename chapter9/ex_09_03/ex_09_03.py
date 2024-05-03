fhand = open(input("Enter text file: "))

emails = dict()

for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) < 3 or words[0] != 'From' : continue
    elif words[1] in emails:
        emails[words[1]] += 1
    else:
        emails[words[1]] = 1

    #print(words[2])

print(emails)