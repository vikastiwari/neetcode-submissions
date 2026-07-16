class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>=2:
            top1 = heapq.heappop(stones)*-1
            top2 = heapq.heappop(stones)*-1

            print("fd",top1,top2)

            if top1==top2:
                continue
            else:
                heapq.heappush(stones,-abs(top1-top2)) 

        if len(stones)==0:
            return 0

        return stones[0]*-1    
        