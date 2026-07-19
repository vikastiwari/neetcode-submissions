class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        dist=0
        ROWS, COLS = len(grid), len(grid[0])
        len_zero=0


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c]==0:
                    len_zero+=1


        if len(queue)==ROWS*COLS or len_zero + len(queue)==ROWS*COLS  :
            return 0  
     

        while queue:
            length = len(queue)
            print("len",length)

            for l in range(length):
                r,c = queue.popleft()
                grid[r][c]=2

                neighbors = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]

                for nr, nc in neighbors:
                    if nr>=ROWS or nc>=COLS or nr<0 or nc<0 or grid[nr][nc]!=1:
                        continue

                    queue.append((nr,nc))
                    grid[nr][nc]=2

            dist+=1    

        for r in range(ROWS):
            for c in range(COLS) :
                if grid[r][c]==1:
                    return -1
        return dist-1            