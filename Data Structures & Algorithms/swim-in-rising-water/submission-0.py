class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        my_stack=[]
        my_stack.append((grid[0][0],0,0))
        heapq.heapify(my_stack)
        visit=set()

        while my_stack:
            t,x,y = heapq.heappop(my_stack)
            if x==len(grid)-1 and y==len(grid[0])-1:
                return t
            if (x,y) in visit:
                continue
            visit.add((x,y))
            neighbors = [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]
            for r,c in neighbors:
                if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
                    continue
                else:
                    heapq.heappush(my_stack,(max(t,grid[r][c]),r,c)) 
        return -1               


        