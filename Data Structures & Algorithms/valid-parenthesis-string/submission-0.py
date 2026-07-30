class Solution:
    def checkValidString(self, s: str) -> bool:
        # Our range of possible open parentheses counts
        leftMin = 0
        leftMax = 0
        
        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
            else: # c == "*"
                # We could treat '*' as ')' which decreases our minimum possible open parentheses
                leftMin -= 1
                # We could treat '*' as '(' which increases our maximum possible open parentheses
                leftMax += 1
                
            # 1. The Death Check
            # Even if we turned every single '*' into a '(', we STILL have a negative count.
            # We have too many ')' and it is impossible to recover.
            if leftMax < 0:
                return False
                
            # 2. The Adjustment Check
            # If treating '*' as ')' caused our count to go negative, we just cancel that choice.
            # We decide to treat those '*' as empty strings "" instead, pulling our min back up to 0.
            if leftMin < 0:
                leftMin = 0
                
        # At the very end, if 0 is a mathematically valid possibility in our range, 
        # it means there is a combination that perfectly balances the parentheses!
        return leftMin == 0
