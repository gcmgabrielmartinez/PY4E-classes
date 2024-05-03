numbers = list()
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        float(num)
    except:
        continue

    numbers.append(num)

print(f"Maximum: {float(max(numbers))}")
print(f"MInimum: {float(min(numbers))}")
