Original_string = "Naman"

def reverse_string(Original_string):
    # ''. join is used to join with empty character
    return''.join(reversed(Original_string))
rev_str = reverse_string(Original_string)
print(rev_str)