class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = str(n)
        while len(s) != 1:
            n = map(lambda x: int(x)*int(x), s)
            # print n
            n = sum(n)
            s = str(n)
        # print int(s)
        return int(s) == 1

if __name__ == '__main__':
    s = Solution()
    print map(s.isHappy, xrange(10,17))