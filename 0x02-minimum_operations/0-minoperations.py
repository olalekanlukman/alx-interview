#!/usr/bin/python3
""" Module for 0-minoperations"""

def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    if n == 1:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)
    return n



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
