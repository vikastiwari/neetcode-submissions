class Solution:
    def isHappy(self, n: int) -> bool:
        answer=False
        set1=set()
        sum=0
        while n:
            sum+=(n%10)*(n%10)
            n=n//10

            if not n:
                if sum==1:
                    return True
                if sum in set1:
                    return False 
                else:
                    set1.add(sum)
                    n=sum
                    sum=0       



        return answer
        