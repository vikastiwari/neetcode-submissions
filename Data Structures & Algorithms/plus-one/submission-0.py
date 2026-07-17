class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer=[]
        num=0


        for d in digits:
            num = 10*num + d

        num+=1

        while num:
            answer.append(num%10)
            num=num//10

        return answer[::-1]