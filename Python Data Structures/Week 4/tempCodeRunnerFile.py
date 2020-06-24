fname = input("Enter file name:")
fh = open(fname)
lst = list()
for line in fh:
    lst.append(line)
print(lst)