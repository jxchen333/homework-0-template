"""
Egyptian algorithm
"""

def egyptian_multiplication(a, n):
    """
    returns the product a * n

    assume n is a nonegative integer
    """
    def isodd(n):
        """
        returns True if n is odd
        """
        return n & 0x1 == 1

    if n == 1:
        return a
    if n == 0:
        return 0

    if isodd(n):
        return egyptian_multiplication(a + a, n // 2) + a
    else:
        return egyptian_multiplication(a + a, n // 2)


if __name__ == '__main__':
    # this code runs when executed as a script
    for a in [1,2,3]:
        for n in [1,2,5,10]:
            print("{} * {} = {}".format(a, n, egyptian_multiplication(a,n)))
            print("{} ^ {} = {}".format(a, n, egyptian_multiplication(a,n)))


def power(a, n):
    """
    computes the power a ** n

    assume n is a nonegative integer
    """
    # copy the code from the template, since the idea is similar
    def isodd(n):
        """
        returns True if n is odd
        """
        return n & 0x1 == 1
    
    if n == 1:
        return a # a^1=a
    if n == 0:
        return 1 # a^0=1

    if isodd(n):
        return power(a * a, n // 2) * a # a^(2k+1) = (a^2)^k * a
    else:
        return power(a * a, n // 2) # a^(2k) = (a^2)^k

if __name__ == '__main__':
    # this code runs when executed as a script
    print('------------POWER-------------------------------')
    for a in [1,2,3]:
        for n in [1,2,5,10]:
            print("{} ^ {} = {}".format(a, n, power(a,n)))