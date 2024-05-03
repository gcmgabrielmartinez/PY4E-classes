fhand = open("mbox-short.txt")

for line in fhand:
    print(line.rstrip().upper())