from LinearStructures import *

####################### [CLASS] TreeNode #######################
################################################################
# 
################################################################

class TreeNode:
    data = None
    left = None
    right = None
    parent = None
    weight = 0
    
    def __init__(self, data = None):
        if data != None:
            self.data = data
            self.weight = 1
    
    def get_data(self):     return self.data
    def get_left(self):     return self.left
    def get_right(self):    return self.right
    def get_parent(self):   return self.parent
    def get_weight(self):   return self.weight
    
    def set_data(self, data):       self.data = data
    def set_left(self, left):       self.left = left
    def set_right(self, right):     self.right = right
    def set_parent(self, parent):   self.parent = parent
    
    def has_children(self):
        return self.get_left() != None and self.get_right() != None
    
    def is_terminal(self):
        return self.get_left() == None and self.get_right() == None


################## [CLASS] BinarySearch Tree ###################
################################################################
# 
################################################################

class BinarySearchTree:
    root = None
    
    def __init__(self):
        pass
    
    def get_root(self):         return self.root
    def set_root(self, root):   self.root = root
    
    def is_empty(self):         return self.get_root() == None
    
    def insert(self, data):
        node = TreeNode(data)
        if self.is_empty():
            self.set_root(node)
        else:
            pointer = self.get_root()
            while True:
                pointer.weight += 1 # direct reference
                if data < pointer.get_data():
                    if pointer.get_left() == None:
                        node.set_parent(pointer)
                        pointer.set_left(node)
                        break
                    else:
                        pointer = pointer.get_left()
                else:
                    if pointer.get_right() == None:
                        node.set_parent(pointer)
                        pointer.set_right(node)
                        break
                    else:
                        pointer = pointer.get_right()
    
    def print_in_order(self):
        pointer = self.get_root()
        node_stack = Stack()
        node_stack.push(pointer)
        while pointer != None and not node_stack.is_empty():
            while pointer.get_left() != None:
                pointer = pointer.get_left()
                node_stack.push(pointer)
            print pointer.get_data(),
            pointer = node_stack.pop()
            while pointer.get_right() == None:
                if node_stack.is_empty():
                    break
                pointer = node_stack.pop()
                print pointer.get_data(),
            pointer = pointer.get_right()
            node_stack.push(pointer)
