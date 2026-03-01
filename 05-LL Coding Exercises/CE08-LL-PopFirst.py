# Implement the pop_first method for the LinkedList class.
# The pop_first method should remove the first node (the head) from the linked list, update the head attribute and the length attribute accordingly, and return the removed node.
# Keep in mind the following requirements:

# The method should handle the cases where the list is empty and where the list has one or more nodes.
# The method should save a reference to the current head node before updating the head attribute.
# The method should update the head attribute to the second node in the list.
# The method should disconnect the removed node from the list by setting its next attribute to None.
# The method should update the length attribute of the LinkedList to reflect the removal of the node.
# If the list becomes empty after removing the node, the method should set the tail attribute of the LinkedList to None.
# The method should return the removed node, or None if the list is empty.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None 
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length==0:
            self.tail=None
        return temp

my_linked_list = LinkedList(2)
my_linked_list.append(1)

# (2) Items - Returns 2 Node
print(my_linked_list.pop_first().value)
# (1) Item -  Returns 1 Node
print(my_linked_list.pop_first().value)
# (0) Items - Returns None
print(my_linked_list.pop_first())