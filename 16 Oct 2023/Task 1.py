#Write a program that classifies a triangle based on its side lengths.
#Given three input values representing the lengths of the sides,
#determine if the triangle is equilateral (all sides are equal),
#isosceles (exactly two sides are equal), or scalene (no sides are equal).

side_1 = int(input("Enter your first side\n"))
side_2 = int(input("Enter your second side\n"))
side_3 = int(input("Enter your third side\n"))

if (side_1 == side_2 == side_3):
  print( "Triangle is equilateral")

elif(side_1 == side_2!=side_3):
    print("Triangle is isosceles")

else:
     print("Triangle is scalene ")
