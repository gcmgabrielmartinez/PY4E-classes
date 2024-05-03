import socket

try: 
    url = input("Enter - ")
    host = url.split("/")[2]
    #print(host)

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

except:
    print("invalid url")
    exit()

count = 0
while count < 3000:
    data = mysock.recv(512)
    if len(data) < 1:
        break

    for char in list(data.decode()):
        count += 1
        print(char, end="")
        if count == 3000: break
    #print(data.decode(),end='')    

print("\nCount:",count)

mysock.close()