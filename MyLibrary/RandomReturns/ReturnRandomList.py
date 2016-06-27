import random

def returnRandomListOfIntegers(minVal = 0, maxVal = 100, arraySize = 10):
    return map(lambda x: random.randint(minVal, maxVal), xrange(arraySize))