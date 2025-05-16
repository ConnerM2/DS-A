# Linked lists are a list like data structure where each node points to the next node
# There are no indexes, just a head, nodes, and tails
# Instead of being right next to each other in memory, like a list, they are spread out
# Nodes are essentially a dictionary
#      {"value": 10, "next": None}


# Creating a linked list
class Node:
    # Creates nodes
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        # Uses the Node class to create new node with "value"
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_linked_list = LinkedList(4)
my_linked_list.append(3)
my_linked_list.print_list()
