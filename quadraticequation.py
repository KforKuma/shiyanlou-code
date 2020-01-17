#! /usr/bin/env python3
import math
a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))
d = b**2 - 4*a*c
if d < 0:
    print("ROOTS are imaginary")
elif d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Root 1 = {}\nRoot 2 = {}".format(root1,root2))
else:
    root = (-b) / (2*a)
    print("The uniq root is ",root)
