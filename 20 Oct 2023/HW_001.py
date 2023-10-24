# user_input = input("Enter the string")
# Palindrome checker
# Reverse the string & match with the old string it should be same
# By using traditional method or By using Build-in functions

def reverse_string(input_string):
    reverse_str = ""
    for char in input_string:
        reverse_str = char + reverse_str
    return reverse_str


original_string = "ABCD"
rev_str = reverse_string(original_string)
print(rev_str)

if original_string == rev_str:
    print("It is palindrome")
else:
    print("It is not")