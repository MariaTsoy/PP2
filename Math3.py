import math

sides = int(input("Number of sides: "))
sideLen = int(input("Length of a side: "))
print("Area of polygon: ", sides * pow(sideLen, 2) / (4 * math.tan(math.pi / sides)))
