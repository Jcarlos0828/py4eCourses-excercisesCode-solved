#Code Author: José Carlos del Castillo Estrada

counts = dict()
names = ['csev','cwen', 'csev', 'zqian', 'cwen', 'cwen', 'cwen']

for reading in names:
    if reading not in counts:
        counts[reading]  = 1
    else:
        counts[reading] = counts[reading] + 1
print(counts)

#Another way of doing the same code in lines 6-11
#.get() do a "return" of what is in the second position
'''
for reading in names:
    counts[reading] = counts.get(reading, 0) + 1
print(counts)
'''
print(dir(counts))