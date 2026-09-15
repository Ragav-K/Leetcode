class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)

        # dp[i] = maximum number of non-overlapping
        # palindromic substrings of length at least k
        dp = [0] * (n + 1)

        # pal[i][j] indicates whether s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]

            if i >= k:
                for j in range(i - k + 1):
                    if pal[j][i - 1]:
                        dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]