def floodFill(image, sr, sc, newColor):
    """
    Flood fill algorithm - change connected pixels of same color
    
    Args:
    image: 2D grid of pixel colors
    sr, sc: starting row and column
    newColor: the new color to fill with
    
    Returns: modified image
    
    Approach:
    1. Get original color at (sr, sc)
    2. If original == newColor, return (no change needed)
    3. DFS from (sr, sc) to change all connected pixels of original color
    """
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]
    
    if original_color == newColor:
        return image
    
    def dfs(r,c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        if image[r][c] != original_color:
            return
        
        image[r][c] = newColor
        
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)
                
    dfs(sr,sc)
    return image

# Test case:
image = [[1,1,1],[1,1,0],[1,0,1]]
print(floodFill(image, 1, 1, 2))
# Output: [[2,2,2],[2,2,0],[2,0,1]]