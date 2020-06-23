#Code Author: José Carlos del Castillo Estrada

#Excercise solved from the book "Python for Everybody" by Dr. Charles R. Severance
#Following the Coursera program "Python Data Structures" by the University of Michigan

'''
Program to find coincidences of the type
    --> X-DSPAM-Confidence:    0.8475
and obtain the float average of the numbers in those lines
'''
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
acum = 0
numOfValues = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        acum = acum + float(line[line.find(':')+1:].strip())
        numOfValues = numOfValues + 1
acum = acum / numOfValues
print("Average spam confidence:",acum)