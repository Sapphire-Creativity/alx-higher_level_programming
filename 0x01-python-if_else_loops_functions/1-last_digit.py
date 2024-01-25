#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

def interpret_last_digit(number):
    number_str = str(number)
    last_digit = int(number_str[-1])
    
    if last_digit < 6 and last_digit != 0:
        print("Last digit of {number} is {number} and is less than 6 and not 0")
