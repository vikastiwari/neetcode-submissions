class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create hashmap of list
       
        freq = {}
        answer = []
        buckets = [ [] for i in range(len(nums)+1)]

        for num in nums:
          freq[num] = freq.get(num,0) + 1
    
        # sort according to count frequency
        #sorted_values = sorted(freq.items(), key = lambda x: x[1], reverse=True )

        ## trying O(n) solution 
        for key,value in freq.items():
            buckets[value].append(key)

        # Loop the buckets from index len(nums) to decreasing order till K is zero
        for i in range (len(nums),-1,-1):
            if  buckets[i]:
                answer.extend(buckets[i])  
                if len(answer)==k:
                    return answer




        return answer

        # get all keys
        #return [list[0] for list in sorted_values[:k]] 