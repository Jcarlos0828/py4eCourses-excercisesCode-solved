#Code Author: José Carlos del Castillo Estrada

#Excercise solved from the book "Python for Everybody" by Dr. Charles R. Severance
#Following the Coursera program "Using Python to access Web Data" by the University of Michigan

'''
Obtain the data scrapping the site with Beautiful Soup, obtain the numbers in the "SPAN" tag and sum them
'''


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# http://py4e-data.dr-chuck.net/comments_707321.html
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the SPAN tags
allTags = soup('span')
acum = 0
for tag in allTags:
    # Look at the parts of a tag SPAN
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    acum = acum + int(tag.contents[0])
    print('Attrs:', tag.attrs)
print(acum)