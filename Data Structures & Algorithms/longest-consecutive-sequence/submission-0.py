class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer=0
        nums_set = set(nums)

        for num in nums:
            if num-1 in nums_set:
                continue
            else:
                count=1
                temp=num
                # count till consecutive numbers exists
                while num+1 in nums_set:
                    count+=1
                    num+=1

            if(count>answer):
                answer=count

        return answer
        