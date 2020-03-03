 """
 Write a Python script that given the length n, by user input, which corresponds to two sides of a right-angled triangle, prints the length of the hypotenuse. Please use round with two decimal places.
 """
import math
n = int(input())
h = round(math.sqrt(n ** 2 + n ** 2), 2)
print(h) 
