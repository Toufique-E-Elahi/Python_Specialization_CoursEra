# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
print('Retrieving:',url)
# Retrieve all of the anchor tags
tags = soup('a')

#print(tags)
for i in range(7):
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print(tags[2].contents[0])
    #print('URL:', tags[tag].get('href', None))
    #print('Contents:', tags[tag].contents[0])
    ans=tags[17].contents[0]
    url=tags[17].get('href', None)
    print('Retrieving:',url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')

print(ans)
    #print('Attrs:', tag.attrs)
