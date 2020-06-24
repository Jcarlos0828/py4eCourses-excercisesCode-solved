#Building a List from Scratch
myList = list() #list() is the data type
myList.append('book')
myList.append(99)
print(myList)
print(type(myList))


#Is something in a list? EXAMPLE
xList = [1,9,21,10,16]
print(9 in xList)

ans = 20 in xList
#The type of the variable is a bool
print(type(ans))

'''
Questions?
What's the time complexity of this? My guess is O(n), have to check
'''