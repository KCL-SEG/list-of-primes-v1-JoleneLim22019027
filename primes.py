"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = [2]
    num = 2
    while (len(list) < number_of_primes):
        pFlag = True
        i = 0
        while pFlag and (list[i] <= num):
            if (num % list[i] == 0):
                pFlag = False
            else:
                i += 1
        if pFlag:
            list.append(num)
        
        num += 1

    return list
