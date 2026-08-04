class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        l = 0
        r = 1
        ans = ""
        subans = s[l]
        while r < len(s):
            if s[r] in subans:
                if len(subans) > len(ans):
                    ans = subans
                l += 1
                subans = s[l]
                r = l+1
            else:
                subans += s[r]
                r += 1
        if len(subans) > len(ans):
            ans = subans
        return len(ans)