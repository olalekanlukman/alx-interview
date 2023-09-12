#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """x - rounds
    nums - numbers list
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Build a set of numbers that have not been picked yet
        remaining = set(range(2, n + 1))
        turn = 'Maria'

        while True:
            # Find the next prime number
            prime = 0
            for num in remaining:
                if is_prime(num):
                    prime = num
                    break
            
            # If no prime number is found, the current player loses
            if prime == 0:
                if turn == 'Maria':
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            # Remove the prime number and its multiples from the remaining set
            remaining -= set(prime * i for i in range(1, n // prime + 1))

            # Switch the turn
            turn = 'Ben' if turn == 'Maria' else 'Maria'

    # Determine the winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
