# Python program to sum all numbers in a list.

sum_list = [4,78,65,89,245,104,15,9,525,25]
print(sum_list)
print('The sum of all the numbers in the list is :',sum(sum_list))

numbers = [4,78,65,89,245,104,15,9,525,25]
def sumnumbers(numbers):
  total = sum(numbers)
  return total

print(sumnumbers(numbers))

numbers = [4,78,65,89,245,104,15,9,525,25]
a = sum(numbers)
print("sum of number",a)