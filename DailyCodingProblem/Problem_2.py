#!/usr/bin/env python3

'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

def with_division(list_in):
    product = list_in[0]
    for i in list_in[1:]:
        product *= i

    return [product / i for i in list_in]

def without_division(list_in):
    output = []
    for i in range(len(list_in)):
        product = int(list_in[(i+1)%len(list_in)] != 0)

        for j in range(len(list_in)):
            if i == j:
                continue
            product *= list_in[j]

        output.append(product)

    return output

assert with_division([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert with_division([3, 2, 1]) == [2, 3, 6]

assert without_division([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert without_division([3, 2, 1]) == [2, 3, 6]

