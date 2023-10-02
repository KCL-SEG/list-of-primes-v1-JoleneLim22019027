"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    num = 2
    while (len(list) < number_of_primes):
        i = 2
        divFlag = True
        while (divFlag and i < num):
            if (num % i != 0):
                i += 1
                divFlag = True
            else:
                divFlag = False
        
        if divFlag:
            list.append(num)
        else:
            num += 1

    return list
