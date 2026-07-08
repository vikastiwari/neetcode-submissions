class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        answer = []

        pre=1
        for i in range(0,len(nums)):
            prefix[i]=pre
            pre=pre*nums[i]
        #print(prefix)

        sux=1
        for i in range(len(nums)-1,-1,-1):
            suffix[i]=sux
            sux=sux*nums[i]
        #print(suffix)

        for i in range(0,len(nums)):
            answer.append(prefix[i]*suffix[i])

        return answer    


