class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        set_paci = set()
        set_atl = set()
        ROWS, COLS = len(heights), len(heights[0])
        answer = []

        def dfs(r, c, visit_set):
            visit_set.add((r,c))
            neighbors = [(r+1,c), (r-1,c), (r,c-1), (r,c+1)]
            for rn, cn in neighbors:
                if rn >= ROWS or cn >= COLS or rn < 0 or cn < 0 or (rn,cn) in visit_set:
                    continue
                
                # Check the actual terrain heights!
                if heights[r][c] <= heights[rn][cn]:
                    dfs(rn, cn, visit_set)

        # Launch DFS from all Ocean borders
        for c in range(COLS):
            dfs(0, c, set_paci)
            dfs(ROWS - 1, c, set_atl)

        for r in range(ROWS):
            dfs(r, 0, set_paci)
            dfs(r, COLS - 1, set_atl)

        # Find the intersection
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in set_atl and (r,c) in set_paci:
                    answer.append([r,c]) 
                    
        return answer                      
