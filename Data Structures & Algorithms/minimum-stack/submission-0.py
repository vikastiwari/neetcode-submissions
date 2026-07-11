class MinStack:

    def __init__(self):
        # Initialize your two parallel stacks here
        self.stack=[]
        self.minStack=[]
        pass

    def push(self, val: int) -> None:
        # 1. Push 'val' to your main stack
        # 2. Figure out the current minimum. 
        #    (Is it 'val'? Or is it the top of the minStack?)
        #    Hint: use the built-in min() function! 
        #    Be careful: what if minStack is empty?
        # 3. Push that minimum to your minStack

        self.stack.append(val)

        if self.minStack and (self.minStack[-1]<val):
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)    
        

    def pop(self) -> None:
        # Pop from BOTH stacks
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        # Return the top of the main stack
        return self.stack[-1]
        

    def getMin(self) -> int:
        # The absolute minimum of the stack at any given moment
        # is ALWAYS sitting right at the top of your minStack!
        # Return the top of the minStack
        return self.minStack[-1]
        
