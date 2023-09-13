#!/usr/bin/python3

""" Contains makeChange function"""


from typing import List

def makeChange(coins: List[int], total: int) -> int:
    """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Build up dp array
    for i in range(1, total + 1):
        for c in coins:
            if i - c >= 0 and dp[i - c] != -1:
                dp[i] = min(dp[i], dp[i - c] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1
