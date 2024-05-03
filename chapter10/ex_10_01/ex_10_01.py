fhand = open(input("Enter text file: "))

emails = dict()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From' : continue
    else:
        emails[words[1]] = emails.get(words[1], 0) + 1

#print(emails.items())
emails_lst = list()
for k,v in emails.items():
    emails_lst.append((v, k))

emails_lst.sort(reverse = True)

print(emails_lst[0][1], emails_lst[0][0])

#max_subs = None
#max_email = None
#for email in emails:
#    if max_subs is None or emails[email] > max_subs:
#        max_subs = emails[email]
#        max_email = email

#print(max_email, max_subs)