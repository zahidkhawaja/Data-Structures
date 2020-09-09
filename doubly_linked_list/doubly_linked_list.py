"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev = None, next = None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node = None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):

        self.length += 1

        new_node = ListNode(value)

        # If it's empty (there's no head or tail)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            old_head = self.head
            old_head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):

        # If the linked list is empty
        if self.head is None and self.tail is None:
            return None
        
        # If there's only 1 node
        if self.head == self.tail:
            self.length -= 1
            val = self.head.value
            self.head = None
            self.tail = None
            return val
        else:
            self.length -= 1
            val = self.head.value
            new_head = self.head.next
            self.head = new_head
            return val
        
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):

        self.length += 1

        new_node = ListNode(value)

        # Checking if the LL is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            old_tail = self.tail
            old_tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):

        # If the LL is empty (can't remove anything)
        if self.head is None and self.tail is None:
            return None
        
        # If there's only 1 node
        if self.head == self.tail:
            self.length -= 1
            val = self.head.value
            self.head = None
            self.tail = None
            return val
        else:
            self.length -= 1
            val = self.tail.value
            new_tail = self.tail.prev
            self.tail = new_tail
            return val

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # If it's already in front, do nothing
        if node == self.head:
            return None
        self.delete(node)
        self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # If it's already in the end, do nothing (Similar logic to move_to_front ^)
        if node == self.tail:
            return None
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):

        # If the LL is empty (nothing to delete)
        if self.head is None and self.tail is None:
            return None
        # If only 1 node in the LL (which means nothing is left after deletion)
        elif self.head is self.tail:
            self.length -= 1
            self.head = None
            self.tail = None
        # If the node to delete is the head, we first set self.head to 'next' and set the prev to 'none'
        elif node is self.head:
            self.length -= 1
            self.head = self.head.next
            self.head.prev = None
        # Similar logic as above applies to tail
        elif node is self.tail:
            self.length -= 1
            self.tail = self.tail.prev
            self.tail.next = None
        else: 
            self.length -= 1
            # The previous node's 'next' pointer goes to the current node's 'next'
            # And the next node's 'previous' pointer goes to the current node's 'previous'
            # Effectively deleting the current node and maintaining order
            node.prev.next = node.next
            node.next.prev = node.prev



    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # If empty, do nothing
        if self.head is None and self.tail is None:
            return None
        # We start with the head (default max value) and traverse the list.
        max_value = self.head.value

        # Traversing the LL
        current = self.head.next

        # We know we have reached the end of the list when self.head.next is None 
        while current is not None:
            if current.value > max_value:
                max_value = current.value
            # We set current to current.next to keep going (until we exit the loop)
            current = current.next
        return max_value
