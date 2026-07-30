class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost) or len(gas)!=len(cost):
            return -1
        else:
            index=0
            total_sum=0
            for i in range(len(gas)):
                total_sum += gas[i]-cost[i]
                if total_sum<0:
                    index=i+1
                    total_sum=0 
        return index
        