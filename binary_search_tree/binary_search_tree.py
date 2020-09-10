"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # Left case
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                # Recursive call of insert method
                self.left.insert(value)
        # Right case
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Base case
        if self.value == target:
            return True
        # Left case
        if target < self.value:
            if self.left is None:
                return False
            else:
                # Recursive call of contains method
                return self.left.contains(target)
        # Right case
        if target >= self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # Since we are finding the max value, self.left is irrelevant (left values are lower in a BT)

        # If there's no right value, then we're already on the max
        if self.right is None:
            return self.value
        else:
            # Recursive call of get_max method
            return self.right.get_max()
        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        
        # Call fn on the current value
        fn(self.value)

        if self.right:
            # Recursive call of for_each method
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):

        if self.left:
            self.left.in_order_print()
        print(self.value)

        if self.right:
            self.right.in_order_print()



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self):
        # Using a queue
        queue = []

        # Add the root node to the queue
        queue.append(self)

        while len(queue) > 0:
            # Queue (FIFO) so we need to pop index 0!
            current_node = queue.pop(0)
            print(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self):
        # Using a stack
        stack = []

        # Add the root node to the stack
        stack.append(self)

        while len(stack) > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
