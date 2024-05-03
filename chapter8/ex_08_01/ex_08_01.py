def chop(lst):
    del lst[0]
    del lst[-1]

def middle(lst):
    del lst[0]
    del lst[-1]
    return lst

lsample = ["a", "b", "c", "d", "e"]

chop(lsample)
print(lsample)

lsample = middle(lsample)
print(lsample2)
