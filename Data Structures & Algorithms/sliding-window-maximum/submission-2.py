import heapq
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Edge case
        if not nums: return []
        
        output = []
        
        # We will store tuples in the heap: (-value, index)
        # We process the first 'k' elements first to build our initial window
        max_heap = []
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))
            
        # The max of the first window is at the top of the heap!
        # Remember to multiply by -1 to turn it back into a positive number
        output.append(-max_heap[0][0])
        
        # Now slide the window starting from index 'k'
        for i in range(k, len(nums)):
            
            # STEP 1: Add the new number entering the window into the heap
            heapq.heappush(max_heap,(-nums[i],i))

            
            # STEP 2: "Lazy Deletion"
            # We need to check the top of the heap. 
            # The top of the heap is accessed via max_heap[0]. 
            # The index of the top element is max_heap[0][1].
            # WHILE the index at the top of the heap is OUTSIDE our current window:
            #     Pop it off the heap!
            # (Hint: An index is outside the window if it is <= i - k)
            while max_heap[0][1] <= (i -k):
                heapq.heappop(max_heap)
            
            
            # STEP 3: The top of the heap is now guaranteed to be inside the window.
            # Append it to the output list! (Don't forget the -1 trick)
            
            output.append(-max_heap[0][0])
            
        return output
