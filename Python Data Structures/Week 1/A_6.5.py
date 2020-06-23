#Code Author: José Carlos del Castillo Estrada

#Excercise solved from the book "Python for Everybody" by Dr. Charles R. Severance
#Following the Coursera program "Python Data Structures" by the University of Michigan

'''
Program to extract the number in the string 'text' as a float
'''
text = "X-DSPAM-Confidence:    0.8475"
index = text.find("0")
num = float(text[index:])
print(num)

#Alternative code to substitute lines 10-12
#print(float(text[text.find("0"):]))
