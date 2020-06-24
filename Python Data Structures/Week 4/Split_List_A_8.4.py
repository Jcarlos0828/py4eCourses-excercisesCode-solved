#Code Author: José Carlos del Castillo Estrada

#Excercise solved from the book "Python for Everybody" by Dr. Charles R. Severance
#Following the Coursera program "Python Data Structures" by the University of Michigan

'''
Program to store and print all unique words in the .txt in a sorted way
'''
# Use romeo.txt as the file name
fname = input("Enter file name:")
fh = open(fname)
lst = list()
for line in fh:
    sentence = line.split()
    for word in sentence:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst.sort())