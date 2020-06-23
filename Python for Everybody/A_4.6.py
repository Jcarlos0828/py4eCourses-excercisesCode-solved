#Code Author: José Carlos del Castillo Estrada

#Excercise solved from the book "Python for Everybody" by Dr. Charles R. Severance
#Following the Coursera program "Python for Everybody" by the University of Michigan


def computepay(h,r):
    total = 0
    if h > 40:
        total = h % 40 * (r*1.5)
        total = total + 40 * r
    else:
        total = h * r
    return total

hrs = float(input("Enter Hours:"))
pay = float(input("Enter payment:"))
p = computepay(hrs,pay)
print("Pay",p)