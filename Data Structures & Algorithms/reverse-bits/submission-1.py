class Solution:
    def reverseBits(self, n: int) -> int:
        answer=0
        for i in range(0,32):
            bit = n>>i & 1

            if bit:
                answer |= 1<<(31-i)
        return answer        
        
        