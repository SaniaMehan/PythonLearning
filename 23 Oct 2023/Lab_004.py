original_str= "Naman"
reverse_str = lambda original_str : original_str[::-1]

if reverse_str("Naman") == original_str:
    print("palindrome")
else:
    print("Its not")