#Code Author: José Carlos del Castillo Estrada

#Excercise solved from the book "Python for Everybody" by Dr. Charles R. Severance
#Following the Coursera program "Python Data Structures" by the University of Michigan

'''
Program to find all sentences that starts with "From " to obtain the emails 
and count how many repetitions were found 
'''

#Just press enter to run
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for sentence in fh:
    if sentence.startswith('From '):
        divideSent = sentence.split()
        print(divideSent[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
