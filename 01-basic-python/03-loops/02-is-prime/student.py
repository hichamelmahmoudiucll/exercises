# Write your code here
def is_prime(n):
    for getal in range(2, n):
        if n % getal == 0:
            return False
    return n > 1