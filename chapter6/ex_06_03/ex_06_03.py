def count(w,l):
    c = 0
    for letter in w:
        if letter == l:
            c = c + 1
    print(c)
    
word = input("What's the word? ")
char = input("Which character should be count:")

count(word, char)

