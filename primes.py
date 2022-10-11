"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if(number_of_primes < 1):
        raise ValueError("Please enter a value that is equal to or higher than 1.")
    list = []
    x = 2
    while number_of_primes != 0:
        for q in range(2,x):
            if x % q == 0:
                break
        else:
            list.append(x)
            number_of_primes = number_of_primes - 1
        x = x + 1
    return list
