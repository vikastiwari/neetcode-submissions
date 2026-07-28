class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Step 1: Initialize prices array with infinity, set starting airport to 0
        prices = [float("inf")] * n
        prices[src] = 0

        # Step 2: Loop exactly K + 1 times (max number of flights allowed)
        for i in range(k + 1):
            
            # Create a copy so we don't accidentally chain multiple flights in one step!
            tmpPrices = prices.copy()

            # Step 3: Check every single flight in the entire list
            for source, dest, price in flights:
                
                # If we haven't even figured out how to reach the source yet, skip it
                if prices[source] == float("inf"):
                    continue

                # If taking this flight is cheaper than our current known price to reach dest
                if prices[source] + price < tmpPrices[dest]:
                    tmpPrices[dest] = prices[source] + price
            
            # Update our main array before the next loop
            prices = tmpPrices

        # Step 4: Return the result (or -1 if we couldn't reach it in K stops)
        if prices[dst] == float("inf"):
            return -1
            
        return prices[dst]
