class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        
        # 1. Add ALL treasures (0) to the queue to start our Multi-Source ripples!
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    
        # A variable to track how many "steps" our ripples have traveled
        dist = 0
        
        # 2. Start the BFS!
        while q:
            # How many coordinates are currently in the queue for this 'ripple' level?
            length = len(q)
            
            # Process all coordinates for the current distance
            for i in range(length):
                r, c = q.popleft()
                
                # Write the shortest distance to this cell!
                grid[r][c] = dist
                
                # Define the 4 neighbors
                neighbors = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
                for nr, nc in neighbors:
                    # If neighbor is out of bounds, or a wall (-1), or ALREADY VISITED... skip it!
                    # Hint: We know it's not visited if its value is still the massive INF number (2147483647)
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 2147483647):
                        continue
                        
                    # This land is valid and unvisited! Add it to the queue for the NEXT ripple level!
                    q.append((nr, nc))
                    
                    # Mark it as 'visited' immediately so other ripples don't add it to the queue too!
                    grid[nr][nc] = dist + 1 
            
            # Increase the distance for the next ripple level!
            dist += 1
