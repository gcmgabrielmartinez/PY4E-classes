import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

#http://py4e-data.dr-chuck.net/comments_42.json
#http://py4e-data.dr-chuck.net/comments_1874430.json

html = urllib.request.urlopen(url, context=ctx).read()

info = json.loads(html)

#print("User count:", len(info["comments"]))

sum = 0
for user in info["comments"]:
    sum += int(user["count"])

print(sum)
