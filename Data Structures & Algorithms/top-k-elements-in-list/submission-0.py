class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create hashmap of list
       
        freq = {}
        answer = []

        for num in nums:
          freq[num] = freq.get(num,0) + 1
    
        # sort according to count frequency
        sorted_values = sorted(freq.items(), key = lambda x: x[1], reverse=True )

        # get all keys
        return [list[0] for list in sorted_values[:k]] 