class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        
        last = [0] * 26
        
        for i in range(1, len(s) + 1):
            ch = ord(s[i - 1]) - ord('a')
            
            dp[i] = (2 * dp[i - 1] - last[ch]) % MOD
            
            last[ch] = dp[i - 1]
        
        return (dp[len(s)] - 1) % MOD