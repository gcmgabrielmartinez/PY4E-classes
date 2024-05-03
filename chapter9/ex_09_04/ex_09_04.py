fhand = open(input("Enter text file: "))

emails = dict()

for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) < 3 or words[0] != 'From' : continue
    #else:
    #    emails[words[1]] = emails.get(words[1], 0) + 1
    elif words[1] in emails:
        emails[words[1]] += 1
    else:
        emails[words[1]] = 1

    #print(words[2])

max_subs = None
max_email = None
for email in emails:
    if max_subs is None or emails[email] > max_subs:
        max_subs = emails[email]
        max_email = email

print(max_email, max_subs)