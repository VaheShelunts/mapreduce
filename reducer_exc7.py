#!/usr/bin/env python

import sys

# Sum of all sales (values) is initialized with zero, we just started
sum_of_values = 0
count_of_purchases = 0
average_sales = 0

# Previous key is initialized with None, we just started
previous_key = None

# For each new line in the standard input 
for line in sys.stdin:
    data = line.strip().split("\t")
    key, value = data
    if previous_key != None and previous_key != key:
        sys.stdout.write("{0}\t{1}\n".format(previous_key, average_sales))
        # Sum of sales starts again with 0
        sum_of_values
        count_of_purchases = 0
        average_sales = 0

    sum_of_values += float(value)
    count_of_purchases += 1
    average_sales = sum_of_values / count_of_purchases
    # the previous key for the next iteration is the current key of the this iteration 
    previous_key = key

# write the last result to stdout
sys.stdout.write("{0}\t{1}\n".format(previous_key, average_sales))
