fruit = input("What's the fruit? ")
index = len(fruit)
    
while index > 0:
    letter = fruit[index-1]
    print(letter)
    index = index - 1

#print(fruit[:]) [:] passes the entire string
