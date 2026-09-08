class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1000:
            return 0
        c = int(n/100)
        return (c-1)*1000 + n-(c*1000)+1