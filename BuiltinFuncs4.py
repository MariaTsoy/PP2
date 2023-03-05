import time
import math

num = int(input("Number: "))
millisecs = int(input("Milliseconds: "))
time.sleep(millisecs / 1000)
print("Square root of", num, " after", millisecs, "milliseconds is", math.sqrt(num))
