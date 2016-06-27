def findGcdOf2Numbers(a, b):
    if b == 0:
        return b
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b

    return b

print findGcdOf2Numbers(11, 73)
print findGcdOf2Numbers(73, 11)
print findGcdOf2Numbers(11, 22)
print findGcdOf2Numbers(22, 11)
print findGcdOf2Numbers(3918848, 1653264)
print findGcdOf2Numbers(1653264, 3918848)
print findGcdOf2Numbers(357, 234)
print findGcdOf2Numbers(234, 357)