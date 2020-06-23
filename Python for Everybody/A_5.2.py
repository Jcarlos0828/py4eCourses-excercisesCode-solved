#Code Author: José Carlos del Castillo Estrada

#Excercise solved from the book "Python for Everybody" by Dr. Charles R. Severance
#Following the Coursera program "Python for Everybody" by the University of Michigan 


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num = int(num)
        if smallest is None:
            smallest = num
        elif num < smallest:
            smallest = num
        if largest is None:
            largest = num
        elif num > largest:
            largest = num
    except:
        print("Invalid input")


print("Maximum is", largest)
print("Minimum is", smallest)