class MedianFinder:

    def __init__(self):
        self.small_heap=[]
        self.big_heap=[]
        self.size=0

        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_heap,-num)
        self.size+=1

        if self.big_heap and (self.small_heap[0]*-1 >self.big_heap[0]):
            pop1 = heapq.heappop(self.small_heap)
            pop2 = heapq.heappop(self.big_heap)
            heapq.heappush(self.small_heap,-pop2)
            heapq.heappush(self.big_heap,-pop1)

        if self.size%2==0:
            if len(self.small_heap)>len(self.big_heap):
                pop=heapq.heappop(self.small_heap)
                heapq.heappush(self.big_heap,-pop)
       

    def findMedian(self) -> float:
        if self.size%2==0:
            return (self.small_heap[0]*-1 + self.big_heap[0])/2
        else:
            return self.small_heap[0]*-1


        
        