class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        set_paci = set()
        set_atl=set()
        ROWS, COLS = len(heights), len(heights[0])
        answer=[]

        def dfs(r,c,set):
            set.add((r,c))
            neighbors = [(r+1,c),(r-1,c),(r,c-1),(r,c+1)]
            for rn,cn in neighbors:
                if rn>=ROWS or cn>=COLS or rn<0 or cn<0 or (rn,cn) in set:
                    continue

                if heights[r][c]<=heights[rn][cn]:
                    dfs(rn,cn,set)



        for r in range(ROWS):
            for c in range(COLS):
                if r==0 or c==0:
                    dfs(r,c,set_paci)

        for r in range(ROWS):
            for c in range(COLS):
                if r==ROWS-1 or c==COLS-1:
                    dfs(r,c,set_atl)
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in set_atl and (r,c) in set_paci:
                    answer.append([r,c]) 
        return answer                      
            
 
        