#!/usr/bin/pythyon3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if a > i:
                raise Exception('Too far')
	    elif:
                result = result + i / b ** a
	    else:
                result = a + b
        finally:
            return result		
