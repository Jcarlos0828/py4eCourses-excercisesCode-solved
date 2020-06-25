#Code Author: José Carlos del Castillo Estrada

#Excercise solved from the book "Python for Everybody" by Dr. Charles R. Severance
#Following the Coursera program "Using Python to access Web Data" by the University of Michigan

'''
Program to find all numbers in a .txt using Regular Expresssions and sum them
'''
import re
#Insert your path (for windows works)
#text = open(r'C:\users\Path\file\Using Python to access Web Data\Week 2\regex_sum42.txt')
text = open('regex_sum707319.txt')
sentence = list()
acum = 0
for i in text:
    i.rstrip()
    coinc = re.findall('([0-9]+)', i)
    if len(coinc) < 1 : 
        continue
    for j in coinc:
        acum = acum + int(j)
    sentence.append(coinc)
print("Acum:",acum)
