class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        result = 1

        for i in range(1, 2 * k + 1):
            result = result * (n + k - i) % MOD
            result = result * pow(i, MOD - 2, MOD) % MOD

        return result