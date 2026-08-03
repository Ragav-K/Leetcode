class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        top = 0
        down = len(matrix)-1
        left = 0
        right = len(matrix[0])-1

        ans = []

        while top <= down and left <= right:
            for col in range(left,right+1):
                ans.append(matrix[top][col])
            top += 1
            for row in range(top,down+1):
                ans.append(matrix[row][right])
            right -= 1
            if top <= down:
                for col in range(right,left-1,-1):
                    ans.append(matrix[down][col])
                down -= 1
            if left <= right:
                for row in range(down,top-1,-1):
                    ans.append(matrix[row][left])
                left += 1
        return ans