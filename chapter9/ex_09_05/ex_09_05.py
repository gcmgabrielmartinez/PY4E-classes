fhand = open(input("Enter text file: "))

emails = dict()

for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) < 3 or words[0] != 'From' : continue
    else:
        domain = words[1].split("@")[1]
        emails[domain] = emails.get(domain, 0) + 1 #correspond to the if condition above
        #if domain in emails:
        #    emails[domain] += 1
        #else:
        #    emails[domain] = 1

    #print(words[2])

print(emails)