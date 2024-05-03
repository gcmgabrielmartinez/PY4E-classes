count = 0
total = 0
while True:

    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n = int(num)
        count += 1
        total += n
                        
    except:
        print("Invalid input")
        pass

print(total, count, total/count)