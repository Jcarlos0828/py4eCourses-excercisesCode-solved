#Code Author: José Carlos del Castillo Estrada

#Excercise solved from the book "Python for Everybody" by Dr. Charles R. Severance
#Following the Coursera program "Python Data Structures" by the University of Michigan

'''
Program to find all sentences that starts with "From " to obtain the emails and store them in a dictionary,
count how many repetitions were found, and then display the email that sent the most emails and how many were sent
'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emails = dict()
for lines in handle:
    if lines.startswith('From '):
        words = lines.split()
        emails[words[1]] = emails.get(words[1],0) + 1
bigWord = None
bigCount = None
for key,valueIter in emails.items():
    if bigCount is None or valueIter > bigCount:
        bigWord = key
        bigCount = valueIter

print(bigWord, bigCount)