#class Stack:
from stack import Stack


def __init__(self):
        self.stack = []

def is_empty(self):
    return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def size(self):
        return len(self.stack)


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)


# Example usage:

# Creating a stack and performing operations
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # Output: 3
print(stack.peek())  # Output: 2
#print(stack.size())  # Output: 2

# Creating a queue and performing operations
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1
print(queue.size())  # Output: 2
