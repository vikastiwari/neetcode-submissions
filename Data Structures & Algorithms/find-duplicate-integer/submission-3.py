class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            nums[abs(num)] = -1*nums[abs(num)]
            if nums[abs(num)]>0:
                return abs(num)

        