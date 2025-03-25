# Linked lists are a list like data structure where each node points to the next node
# There are no indexes, just a head, nodes, and tails
# Instead of being right next to each other in memory, like a list, they are spread out
# Nodes are essentially a dictionary
#      {"value": 10, "next": None}

# This isn't a linked list, but you can think of it like a linked list
head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }
}
print(head["next"]["next"]["value"])

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

my_linked_list = LinkedList(4)
print(my_linked_list.head.value)
