class Solution:
    def search(self, nums: List[int], target: int) -> int:
        answer=-1
        start=0
        end=len(nums)-1

        while end>=start:
            mid=(start+end)//2

            if target == nums[mid]:
                return mid

            if nums[mid]>=nums[start]:
                if nums[start] <= target and target < nums[mid]:
                    end=mid-1
                else:
                    start=mid+1
            else:
                if nums[mid] <target  and target <=nums[end]:
                    start=mid+1
                else:
                    end=mid-1
                    
        return answer

        