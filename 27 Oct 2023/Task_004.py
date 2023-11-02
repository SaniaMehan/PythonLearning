# Python program to multiply all numbers in a list.
import math

mul_list = [4,15,9,25]
print(mul_list)

numbers = 1
for i in mul_list:
     numbers = numbers * i
print(numbers)

numbers = [4,15,9,25]
def find_product_with_math_prod(numbers):
    product = math.prod(numbers)
    return product

print(find_product_with_math_prod(numbers))