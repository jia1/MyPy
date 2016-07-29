####################### [CLASS] ListNode #######################
################################################################
# 
# Attributes:   data
#               ListNode next_node
#               ListNode prev_node
#
# Init:         data
#               ListNode next_node = None
# 
# Methods:  GET get_data()  -> data
#               get_next()  -> ListNode next_node
#               get_prev()  -> ListNode prev_node
#           SET set_data()
#               set_next()
#               set_prev()
# 
# Implemented:  [CLASS] LinkedList
#               [CLASS] Stack
#               [CLASS] Deque
# 
################################################################

class ListNode:
    data = None
    next_node = None
    prev_node = None
    
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node
    
    def get_data(self): return self.data
    def get_next(self): return self.next_node
    def get_prev(self): return self.prev_node
    
    def set_data(self, data):       self.data = data
    def set_next(self, next_node):  self.next_node = next_node
    def set_prev(self, prev_node):  self.prev_node = prev_node


###################### [CLASS] LinkedList ######################
################################################################
# 
# Attributes:   ListNode head
#               ListNode tail
#               int length
# 
# Init:         int length = 0
# 
# Methods:  GET get_head()              -> ListNode head or None
#               get_tail()              -> ListNode tail or None
#               get_length()            -> int length
#           SET set_head()              -> void
#           
#           ADD prepend(data)           -> void
#               append(data)            -> void
#               insert(index, data)     -> boolean
#           
#           DEL delete_first()          -> ListNode head or None
#               delete_last()           -> ListNode tail or None
#               delete(data) + 2 opt.   -> boolean
#               delete_at(index)        -> boolean
#           
#           REV reverse()               -> void
#           
#           OUT print_list()            -> void
# 
# 
# Method dependencies: (method <- calls)
# 
# clear     <- set_head
# 
# is_empty  <- get_head
#
# contains  <- get_head,
#              ListNode: get_data, get_next
# 
# get_node  <- ALL GET,
#              ListNode: get_next, get_prev
# 
# prepend   <- get_head, set_head,
#              ListNode: __init__, set_next, set_prev
# 
# append    <- get_head, set_head,
#              ListNode: __init__, set_next, set_prev
# 
# insert    <- prepend, append, ALL GET,
#              ListNode: ALL except get_data and set_data
# 
# delete_first  <- is_empty, get_head, set_head,
#                  ListNode: get_data, get_next
# 
# delete_last   <- is_empty, get_tail,
#                  ListNode: ALL GET, NO SET
# 
# delete    <- delete_first, delete_last, is_empty, get_head, get_tail,
#              ListNode: ALL except set_data
# 
# delete_at <- delete_first, delete_last, ALL GET,
#              ListNode: ALL except get_data and set_data
# 
# reverse   <- get_length, get_head, set_head
#              ListNode: ALL except get_data and set_data
# 
# print_list    <- ALL GET,
#                  ListNode: ALL GET
# 
# direct reference - summons the attributes directly without GET method
# 
# Used by:  [CLASS] LinkedList
#           [CLASS] Stack
#           [CLASS] Deque
# 
################################################################

class LinkedList:
    head = None
    tail = None
    length = 0 # length is updated via method calls
    
    def __init__(self):
        self.length = 0
    
    def get_head(self):     return self.head
    def get_tail(self):     return self.tail
    def get_length(self):   return self.length
    
    # Update the head attribute of the LinkedList object
    # Default option for update_tail is True
    # i.e. Finite calls of get_next() on head will reach tail
    # U/C:
    # self.set_head(new_head, False) -> Call self.length += 1
    # self.set_head(new_head, True) -> self.length is updated
    # Does not return a value (void)
    def set_head(self, head, update_tail = True):
        self.head = head                # direct reference
        new_length = 0
        if head == None:
            self.tail = head            # direct reference
            self.length = new_length    # direct reference
        else:
            pointer = head
            if update_tail:
                # parse through the LinkedList object
                # to get the pointer for the new tail
                while pointer.get_next() != None:
                    new_length += 1
                    pointer = pointer.get_next()
                self.tail = pointer             # direct reference
                self.length = new_length + 1    # direct reference
    
    # Does not return a value (void)
    def clear(self):
        self.set_head(self, None)
    
    # Checks if the LinkedList object is empty (no head node)
    # Returns either True or False (boolean)
    def is_empty(self):
        return self.get_head() == None
    
    # Checks if the LinkedList object has any node that contains data
    # Returns either True or False (boolean)
    def contains(self, data):
        pointer = self.get_head()
        while pointer != None:
            if pointer.get_data() == data:
                return True
            pointer = pointer.get_next()
        return False
    
    # Returns either the node at index (ListNode)
    # or None (index out of bounds)
    def get_node(self, index):
        if index >= self.get_length():
            return None
        else:
            last_index = self.get_length() - 1
            if index <= last_index // 2:
                iteration = 0
                pointer = self.get_head()
                while iteration < index:
                    pointer = pointer.get_next()
                    iteration += 1
            else:
                iteration = last_index
                pointer = self.get_tail()
                while iteration > index:
                    pointer = pointer.get_prev()
                    iteration -= 1
            return pointer
    
    # Does not return a value (void)
    def prepend(self, head_data):
        new_head = ListNode(head_data)
        if self.get_head() == None:
            self.set_head(new_head, True) # update tail as itself
        else:
            self.get_head().set_prev(new_head)
            new_head.set_next(self.head)
            self.set_head(new_head, False)
            self.length += 1 # direct reference
    
    # Does not return a value (void)
    def append(self, tail_data):
        new_tail = ListNode(tail_data)
        if self.get_head() == None:
            self.set_head(new_tail, True) # update tail as itself
        else:
            self.get_tail().set_next(new_tail) # set next of curr tail
            new_tail.set_prev(self.get_tail()) # set prev of new tail
            self.tail = new_tail    # direct reference
            self.length += 1        # direct reference
    
    # Returns either True or False (boolean)
    def insert(self, index, data): 
        last_index = self.get_length() - 1
        if index > last_index:      # if index out of bounds
            return False
        if index == 0:              # if prepend
            self.prepend(data)
            return True
        elif index == last_index:   # if append
            self.append(data)
            return True
        else:
            # If index is within first half of the LinkedList
            #   parse from the head
            # Else parse from the tail
            if index <= last_index // 2:
                iteration = 0
                pointer = self.get_head()
                while iteration < index:
                    pointer = pointer.get_next()
                    iteration += 1
            else:
                iteration = last_index
                pointer = self.get_tail()
                while iteration > index:
                    pointer = pointer.get_prev()
                    iteration -= 1
            # pointer is pointing to the ListNode at index
            # Before:   old previous <-> old next
            # After:    old previous <-> node <-> old next
            node = ListNode(data)
            node.set_prev(pointer.get_prev())
            node.set_next(pointer)
            pointer.get_prev().set_next(node)
            pointer.set_prev(node)
            self.length += 1 # direct reference
            return True
    
    # Similar to poll first
    # Return ListNode data if pop is called on a non-empty LinkedList
    def delete_first(self):
        if self.is_empty():
            return None
        popped = self.get_head()
        self.set_head(popped.get_next(), False)
        self.length -= 1 # direct reference
        return popped.get_data()
    
    # Return ListNode data if pop is called on a non-empty LinkedList
    # Similar to poll last
    def delete_last(self):
        if self.is_empty():
            return None
        popped = self.get_tail()
        self.tail = popped.get_prev()   # direct reference
        self.get_tail().set_next(None)  # remove ptr to old tail node
        self.length -= 1                # direct reference
        return popped.get_data()
    
    # Deletes the first node with the same value as data
    # 
    # Comes with 2 additional options
    # delete_all:   Every ListNode.data == data will be deleted
    # from_tail:    LinkedList will be parsed from the back
    # 
    # Returns either True or False (boolean)
    def delete(self, data, delete_all = False, from_tail = False):
        if self.is_empty():
            return False
        elif not delete_all:
            if not from_tail: # delete_all: False, from_tail: False
                pointer = self.get_head() # parse from the head
                if pointer.get_data() == data:
                    return self.delete_first() # exit
                pointer = pointer.get_next()
                if pointer == None:
                    return deleted # exit
                while pointer.get_next() != None:
                    if pointer.get_data() == data:
                        # Before:   old previous <-> node <-> old next
                        # After:    old previous <-> old next
                        pointer.get_prev().set_next(pointer.get_next())
                        pointer.get_next().set_prev(pointer.get_prev())
                        self.length -= 1 # direct reference
                        return True # exit
                    pointer = pointer.get_next()
                if pointer.get_data() == data:
                    return self.delete_last()
            else: # delete_all: False, from_tail: True
                pointer = self.get_tail() # parse from the tail
                if pointer.get_data() == data:
                    return self.delete_last() # exit
                pointer = pointer.get_prev()
                if pointer == None:
                    return deleted # exit
                while pointer.get_prev() != None:
                    if pointer.get_data() == data:
                        pointer.get_prev().set_next(pointer.get_next())
                        pointer.get_next().set_prev(pointer.get_prev())
                        self.length -= 1 # direct reference
                        return True
                    pointer = pointer.get_prev()
                if pointer.get_data() == data:
                    return self.delete_first()
        else:
            if not from_tail: # delete_all: True, from_tail: False
                pointer = self.get_head() # parse from the head
                deleted = False
                if pointer.get_data() == data:
                    deleted = self.delete_first()
                pointer = pointer.get_next()
                if pointer == None:
                    return deleted
                while pointer.get_next() != None:
                    if pointer.get_data() == data:
                        pointer.get_prev().set_next(pointer.get_next())
                        pointer.get_next().set_prev(pointer.get_prev())
                        self.length -= 1 # direct reference
                        deleted = True
                    pointer = pointer.get_next()
                if pointer.get_data() == data:
                    deleted = self.delete_last()
                return deleted # exit
            else: # delete_all: True, from_tail: True
                pointer = self.get_tail() # parse from the tail
                deleted = False
                if pointer.get_data() == data:
                    deleted = self.delete_last()
                pointer = pointer.get_prev()
                if pointer == None:
                    return deleted
                while pointer.get_prev() != None:
                    if pointer.get_data() == data:
                        pointer.get_prev().set_next(pointer.get_next())
                        pointer.get_next().set_prev(pointer.get_prev())
                        self.length -= 1 # direct reference
                        deleted = True
                    pointer = pointer.get_prev()
                if pointer.get_data() == data:
                    deleted = self.delete_first()
                return deleted # exit
    
    # Returns either True or False (boolean)
    def delete_at(self, index):
        last_index = self.get_length() - 1
        if index > last_index:
            return False
        if index == 0:
            self.delete_first()
            return True
        elif index == last_index:
            self.delete_last()
            return True
        else:
            # If index is within first half of the LinkedList
            #   parse from the front
            # Else parse from the back
            if index <= last_index // 2:
                iteration = 0
                pointer = self.get_head()
                while iteration < index:
                    pointer = pointer.get_next()
                    iteration += 1
            else:
                iteration = last_index
                pointer = self.get_tail()
                while iteration > last_index:
                    pointer = pointer.get_prev()
                    iteration -= 1
            new_next = pointer.get_next()     
            pointer.get_next().set_prev(pointer.get_prev())
            pointer.get_prev().set_next(new_next)
            self.length -= 1 # direct reference
            return True
    
    # Does not return a value (void)
    def reverse(self):
        pointer = self.get_head()
        # Step 01 - old head node -> new tail node
        old_next = pointer.get_next()
        pointer.set_next(pointer.get_prev())
        pointer.set_prev(old_next)
        self.tail = self.get_head() # direct reference
        pointer = old_next
        # Step 02 - for every internal node, swap the next and prev
        for i in xrange(self.get_length() - 2):
            old_next = pointer.get_next()
            pointer.set_next(pointer.get_prev())
            pointer.set_prev(old_next)
            pointer = old_next
        # Step 03 - old tail node -> new head node
        old_next = pointer.get_next()
        pointer.set_next(pointer.get_prev())
        pointer.set_prev(old_next)
        self.set_head(pointer, False)

    # LinkedList:   2 <-> 4 <-> 6
    # Output:       2 4 6 None 3 2 6
    # 
    # 2 4 6 are the values of each ListNode delimited by space
    # 3 is the length
    # 2 is the head
    # 6 is the tail
    #
    # Does not return a value (void)
    def print_list(self, from_tail = False):
        if not from_tail:
            pointer = self.get_head()
            while pointer != None:
                print pointer.get_data(),
                pointer = pointer.get_next()
            print None,
            print self.get_length(),
            if self.get_length() > 0: # if not None, print head and tail
                print self.get_head().get_data(),
                print self.get_tail().get_data()
            else:
                print
        else:
            pointer = self.get_tail()
            while pointer != None:
                print pointer.get_data(),
                pointer = pointer.get_prev()
            print None,
            print self.get_length(),
            if self.get_length() > 0: # if not None, print head and tail
                print self.get_tail().get_data(),
                print self.get_head().get_data()
            else:
                print


######################## [CLASS] Stack #########################
################################################################
# 
# Attributes:   Inherited from LinkedList
# Init:         Inherited from LinkedList
#
# Methods:      1. Inherited from LinkedList: clear, is_empty
#               (other methods not stated above should not be called)
# 
#               2. Stack methods derived from LinkedList methods
#           GET peek        -> data or None
#           ADD push        -> void
#           DEL pop         -> ListNode head or None
#           OUT print_stack -> void
# 
################################################################

class Stack(LinkedList):
    def __init__(self):
        pass
    
    def push(self, data):
        return self.prepend(data)
    
    def pop(self):
        return self.delete_first()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.get_head().get_data()
    
    def print_stack(self):
        self.print_list()


######################## [CLASS] Deque #########################
################################################################
# 
# Attributes:   Inherited from LinkedList
# Init:         Inherited from LinkedList
#
# Methods:      1. Inherited from LinkedList: clear, is_empty
#               (other methods not stated above should not be called)
# 
#               2. Deque methods derived from LinkedList methods
#           GET get_first   -> data or None
#               get_last    -> data or None
#  
#           ADD offer_first -> void
#               offer_last  -> void
# 
#           DEL poll_first  -> ListNode head or None
#               poll_last   -> ListNode tail or None
# 
#           OUT print_deque -> void
# 
################################################################

class Deque(LinkedList):
    def __init__(self):
        pass
    
    def get_first(self):
        if self.is_empty():
            return None
        return self.get_head().get_data()
    
    def get_last(self):
        if self.is_empty():
            return None
        return self.get_tail().get_data()
    
    def offer_first(self, data):
        return self.prepend(data)
    
    def offer_last(self, data):
        return self.append(data)
    
    def poll_first(self):
        return self.delete_first()
    
    def poll_last(self):
        return self.delete_last()
    
    def print_deque(self):
        self.print_list()
