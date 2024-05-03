fhand = open(input("Enter text file: "))

letters = dict()

for line in fhand:
    for letter in line:
        if letter.isalpha():
            letters[letter.lower()] = letters.get(letter.lower(), 0) + 1

#print(letters.items())

letters_lst = list()
for k,v in letters.items():
    letters_lst.append((k, v/sum(letters.values())*100))

letters_lst.sort()
for letter in letters_lst:
    print(letter[0], letter[1])