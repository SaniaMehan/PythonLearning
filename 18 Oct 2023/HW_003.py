# Fibonaci series
# 0,0+1, 0+1+1,
# n = 7

#a = 0
#b = 1
#we can mulitple initialize in same line too
a, b = 0, 1
while a < 10:
    print(a, end=' ')
    a, b = b, a + b

#n =int(input("enter number"))
#a=0
#b=1
#print(a)
#print (b)
#for i in range(2,n+1):
    #c=a+b
   # a=b
   # b=c
   # print(c)