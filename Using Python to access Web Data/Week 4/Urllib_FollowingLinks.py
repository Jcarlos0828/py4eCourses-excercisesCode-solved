#Code Author: José Carlos del Castillo Estrada

#Excercise solved from the book "Python for Everybody" by Dr. Charles R. Severance
#Following the Coursera program "Using Python to access Web Data" by the University of Michigan

'''
Following the given URL, find the link in the position given, and repeat the given number of times,
the answer is the last name that you retrieve

Example: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Sequence of names: Fikret - Montgomery - Mhairade - Butchi --> Anayah
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

hold = input("Enter URL: ")
position = int(input("Enter position"))
count = int(input("Enter count"))

newUrl = None
for i in range(count):    
    if i == 0:
        url = hold
    else:
        url = newUrl
    print("Current URL: ", url)

    #This segment captures all the "href" that starts with the tag <a> using BEAUTIFUL SOUP
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    #Store all the tags as a list
    tags = soup('a')
    #This gets the desired URL to iterate until finding the last one
    newUrl = tags[position-1].get('href', None)

#This get just the name of the subject in the URL
print('The person in question is:', tags[position-1].contents[0])