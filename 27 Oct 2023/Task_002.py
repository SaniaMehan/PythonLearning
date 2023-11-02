# Python program to find the smallest number in a list.

min_list = [4,78,65,89,245,104,15,9,525,25]
print(type(min_list))
print(min_list)
print('The smallest number in the list is :',min(min_list))

numbers = [4,78,65,89,245,104,15,9,525,25]
def find_smallest_with_min(numbers):
    smallest = min(numbers)
    return smallest

print(find_smallest_with_min(numbers))

numbers = [4,78,65,89,245,104,15,9,525,25]
a = min(numbers)
print(a)