#Use the ternary operator to find the maximum of three numbers entered by the user.
num1 = int (input("Enter the one number \n"))
num2 = int (input("Enter the second number \n"))
num3 = int (input("Enter the third number \n"))

maximum = num1 if (num1 > num2 and num1 > num3) else (num2 if num2 > num3 else num3)
print("The maximum number is:", maximum)

# Develop a Python script that calculates the square and cube of a given number.
num = 10
print("the square of number is: ",10**2,"")

cube =12
print("the cube of number is: ",12**3,"")