fhandle = open("words.txt")
order = 0
dict_ap = dict()

for lines in fhandle:
    for word in lines.split():
        if word in dict_ap:
            continue
        else:
            dict_ap[word] = order
            order += 1

print(dict_ap)