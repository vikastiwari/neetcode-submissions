class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp={}
        def dfs(i,j):
            if j==len(p):
                return i==len(s)
            if (i,j) in dp:
                return dp[(i,j)]

            match = i<len(s) and(s[i]==p[j] or p[j]=='.')
            
            if j+1<len(p) and p[j+1]=='*':
                #1. Leave it
                skip_star = dfs(i,j+2)
                #2. Take it
                use_star = match and dfs(i+1,j)
                dp[(i,j)] = skip_star or use_star
                return dp[(i,j)]
            else:
                if match:
                    dp[(i,j)] = dfs(i+1,j+1)
                    return dp[(i,j)]
                else:
                    return False    
        return dfs(0,0)    
        