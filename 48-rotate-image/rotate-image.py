class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """ans = []
        while len(ans) != len(matrix):
            j = 0
            subans = []
            for i in range(len(matrix[0])-1,0,-1):
                subans.append(matrix[i][j])
            j += 1
            ans.append(subans)
        for i in range(len(matrix)):
            matrix[i] = ans[i]"""

        """seen = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (row,col) not in seen:
                    temp = matrix[row][col]
                    matrix[row][col] = matrix[col][len(matrix)-row-1]
                    matrix[col][len(matrix)-row-1] = temp
                    seen.add((row,col))
                    seen.add((col,len(matrix)-row-1))
        """

        """seen = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i,j) not in seen:

                    temp1 = matrix[i][j]
                    temp2 = matrix[j][len(matrix)-i-1]
                    temp3 = matrix[len(matrix)-i-1][len(matrix)-j-1]
                    temp4 = matrix[len(matrix)-j-1][i]

                    matrix[len(matrix)-j-1][i] = temp3
                    matrix[len(matrix)-i-1][len(matrix)-j-1] = temp2
                    matrix[j][len(matrix)-i-1] = temp1
                    matrix[i][j] = temp4

                    seen.add((i,j))
                    seen.add((j,len(matrix)-i-1))
                    seen.add((len(matrix)-i-1,len(matrix)-j-1))
                    seen.add((len(matrix)-j-1,i))
        """

        for i in range(len(matrix)//2):
            for j in range((len(matrix[0])+1)//2):

                temp1 = matrix[i][j]
                temp2 = matrix[j][len(matrix)-i-1]
                temp3 = matrix[len(matrix)-i-1][len(matrix)-j-1]
                temp4 = matrix[len(matrix)-j-1][i]

                matrix[len(matrix)-j-1][i] = temp3
                matrix[len(matrix)-i-1][len(matrix)-j-1] = temp2
                matrix[j][len(matrix)-i-1] = temp1
                matrix[i][j] = temp4