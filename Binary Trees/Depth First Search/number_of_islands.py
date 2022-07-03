"""
    PROMPT:
            Given an m x n 2-D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

            An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
            You may assume all four edges of the grid are all surrounded by water.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def depth_search(m, n):
            if (n >= len(grid[0])) or (m >= len(grid)) or (n < 0) or (m < 0) or grid[m][n] == "0":
                return
            
            # Change the land to see to reduce repetition
            grid[m][n] = "0"
            
            # Check all 4 adjacent cells
            for m, n in ((m-1, n), (m+1, n), (m, n-1), (m, n+1)):
                depth_search(m, n)
            
  
        island_count = 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == "1":
                    # Since any land touched is turned to sea, there's no chance to accidentally recount islands
                    depth_search(m, n)
                    island_count += 1
        
        return island_count