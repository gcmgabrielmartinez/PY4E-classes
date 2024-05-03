largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n = int(num)
        if largest is None and smallest is None:
            largest = n
            smallest = n
        else:
            if n < smallest:
                smallest = n
            if n > largest:
                largest = n
            
    except:
        print("Invalid input")
        pass

print("Maximum is", largest)
print("Minimum is", smallest)