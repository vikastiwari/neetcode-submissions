class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []

        char_map = {}

        for i,num in enumerate(nums):
            diff = target - num

            if diff in char_map:
                return [char_map.get(diff),i]

            char_map[num] = i
                 

    
        return []

        