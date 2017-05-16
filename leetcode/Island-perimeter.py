class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        a=len(grid)
        b=len(grid[0])
        result=0
        for i in range(a):
            for j in range(b):
                if grid[i][j]==1:
                    result+=4
                    if i>0 and grid[i-1][j]==1:
                        result-=2
                    if j>0 and grid[i][j-1]==1:
                        result-=2
        return result
