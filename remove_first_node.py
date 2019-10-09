# Python3 program to remove first node of 
# linked list. 
import sys 

# Link list node 
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

# Function to remove the first node 
# of the linked list 
def removeFirstNode(head): 
	if not head: 
		return None
	temp = head 

	# Move the head pointer to the next node 
	head = head.next
	temp = None
	return head 

# Function to push node at head 
def push(head, data): 
	if not head: 
		return Node(data) 
	temp = Node(data) 
	temp.next = head 
	head = temp 
	return head 

# Driver code 
if __name__=='__main__': 

	# Start with the empty list 
	head = None

	# Use push() function to construct 
	# the below list 8 -> 23 -> 11 -> 29 -> 12 
	head = push(head, 12) 
	head = push(head, 29) 
	head = push(head, 11) 
	head = push(head, 23) 
	head = push(head, 8) 

	head = removeFirstNode(head) 
	
	while(head): 
		print("{} ".format(head.data), end ="") 
		head = head.next

 
