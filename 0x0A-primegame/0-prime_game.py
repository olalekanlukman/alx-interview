#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""




def isWinner(x, nums):
    # Function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Function to play the game
    def play_game(n):
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        turn = 0  # 0 for Maria, 1 for Ben
        while primes:
            prime = primes.pop(0)
            primes = [p for p in primes if p % prime != 0]
            turn = 1 - turn
        return "Maria" if turn else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

