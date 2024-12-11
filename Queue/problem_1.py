class QueueWithStacks:
    def __init__(self):
        self.stack1 = []  # Stack to handle enqueue operations
        self.stack2 = []  # Stack to handle dequeue operations

    # Enqueue operation: Push data onto stack1
    def enqueue(self, data):
        self.stack1.append(data)

    # Dequeue operation: Pop from stack2 (or transfer elements from stack1 to stack2 if stack2 is empty)
    def dequeue(self):
        # If both stacks are empty, the queue is empty
        if not self.stack1 and not self.stack2:
            return "Queue is empty"
        
        # If stack2 is empty, move elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # Pop the top element from stack2, which is the front of the queue
        return self.stack2.pop()

    # Peek operation: Return the front of the queue without removing it
    def peek(self):
        if not self.stack1 and not self.stack2:
            return "Queue is empty"
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2[-1]  # Peek the top of stack2

    # Check if the queue is empty
    def is_empty(self):
        return not self.stack1 and not self.stack2

# Example usage
queue = QueueWithStacks()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2

queue.enqueue(4)

print(queue.dequeue())  # Output: 3
print(queue.peek())     # Output: 4
print(queue.dequeue())  # Output: 4
print(queue.is_empty()) # Output: True
