
def computegrade(s):
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

try:
    score = float(input("Enter Score: "))
    if score > 1.0 or score < 0:
        raise ValueError

except ValueError: 
        print("Bad score")
        quit()

computegrade(score)
