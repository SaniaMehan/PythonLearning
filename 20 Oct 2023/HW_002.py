#Second way of palindrome checker
# By built in function

Original_string = "Sania"
rev_string =  Original_string[::-1]
print(rev_string)

if Original_string == rev_string:
    print("Palindrome")
else:
    print("It is not a palindrome")

#If we put into a function

Original_string = "Sania"
def is_palindrome(Original_string):
    rev_string = Original_string[::-1]
    print(rev_string)


if Original_string == rev_string:
    print("Palindrome")
else:
    print("It is not a palindrome")

(is_palindrome(Original_string))