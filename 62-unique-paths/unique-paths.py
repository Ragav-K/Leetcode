class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans = [[0]*n for k in range(m)]
        for i in range(n):
            ans[0][i] = 1
        for j in range(m):
            ans[j][0] = 1

        for row in range(1,m):
            for col in range(1,n):
                ans[row][col] = ans[row-1][col] + ans[row][col-1]
        return ans[-1][-1]