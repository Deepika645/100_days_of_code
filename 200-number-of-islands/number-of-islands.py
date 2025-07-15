from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def bfs(row, col):
            q = deque()
            q.append((row, col))
            visited.add((row, col))
            while q:
                m,n = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr,dc in directions:
                    r = m + dr
                    c = n + dc
                    if (r in range(rlen) and c in range(clen) and grid[r][c] == '1' and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))

        rlen = len(grid)
        clen = len(grid[0])
        visited = set()
        islands = 0
        
        for i in range(rlen):
            for j in range(clen):
                if grid[i][j] == '1' and (i,j) not in visited:
                    bfs(i,j)
                    islands += 1
        return islands
        


        