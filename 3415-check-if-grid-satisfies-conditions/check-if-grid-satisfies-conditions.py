class Solution(object):
    def satisfiesConditions(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])

        for row in range(m):
            for col in range(n):
                if row + 1 < m and grid[row][col] != grid[row+1][col]:
                    return False
                if col + 1 < n and grid[row][col] == grid[row][col+1]:
                    return False
        return True