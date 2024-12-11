class MaxStack:
    def __init__(self):
        self.stack = []  # Primary stack to hold the elements
        self.max_stack = []  # Stack to keep track of max values

    def push(self, data):
        self.stack.append(data)
        # If max_stack is empty or the new data is greater than or equal to the top of max_stack, push it to max_stack
        if not self.max_stack or data >= self.max_stack[-1]:
            self.max_stack.append(data)

    def pop(self):
        if self.stack:
            popped = self.stack.pop()
            # If the popped element is the current maximum, pop it from max_stack as well
            if popped == self.max_stack[-1]:
                self.max_stack.pop()
            return popped
        return None  # Stack is empty

    def get_max(self):
        if not self.max_stack:
            return None  # Return None if stack is empty
        return self.max_stack[-1]  # Return the top of the max_stack (the maximum)

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

# Example usage
stack = MaxStack()

stack.push(5)
stack.push(1)
stack.push(3)
stack.push(10)
stack.push(7)

print("Current max:", stack.get_max())  # Output: 10
stack.pop()  # Popping 7
print("Current max:", stack.get_max())  # Output: 10
stack.pop()  # Popping 10
print("Current max:", stack.get_max())  # Output: 5
