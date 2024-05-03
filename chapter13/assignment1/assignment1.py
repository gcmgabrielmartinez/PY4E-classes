import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#http://py4e-data.dr-chuck.net/comments_42.xml
#http://py4e-data.dr-chuck.net/comments_1874429.xml

html = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(html)
results = tree.findall('comments/comment/count')


sum = 0
for result in results:
    sum += int(result.text)
    #print(result.text)

print(sum)
