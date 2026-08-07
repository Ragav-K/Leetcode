class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid[0][0] == 1)
            return 0;
        for(int row = 0; row < obstacleGrid.length; row++)
        {
            for(int col = 0; col < obstacleGrid[0].length; col++)
            {
                if(obstacleGrid[row][col] == 1)
                {
                    obstacleGrid[row][col] = -1;
                }
                if(row == 0 && col == 0)
                {
                    obstacleGrid[row][col] = 1;
                }
                else if(obstacleGrid[row][col] != -1 && (row == 0 || col == 0))
                {
                    if(row==0  && obstacleGrid[row][col-1] > 0)
                    {
                        obstacleGrid[row][col] = 1;
                    }
                    else if (col == 0 && obstacleGrid[row-1][col] > 0)
                    {
                        obstacleGrid[row][col] = 1;
                    }
                }
                else if(obstacleGrid[row][col] == 0)
                {
                    if(obstacleGrid[row-1][col] == -1 || obstacleGrid[row][col-1] == -1)
                    {
                        if (obstacleGrid[row-1][col] == -1 && obstacleGrid[row][col-1] == -1) 
                        {
                            obstacleGrid[row][col] = 0;
                        }
                        else if(obstacleGrid[row-1][col] == -1)
                        {
                            obstacleGrid[row][col] = obstacleGrid[row][col-1]; 
                        }
                        else if(obstacleGrid[row][col-1] == -1)
                        {
                            obstacleGrid[row][col] = obstacleGrid[row-1][col];
                        }
                    }
                    else
                    {
                        obstacleGrid[row][col] = obstacleGrid[row-1][col] + obstacleGrid[row][col-1];
                    }
                }
            }
        }
        if(obstacleGrid[obstacleGrid.length-1][obstacleGrid[0].length-1] == -1)
        {
            return 0;
        }
        else
        {
            return obstacleGrid[obstacleGrid.length-1][obstacleGrid[0].length-1];
        }
    }
}