class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        answer=0

        for num in nums:
            print("a",abs(num),nums[abs(num)])
            nums[abs(num)] = -1*nums[abs(num)]
            print("b",abs(num),nums[abs(num)])
            if nums[abs(num)]>0:
                print("if",abs(num),nums[abs(num)])
                return abs(num)

        return answer
        