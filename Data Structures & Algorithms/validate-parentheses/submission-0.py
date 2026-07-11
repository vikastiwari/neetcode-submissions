class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map closing brackets to their opening pairs
        closeToOpen = {')': '(', ']': '[', '}': '{'}
        
        for c in s:
            # Check if 'c' is a CLOSING bracket (is it a key in our dictionary?)
            if c in closeToOpen:
                
                # Make sure stack isn't empty, AND the top of stack matches the correct opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False # Instant failure if they don't match!
                    
            else:
                # If it's not a closing bracket, it MUST be an opening bracket. Push it!
                stack.append(c)
                
        # If the stack is empty at the end, it means everything was matched perfectly!
        return len(stack) == 0
