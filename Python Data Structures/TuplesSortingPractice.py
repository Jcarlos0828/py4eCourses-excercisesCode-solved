#Program to sort elements BY KEY in dictionary using tuples
dic = {'a':10, 'c':1,'b':22}
t = sorted(dic.items())
print(t)

#Sort BY VALUE in a dictionary using tuples, DESC way 
dic2 = {'a':10, 'b':1,'c':22}
tmp = list()
for k, v in dic2.items():
    tmp.append((v,k))
tmp = sorted(tmp, reverse=True)
print(tmp)