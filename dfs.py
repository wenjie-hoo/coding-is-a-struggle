
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

def maxAreaOfIsland(grid):
    ans = 0
    n, m = len(grid), len(grid[0])
    
    def dfs(x: int, y: int):
        cur = 0
        if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
            cur += 1
            grid[x][y] = 0
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                cur += dfs(mx, my)
        return cur
        
    for i in range(n):
        for j in range(m):
            ans = max(dfs(i, j), ans)
    return ans

print(maxAreaOfIsland(grid))
