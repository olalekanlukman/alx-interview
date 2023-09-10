#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    if n <= 1:
        return n
    
    # Initialize an array to store the minimum operations required for each position
    dp = [0] * (n + 1)
    
    # Start from position 2 (first H already exists)
    for i in range(2, n + 1):
        dp[i] = i  # Default to just pasting i times
        
        # Try all possible factors of i
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    
    return dp[n]
