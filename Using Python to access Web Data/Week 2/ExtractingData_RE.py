import re
text = open('regex_sum42.txt')
sentence = list()
for i in text:
    i.rstrip()
    coinc = re.findall('[0-9]', i)
    sentence.append(coinc)
print(sentence)