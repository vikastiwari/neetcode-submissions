class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x,y in points:
            distance = x**2 + y**2
            heapq.heappush(maxHeap,[-distance,x,y])

            if len(maxHeap)>k:
                heapq.heappop(maxHeap)

        ans = []
        while maxHeap:
            distance, x , y = heapq.heappop(maxHeap)
            ans.append([x,y])
        return ans    
        