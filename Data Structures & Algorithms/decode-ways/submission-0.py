class Solution:
    def numDecodings(self, s: str) -> int:
        answer=0
        dp=collections.defaultdict(int)
        def dfs(i):
            if i==len(s):
                return 1
            if i+1>len(s):
                return 0    
            if s[i]=="0":
                return 0
            if i in dp:
                return dp[i]
            ways = dfs(i+1)   
            if i+1 < len(s) and "10" <=s[i:i+2]<="26":
                ways+=dfs(i+2) 
            dp[i]=ways
            return ways    
        return dfs(0)    


        