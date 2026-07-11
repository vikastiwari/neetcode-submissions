class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]

        for token in tokens:
            if token == "+":
                a2 = stack.pop()
                a1 = stack.pop()
                a3 = a1 + a2
                stack.append(a3) 

            elif  token == "-":
                a2 = stack.pop()
                a1 = stack.pop()
                a3 = a1 - a2
                stack.append(a3)  

            elif  token == "*":
                a2 = stack.pop()
                a1 = stack.pop()
                a3 = a1 * a2
                stack.append(a3)  

            elif  token == "/":
                a2 = stack.pop()
                a1 = stack.pop()
                a3 = int(a1 / a2)
                stack.append(a3)            

            else:
                stack.append(int(token))

        return stack[0]
