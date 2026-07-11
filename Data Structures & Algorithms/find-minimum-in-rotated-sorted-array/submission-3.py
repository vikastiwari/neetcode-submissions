class Solution:
    def findMin(self, nums: List[int]) -> int:
        answer=nums[0]
        start=0
        end= len(nums)-1

        while end>=start:

            if nums[start]<=nums[end]:
                answer = min (answer,nums[start])
                return answer

            mid=(end+start)//2

            answer = min(answer,nums[mid])

            if nums[mid]>=nums[start]:
                start=mid+1
            else:
                end=mid-1        

        return answer

        