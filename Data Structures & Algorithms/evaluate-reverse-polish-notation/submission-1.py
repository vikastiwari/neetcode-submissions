class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        # 1. Map the string operators to their exact math functions
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        for token in tokens:
            if token in operations:
                # 2. Pop the numbers ONCE
                a2 = stack.pop()
                a1 = stack.pop()
                
                # 3. Call the correct math function from the dictionary!
                result = operations[token](a1, a2)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]
