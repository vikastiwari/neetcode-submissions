class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Recursive helper function
        def helper(x, n):
            # Base Cases
            if x == 0: return 0
            if n == 0: return 1
            
            # The Divide and Conquer step
            res = helper(x, n // 2)
            res = res * res # Square the result to cut the work in half
            
            # If n is even, return the squared result
            # If n is odd, we need to multiply by x one more time
            if n % 2 == 1:
                return res * x
            else:
                return res

        # Handle negative powers (e.g., 2^-3 is just (1/2)^3)
        res = helper(x, abs(n))
        if n >= 0:
            return res
        else:
            return 1 / res
