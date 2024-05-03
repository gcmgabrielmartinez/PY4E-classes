import urllib.request, urllib.parse, urllib.error

try:
    url = input("Enter - ")
    fhand = urllib.request.urlopen(url)
    
except:
    print("Invalid url")
    quit()

count = 0
for line in fhand:
    for char in line.decode():
        print(char, end = "")
        count += 1
        if count == 3000: break
    if count == 3000: break

#    print(line.decode().strip()) #you need to decode, because url is encrypted in bytes

print("\nCount:",count)
#http://data.pr4e.org/romeo.txt