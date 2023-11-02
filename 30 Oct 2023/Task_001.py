#Find the maximum and minimum elements in a tuple.
# One way
my_tuple = (15, 8, 25, 36, 42, 10)
print(max(my_tuple))
print(min(my_tuple))

# Second way
my_tuple = (15, 8, 25, 36, 42, 10)
sorted_tuple = sorted(my_tuple)
max_value = sorted_tuple[-1]
min_value = sorted_tuple[0]
print(max_value)
print(min_value)