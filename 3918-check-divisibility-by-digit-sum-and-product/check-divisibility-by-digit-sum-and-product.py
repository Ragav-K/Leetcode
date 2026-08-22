class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = 0
        p = 1
        x = n

        while x:
            d = x % 10
            s += d
            p *= d
            x //= 10

        return n % (s+p) == 0 