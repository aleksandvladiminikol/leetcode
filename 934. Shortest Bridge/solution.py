from typing import List

grid = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]
]

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
                return
            grid[i][j] = 2
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        def bfs():
            queue = []
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        queue.append((i, j))
            step = 0
            while queue:
                size = len(queue)
                for _ in range(size):
                    i, j = queue.pop(0)
                    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 2:
                            continue
                        if grid[x][y] == 1:
                            return step
                        grid[x][y] = 2
                        queue.append((x, y))
                step += 1
        found = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
            if found:
                break
        return bfs()
    
print(Solution().shortestBridge(grid))
