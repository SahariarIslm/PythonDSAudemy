# LL: Get
# Implement the get method for the LinkedList class.
# The get method should take an integer index as a parameter and return a pointer to the node at the specified index in the linked list.
# If the index is out of bounds (less than 0 or greater than or equal to the length of the list), the method should return None.
# Keep in mind the following requirements:

# The method should handle the cases where the index is out of bounds.
# The method should start at the head of the list and traverse the list using the next attribute of the nodes.
# The method should stop traversing the list when it reaches the specified index and return the node at that position.
# If the index is out of bounds, the method should return None.

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
        if self.length == 0:
            self.tail = None
        return temp

    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp=temp.next
        return temp

my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
print(my_linked_list.get(3).value)