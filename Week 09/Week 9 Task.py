# Week 9

import sys

operation = sys.argv[1]

def sum_numbers(nums):
    return sum(nums)

def multiply_numbers(nums):
    for x in nums:
         result = result * x
    return result 

numbers_to_sum = [int(i) for i in sys.argv[2:]]

if operation == "add":
    print(sum_numbers(numbers_to_sum))
elif operation == "multiply":
    print(multiply_numbers(numbers_to_sum))
