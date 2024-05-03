import re

reg_ex = input("Enter a regular expression: ")
fhandle = open("mbox.txt")
num = 0

for line in fhandle:
    line = line.rstrip()
    if re.search(reg_ex, line):
        num += 1

print(f"mbox.txt has {num} lines that matched {reg_ex}") 