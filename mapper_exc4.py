#!/usr/bin/env python

# Import the sys library 
# for writing and reading the standard input and output
import sys


# For each new line in the standard input (stdin) 
for line in sys.stdin:

    # split the line at the tabulator ("\t")
    # strip removes whitespaces and new lines at the beginning and end of the line
    # the result is a tuple with 6 elements
    data = line.strip().split("\t")

    if len(data) != 6:
        raise Exception('Tuple should have 6 elements')
    # store the 6 elements of the tuple in seperate variables
    date, time, item, category, sales, payment = data
    sys.stdout.write("{0}\t{1}\n".format(payment, sales))

