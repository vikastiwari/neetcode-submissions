class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        sub=[]


        def dfs(open,close):
            if close==n and open==n :


                ans.append("".join(sub)) 
                return 

            if open<n:
                sub.append("(")
                dfs(open+1,close)
                sub.pop()
            if close<n and close<open:
                sub.append(")")
                dfs(open,close+1)
                sub.pop()    



        dfs(0,0)
        return ans    
        