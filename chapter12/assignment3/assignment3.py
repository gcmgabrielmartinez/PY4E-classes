import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input("Enter count: "))
pos = int(input("Enter position: "))

names = list()

for i in range(count+1):
    names.append( re.search(r"^(.+)\_by\_(.+)\.html$",url).group(2) )
    print("retieving:", url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the span tags
    tags = soup('a')
    url = tags[pos-1].get("href", None)


print("Sequence of names: ", end = "")
for name in names:
    print(f"{name} ", end="")
print()
print("Last name in sequence: ", names[-1])