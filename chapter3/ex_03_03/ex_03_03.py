try:
    score = input("Enter Score: ")
    s = float(score)
    if s > 1.0 or s < 0:
        raise ValueError

except ValueError: 
        print("Bad score")
        quit()

if s >= .9:
    print("A")
elif s >= .8:
    print("B")
elif s >= .7:
    print("C")
elif s >= .6:
    print("D")
else:
    print("F")
