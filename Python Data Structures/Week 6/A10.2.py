#Code Author: José Carlos del Castillo Estrada

#Excercise solved from the book "Python for Everybody" by Dr. Charles R. Severance
#Following the Coursera program "Python Data Structures" by the University of Michigan

'''
Program to find all sentences that starts with "From " to obtain all the hours an email
was sent and store them in a dictionary, count how many repetitions were found in the hours,
and then display the tuples in the dictionary in ASCENDENT order sorting by HOURS
'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours = dict()
for lines in handle:
    if lines.startswith('From '):
        #To obtain the hour from the whole sentence
        sentence = lines.split()
        sentence = sentence[5]
        sentence = sentence.split(':')
        sentence = sentence[0]
        #To save the hour in the dictionary, if it does not exist, add it
        hours[sentence] = hours.get(sentence,0) + 1
#To sort by values
auxL = sorted(hours.items())
for k, v in auxL:
    print(k, v)

