class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def mul(n):
            if n <= 1:
                return n
            return mul(n-1) + mul(n-2)
        ans = mul(n)
        return ans