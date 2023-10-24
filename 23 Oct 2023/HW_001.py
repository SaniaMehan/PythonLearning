# Lambda expression to triple power 2**3 a number

output= lambda a:a**3
print(output(2))

#Function with a Parameter which can do x^y

x= int(input("Enter the Value of X : \n"))
y = int(input("Enter the Value of Y : \n"))

def power(x, y):
    result = x ** y
    return result
print(power(x, y))
