#!/usr/bin/env python

import sys



# Sum of all sales (values) is initialized with zero, we just started
count_of_purchases = 0

# Previous key is initialized with None, we just started
previous_key = None

# For each new line in the standard input 
for line in sys.stdin:

    # split the line at the tabulator ("\t")
    # strip removes whitespaces and new lines at the beginning and end of the line
    # The result is a tuple with 2 elements
    data = line.strip().split("\t")

    # Store the 2 elements of this line in seperate variables
    key, value = data

    if previous_key != None and previous_key != key:
        # Then write the result of the old key (Key=category, Value= Sum of Sales)
        # to the standart output (stdout)
        # Key and value are seperated by a tab (\t)
        # Line ends with new line (\n)
        if count_of_purchases > 114:
            sys.stdout.write("{0}\t{1}\n".format(previous_key, count_of_purchases))
        # Sum of sales starts again with 0
        count_of_purchases = 0


    count_of_purchases += 1
    # the previous key for the next iteration is the current key of the this iteration 
    previous_key = key

    # write the last result to stdout
if count_of_purchases > 114:
    sys.stdout.write("{0}\t{1}\n".format(previous_key, count_of_purchases))