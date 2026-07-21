import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. Build Adjacency List
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
            
        # 2. Setup Min-Heap and Visited Set
        minHeap = [(0, k)] # (time, node)
        visit = set()
        t = 0 # This will hold our final answer!
        
        # 3. Dijkstra's Algorithm
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            
            # Did we already find a faster path to this node? Skip it!
            if n1 in visit:
                continue
                
            # It's a new node! Add to visit set.
            visit.add(n1)
            
            # Update our master time! 
            # Because of the heap, this naturally grabs the largest time at the very end!
            t = w1
            
            # ACTION REQUIRED: 
            # Loop through all neighbors of n1 in the edges map
            # If the neighbor is not in visit:
            #   Push (current_time + neighbor_time, neighbor) to the heap
            for n2,w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap,(w1+w2,n2))
            
        # 4. Final Check
        # If we visited every single node, return t. Otherwise, return -1.
        if len(visit) == n:
            return t
        else:
            return -1
