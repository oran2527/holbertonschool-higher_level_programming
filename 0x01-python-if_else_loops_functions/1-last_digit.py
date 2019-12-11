#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:	
	l = number % 10
else:
	l = abs(number) % 10 * -1
print("Last digit of {:d} is {:d} and is ".format(number, l),end="");
if l > 5:
	print(" greater than 5")
elif l < 6 and l != 0:
	print("less than 6 and not 0")
else:
	print("0".format(number, l))
