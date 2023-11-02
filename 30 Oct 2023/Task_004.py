#Remove a key-value pair from the dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(my_dict)
print(my_dict.values())
print((my_dict.keys()))

remove = my_dict.pop('a')
print(remove)
print(my_dict)

# Second method
my_dict1 = {"name": "John", "age": 30, "city": "New York"}
del my_dict1["name"]
print(my_dict1)

#Third method
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Remove and get an arbitrary key-value pair
removed_pair = my_dict.popitem()