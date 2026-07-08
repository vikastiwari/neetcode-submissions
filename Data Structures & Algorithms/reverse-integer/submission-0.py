class Solution:
    def reverse(self, x: int) -> int:
        MAX = (2**31) -1
        sign=1
        if x<0:
            sign=-1
            x = abs(x)

        answer=0

        while x:
            digit = x%10
            x=x//10  
            answer= (answer*10) + digit  
            if answer>MAX:
                return 0

        return answer*sign         