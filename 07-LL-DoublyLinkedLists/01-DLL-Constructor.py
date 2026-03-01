class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)           # Create a new node object from the Node class
        
        self.head = new_node             # Assign the new node to the head pointer
        self.tail = new_node             # Assign the new node to the tail pointer
        self.length = 1                  # Initialize the doubly linked list length to 1

    def print_list(self):
        cur = self.head                  # assigning head node to the current pointer
        while cur:                       # run the loop untill current node is not None
            print(cur.value)             # printing curent node value
            cur = cur.next               # moving current to next node

    def append(self,value):
        new_node = Node(value)           # Create a new node object from the Node class

        if self.head is None:            # if head is empty
            self.head = new_node         # Assign the new node to the head pointer
            self.tail = new_node         # Assign the new node to the tail pointer
            self.length = 1              # Initialize the doubly linked list length to 1
        else:                            # if head is not empty
            self.tail.next = new_node    # Assign the new node to the next pointer of the DLL
            new_node.prev = self.tail    # Assign the previous pointer of the new node to the current tail node
            self.tail = new_node         # Move/change the tail pointer to the new_node
            self.length += 1             # Increase the dll leanght by one
        return True
    
    def pop(self):
        if self.head is None:
            return None
        last = self.tail                 # set 'last' pointer on tail 
        if self.length == 1:             # check if new node length is 1
            self.head = None             # point the head pointer to None
            self.tail = None             # point the tail pointer to None
        else:
            self.tail = self.tail.prev   # pull the tail pointer from the last node
            self.tail.next = None        # unlink the next pointer from the last node
            last.prev = None             # unlink the prev pointer of the last node 
            self.length -= 1             # decrement the length of the node
        return last.value
    
    def prepend(self,value):
        new_node = Node(value)           # create a new node object from Node Class

        if self.head is None:            # if head is empty
            self.head = new_node         # Assign the new node to the head pointer
            self.tail = new_node         # Assign the new node to the tail pointer
        else:
            new_node.next = self.head    # Assign next pointer of the new node to the head node
            self.head.prev = new_node    # Assign prev pointer of the head node to the new node 
            self.head = new_node         # shift the head node pointer to the new node 
            self.length +=1              # Increase the dll leanght by 1
        return True
    
    # def pop_first(self):
    #     if self.head is None:
    #         return None
    #     if self.length == 1:             # check if new node length is 1
    #         self.head = None             # point the head pointer to None
    #         self.tail = None             # point the tail pointer to None
    #     else:
    #         next = self.head.next        # set next pointer to the second node
    #         next.prev = None             # set prev pointer of the next node to none 
    #         self.head.next = None        # set next pointer of the head node to none 
    #         self.head = next             # set head pointer of the dll to next 
        
    #     self.length -= 1                 # decrement the length of the node
    #     return True

    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head                 # set temp pointer to the head node
        if self.length == 1:             # check if new node length is 1
            self.head = None             # point the head pointer to None
            self.tail = None             # point the tail pointer to None
        else:
            self.head = self.head.next   # set head pointer of the dll to next 
            self.head.prev = None        # set prev pointer of the head node to none 
            temp.next = None             # set next pointer of the temp node to none 
        self.length -= 1                 # decrement the length of the node
        return temp


        
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.print_list()
print("break")
my_doubly_linked_list.prepend(10)
my_doubly_linked_list.print_list()
print("break")
print(my_doubly_linked_list.pop_first())
# print(my_doubly_linked_list.pop_first())
# print(my_doubly_linked_list.pop_first())
my_doubly_linked_list.print_list()
# print(my_doubly_linked_list.pop())
# print(my_doubly_linked_list.pop())
# print(my_doubly_linked_list.pop())

