import socket
import time

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


content = b""
while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    time.sleep(0.25)
    content = content + data

mysock.close()

# Look for the end of the header (2 CRLF)
pos = content.find(b"\r\n\r\n")

# Skip past the header and save the picture data
content = content[pos+4:]
print(content.decode())
