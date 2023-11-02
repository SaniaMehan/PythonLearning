# Dict

my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 95}
print(my_dict)

# If you have a duplicate key, latest value of key will be used!!
# Retrive all the values & keys
keys = my_dict.keys()
values = my_dict.values()
print(keys)
print(values)

# Get all the keys into a List
keys_list = list(keys)
print(keys_list)

print(keys_list[0])
print(keys_list[1])
print(keys_list[2])



my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 95}

# Dict - Key and Value

# my_dict.clear()

print(my_dict)

copy_my_dict = my_dict.copy()
print(copy_my_dict)


print(my_dict.items()) # will print into set
set_dic = set(my_dict.items())
print(set_dic)
