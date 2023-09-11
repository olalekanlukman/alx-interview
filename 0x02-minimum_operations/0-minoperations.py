#!/usr/bin/python3
""" Module for 0-minoperations"""

def minOperations(n):
    if n == 1:
        return 0
    if n <= 0 or n % 1 != 0:
        return 0

    operations = 0
    i = 2

    while n > 1:
        while n % i == 0:
            operations += i
            n = n // i
        i += 1

    return operations


# def minOperations(n):
#     """
#     minOperations
#     Gets fewest # of operations needed to result in exactly n H characters
#     """
#     H_count = 1
#     copy = 0
#     command_count = 0

#     for i in range(0, n):

#         if H_count == n:
#             return command_count
#         if n % H_count == 0:
#             copy = H_count
#             H_count += copy
#             command_count += 2
#         else:
#             H_count += copy
#             command_count += 1
#     return command_count
