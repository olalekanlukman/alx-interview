#!/usr/bin/python3

""" Contains makeChange function"""

def makeChange(coins, total):
     """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0
    
    # Initialize the dp array with inf for all values except for 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Loop through the total amount
    for i in range(1, total + 1):
        # For each coin, update the dp value
        for c in coins:
            if i - c >= 0 and dp[i - c] != float('inf'):
                dp[i] = min(dp[i], dp[i - c] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1
