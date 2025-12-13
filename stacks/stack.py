class Stack:
    def _init_(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def is_empty(self):
        return len(self.stack) == 0
    
    def pop(self):
        if self.is_empty():
            return "Stack is emptyy"
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
mystack = Stack()
mystack.push(34)
mystack.push(199)
mystack.push(32)

print(f" Original Stack {mystack.stack}")
print(f"Popped element {mystack.pop()}")
print(f"Stack after pop {mystack.stack}")
print(f"Accessed Element {mystack.peek()}")
print(f"Size of stack {mystack.size()}")