import random

def generateRandomArray(minVal = 0, maxVal = 100, arraySize = 10):
    return map(lambda x: random.randint(minVal, maxVal), xrange(arraySize))

import sys

def findmaximumPairwiseSum(l):
    maximum = - sys.maxint - 1
    secondmaximum = maximum

    for i in l:
        if i > maximum:
            secondmaximum = maximum
            maximum = i
        elif i > secondmaximum:
            secondmaximum = i

    print maximum, secondmaximum
    return maximum * secondmaximum



l = generateRandomArray()

print l
print sorted(l)
print findmaximumPairwiseSum(l)
