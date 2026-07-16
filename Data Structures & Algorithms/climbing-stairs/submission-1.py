class Solution:
    def climbStairs(self, n: int) -> int:
        if n in [1,2,3]:
            return n
        ans=0 
        a=2
        b=3    
        
        count=3
        while count<n:
            ans = a+b
            a=b
            b=ans
            count+=1
        return ans    

        