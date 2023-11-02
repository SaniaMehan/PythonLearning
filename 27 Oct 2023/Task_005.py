#Python program to count the number of strings in a list where the string length
#is 2 or more and the first and last character are the same.


string =['rudr','sania', 'mehan', 'sanjay','ar']
print(len(string))
print(string)
if len(string)>=2 or string[0]==string[-1]:
    x=len(string)
    print('The Length of the String is ::',x)
else:
    print('The Length of the string is less than 2 or the 1st and last character of the '
          'string is not same!!')