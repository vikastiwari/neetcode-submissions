class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r,c):
            board[r][c]="T"
            neighbors = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]

            for (rn,cn) in neighbors:
                if rn<0 or cn<0 or rn>=ROWS or cn>=COLS:
                    continue
                if board[rn][cn] =="O":
                    dfs(rn,cn)    
        
        for c in range(COLS):
            if board[0][c]=="O":
                dfs(0,c)
            if board[ROWS-1][c]=="O":    
                dfs(ROWS-1,c)

        for r in range(ROWS):
            if board[r][0]=="O":
                dfs(r,0)
            if board[r][COLS-1]=="O":    
                dfs(r,COLS-1)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O":
                    board[r][c]="X"
                elif board[r][c]=="T":
                    board[r][c]="O"            
            



