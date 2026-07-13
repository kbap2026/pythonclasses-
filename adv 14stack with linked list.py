# Python program to
# demonstrate stack implementation
# using list

# The functions associated with stack are:
#
# empty() – Returns whether the stack is empty – Time Complexity: O(1)
# size() – Returns the size of the stack – Time Complexity: O(1)
# top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
# push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
# pop() – Deletes the topmost element of the stack – Time Complexity: O(1)
# Implementation:
# There are various ways from which a stack can be implemented in Python. This article covers the implementation of a stack using data structures and modules from the Python library.
# Stack in Python can be implemented using the following ways:


# stack = []
#
# # append() function to push
# # element in the stack
# stack.append('a')
# stack.append('b')
# stack.append('c')
#
# print('Initial stack')
# print(stack)
#
# # pop() function to pop
# # element from stack in
# # LIFO order
# print('\nElements popped from stack:')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
#
# print('\nStack after elements are popped:')
# print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty

# Python program to demonstrate
# stack implementation using a linked list.
#node class

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class Stack:

	# Initializing a stack.
	# Use a dummy node, which is
	# easier for handling edge cases.
	def __init__(self):
		self.head = Node("head")
		self.size = 0

	# String representation of the stack
	def __str__(self):
		cur = self.head.next
		out = ""
		while cur:
			out += str(cur.value) + "->"
			cur = cur.next
		return out[:-2]

	# Get the current size of the stack
	def getSize(self):
		return self.size

	# Check if the stack is empty
	def isEmpty(self):
		return self.size == 0

	# Get the top item of the stack
	def peek(self):

		# Sanitary check to see if we
		# are peeking an empty stack.
		if self.isEmpty():
			raise Exception("Peeking from an empty stack")
		return self.head.next.value

	# Push a value into the stack.
	def push(self, value):
		node = Node(value)
		node.next = self.head.next
		self.head.next = node
		self.size += 1

	# Remove a value from the stack and return.
	def pop(self):
		if self.isEmpty():
			raise Exception("Popping from an empty stack")
		remove = self.head.next
		self.head.next = self.head.next.next
		self.size -= 1
		return remove.value


# Driver Code
if __name__ == "__main__":
	stack = Stack()
	for i in range(1, 11):
		stack.push(i)
	print(f"Stack: {stack}")

	for _ in range(1, 6):
		remove = stack.pop()
		print(f"Pop: {remove}")
	print(f"Stack: {stack}")
