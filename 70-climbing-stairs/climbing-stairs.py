class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [1,2]
        if n <= 2:
            return ans[n-1]
        for i in range(2,n):
            total = ans[i-1] + ans[i-2]
            ans.append(total)
        return ans[n-1]