class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()
        board = [["."]*n  for i in range (n)]
        ans=[]


        def dfs(r):
            if r == n:
                ans.append(["".join(row)  for row in board])
                return

            for c in range(n):
                if c in col or (r-c) in negDiag or (r+c) in posDiag:
                    continue

                board[r][c]="Q"
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                dfs(r+1)
                board[r][c]="."
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)

        dfs(0)
        return ans
        