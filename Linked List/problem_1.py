class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertMiddle(self, data):
        current = self.head
        if current == None:
            return (f"There is no item")
        elif (current.next == None):
            return (f"there is only one item")
        elif current.next.next:
            slow = self.head
            fast = self.head
            
            while fast != None:
                slow = slow.next
                fast = fast.next.next
                middle = slow
            return middle
        
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    # Function to insert a new node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Function to display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Function to insert a node in the middle of the linked list
    def insert_in_middle(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        # Step 1: Find the middle of the linked list
        slow = self.head
        fast = self.head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        # Step 2: Insert the new node in the middle
        if prev:  # when list has more than 1 element
            prev.next = new_node
            new_node.next = slow
        else:  # when list has only 1 element
            new_node.next = self.head
            self.head = new_node

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(4)
ll.append(5)

print("Original Linked List:")
ll.display()

ll.insert_in_middle(3)
print("Linked List after inserting in the middle:")
ll.display()