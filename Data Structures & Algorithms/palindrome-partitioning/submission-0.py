class Solution:
    def isPalin(self,s,l,r)->bool:
        while l<r:
            if s[l]!=s[r]:
                return False
            l,r=l+1,r-1    
        return True 
 
 
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        part = []

        def dfs(i):
            if i==len(s):
                ans.append(part.copy())
                return

            for j in range(i,len(s)):
                if self.isPalin(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)  
        return ans 

        


        