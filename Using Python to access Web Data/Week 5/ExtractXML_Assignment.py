#Code Author: José Carlos del Castillo Estrada

#Excercise solved from the book "Python for Everybody" by Dr. Charles R. Severance
#Following the Coursera program "Using Python to access Web Data" by the University of Michigan

'''
Following the given URL (XML), extract from the tag <count>, to sum the numbers inside

Example: http://py4e-data.dr-chuck.net/comments_707323.xml
'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    URL = input('Enter URL: ')
    if len(URL) < 1: break
    print("Retrieving ", URL)
    uh = urllib.request.urlopen(URL, context=ctx)

    data = uh.read()
    
    print('Retrieved', len(data), 'characters')
    #This line prints the whole XML
    #print('This is the whole web site',data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('comments/comment')
    total = 0
    for item in results:
        print('Number',item.find('count').text)
        total = int(item.find('count').text) + total
    print("Total: ", total)
    break