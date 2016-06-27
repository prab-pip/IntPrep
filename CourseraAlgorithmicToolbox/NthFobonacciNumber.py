def getNthFobonacciNumber(n):
    nMinus1 = 1
    nMinus2 = 0
    if n == nMinus2 or n == nMinus1:
        return n
    else:
        for i in xrange(n-1):
            nMinus1 = nMinus1 + nMinus2
            nMinus2 = nMinus1 - nMinus2

        return nMinus1

print getNthFobonacciNumber(1000)