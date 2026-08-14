class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        max_len = 0
        fre = {}
        
        for r in range(len(s)):
            fre[s[r]] = fre.get(s[r], 0) + 1
            
            while fre[s[r]] > 2:
                fre[s[l]] -= 1
                l += 1
                
            max_len = max(max_len, r - l + 1)
            
        return max_len