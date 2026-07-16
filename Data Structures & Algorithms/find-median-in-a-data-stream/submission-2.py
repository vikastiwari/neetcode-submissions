class MedianFinder:
    def __init__(self):
        self.small_heap = []
        self.big_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_heap, -num)
        pop = heapq.heappop(self.small_heap) * -1
        heapq.heappush(self.big_heap, pop)

        if len(self.big_heap) > len(self.small_heap):
            pop = heapq.heappop(self.big_heap)
            heapq.heappush(self.small_heap, -pop)

    def findMedian(self) -> float:
        if len(self.small_heap) == len(self.big_heap):
            return (self.small_heap[0] * -1 + self.big_heap[0]) / 2.0
        else:
            return self.small_heap[0] * -1
