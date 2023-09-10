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

# Example usage
n = 9
print(minOperations(n))  # Output: 6
