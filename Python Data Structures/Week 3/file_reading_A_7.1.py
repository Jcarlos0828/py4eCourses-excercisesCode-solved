#Code Author: José Carlos del Castillo Estrada

#Excercise solved from the book "Python for Everybody" by Dr. Charles R. Severance
#Following the Coursera program "Python Data Structures" by the University of Michigan

'''
Program to print all the lines in the file as read
'''
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    print(line.upper().strip())

#Otra manera de hacerlo
''' 
arch = open("words.txt")
for line in arch:
    line.rstrip()
    print(line.upper())
''' 