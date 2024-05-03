# Use the file name mbox-short.txt or mbox.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
numbers = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        numbers += float(line.split(":")[1])
        count += 1
    
print("Average spam confidence:", numbers/count)
