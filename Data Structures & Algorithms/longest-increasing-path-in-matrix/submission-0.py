class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = collections.defaultdict(int)
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]

            max_path = 1    
            neighbors = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            for r,c in neighbors:
                if r<0 or c<0 or r>=len(matrix) or c>=len(matrix[0]):
                    continue
                if matrix[r][c]<=matrix[i][j]:
                    continue    
                max_path = max(max_path, 1+ dfs(r,c)) 
            dp[(i,j)] = max_path     
            return dp[(i,j)]

        our_sum=0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                our_sum=max(our_sum,dfs(r,c))
        return our_sum