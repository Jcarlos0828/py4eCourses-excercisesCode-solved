#Code Author: José Carlos del Castillo Estrada

#Excercise solved from the book "Python for Everybody" by Dr. Charles R. Severance
#Following the Coursera program "Using Python to access Web Data" by the University of Michigan

'''
Following the given URL (json), extract from the key "comments", 
the attribute "count" to sum all in the file the numbers 

Example: http://py4e-data.dr-chuck.net/comments_707324.json
'''

import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    URL = input('Enter json URL: ')
    if len(URL) < 1: break
    print("Retrieving ", URL)
    connection = urllib.request.urlopen(URL, context=ctx)
    data = connection.read()

    #This line prints the whole XML
    #print('This is the whole web site',data.decode())
    
    print('Retrieved', len(data), 'characters')
    info = json.loads(data)
    print('Number of keys:', len(info))
    #The main keys in the file
    print(info.keys())
    total = 0
    for item in info['comments']:
        total = total + (item["count"])
    print(total)