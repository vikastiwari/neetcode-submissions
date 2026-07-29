class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
            
        dp = {}

        # i is pointer for s1, j is pointer for s2
        def dfs(i, j):
            # Base Case: We successfully reached the end of both strings!
            if i == len(s1) and j == len(s2):
                return True
                
            if (i, j) in dp:
                return dp[(i, j)]
            
            # Try taking from s1
            if i < len(s1) and s1[i] == s3[i + j]:
                if dfs(i + 1, j):
                    dp[(i, j)] = True
                    return True
                    
            # Try taking from s2 (If s1 failed, or if s1 didn't match)
            if j < len(s2) and s2[j] == s3[i + j]:
                if dfs(i, j + 1):
                    dp[(i, j)] = True
                    return True
            
            # If neither path worked, it's a dead end.
            dp[(i, j)] = False
            return False

        return dfs(0, 0)
