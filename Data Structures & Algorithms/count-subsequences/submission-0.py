class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def dfs(i, j):
            # Base Case 1: We successfully found all characters of t!
            if j == len(t):
                return 1
            # Base Case 2: We ran out of characters in s, but haven't finished t.
            if i == len(s):
                return 0
                
            if (i, j) in dp:
                return dp[(i, j)]

            # If the characters match, we have TWO choices (Take OR Leave)
            if s[i] == t[j]:
                take = dfs(i + 1, j + 1)
                leave = dfs(i + 1, j)
                dp[(i, j)] = take + leave
                
            # If they don't match, we have ONE choice (Must Leave)
            else:
                leave = dfs(i + 1, j)
                dp[(i, j)] = leave
                
            return dp[(i, j)]

        return dfs(0, 0)
