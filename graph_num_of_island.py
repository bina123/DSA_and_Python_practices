def numIslands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0
    
    def dfs(r,c):
        if (r,c) in visited:
            return
        
        visited.add((r,c))
        
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr, nc = r + dr , c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == '1' and (nr, nc) not in visited:
                    dfs(nr,nc)
                    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r,c) not in visited:
                dfs(r,c)
                islands += 1
                
    return islands
                
                
grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]

print(numIslands(grid))