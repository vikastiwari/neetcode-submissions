class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counter = collections.Counter(tasks)
        maxHeap = [-c for c in counter.values()]

        heapq.heapify(maxHeap)
        queue = collections.deque()

        time=0

        while maxHeap or queue :
            time+=1

            if maxHeap:
                freq=heapq.heappop(maxHeap)
                freq+=1
                if freq<0:
                    queue.append([freq,time+n])

            if queue:
                freq,complete_time = queue[0]
                if(complete_time==time):
                    queue.popleft()
                    heapq.heappush(maxHeap,freq)

        return time            



        