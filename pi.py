# For PiDay 2020 - Created by Brent Hartley using the Chudnovsky Algorithm
# Program called Pi.py (pronounced pie (dot) pie), using a function called PiDay, and
# Run on a raspberry pi, on 3-14-2020
# Variables spell p, i, d, a, y, because, why not?
# This change to the digit limited program lets the program caculate pi for a pre-defined number of seconds
# Change time allotment by changing variable 'time_limit'

import decimal
import sys
import string
import time

# Define start time and time limit. Time limit is equal to 3 minutes 14 seconds because 3.141.

start_time = time.time()
time_limit = (60 * 3) + (14)

# Define the Chudnovsky Algorithm and call it PiDay because why not?

def PiDay():
    x, p, i, d, a, y,  = 1, 0, 1, 1, 3, 3, 
    while True:
        if 4*x+p-i < a*i:
            yield a
            ap = 10*(p-a*i)
            a  = ((10*(3*x+p))//i)-10*a
            x  *= 10
            p  = ap
        else:
            ap = (2*x+p)*y
            aa = (x*(7*d)+2+(p*y))//(i*y)
            x  *= d
            i  *= y
            y  += 2
            d += 1
            a  = aa
            p  = ap
pi_digits = PiDay()
i = 0
for d in pi_digits:
    sys.stdout.write(str(d))
    # Add 1 to the line break counter
    i += 1
    # Print a line break after 60 digits and reset the line break counter
    if i == 60: print(""); i = 0;
    if time.time() - start_time > time_limit: sys.exit("Caculation Complete")
