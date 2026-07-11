class Solution:
    def search(self, nums: List[int], target: int) -> int:
        answer=-1

        start=0
        end=len(nums)-1
        
        while end>=start:
            mid=(end+start)//2

            if nums[mid]>target:
                end=mid-1
            elif nums[mid]<target:
                start=mid+1
            else:
                return mid

        return answer
        