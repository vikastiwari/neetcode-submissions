class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        start=1
        end=max(piles)
        answer=end

        while end>=start:
            mid = (start+end)//2
            time=0

            # calculate time
            for p in piles:
                time+=math.ceil(p/mid)

            if time<=h:
                answer=mid
                end=mid-1
            else:
                start=mid+1  

        return answer
        