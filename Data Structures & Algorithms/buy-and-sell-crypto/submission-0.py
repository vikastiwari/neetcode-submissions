class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer=0
        #max=0
        min=9999

        for price in prices:
            
            if price<min:
                min=price
    

            if answer < price-min:
                answer=price-min

        return answer    


        