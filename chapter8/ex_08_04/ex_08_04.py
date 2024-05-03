fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for word in line.rstrip().split():
        if word in lst:
            continue
        else:
            lst.append(word)
        #print(lst)
lst.sort()
print(lst)