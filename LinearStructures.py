################ [CLASS] ListNode ################
##################################################
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
##################################################
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
    
    def set_data(self, data): self.data = data
    def set_next(self, next_node): self.next_node = next_node
    def set_prev(self, prev_node): self.prev_node = prev_node


############### [CLASS] LinkedList ###############
##################################################
# Attributes:   ListNode head
#               ListNode tail
#               int length
#
# Init:         int length = 0
#
# Methods:  GET get_head()      -> ListNode head
#               get_tail()      -> ListNode tail
#               get_length()    -> int length
#           SET set_head()
#           
#           ADD prepend(data)
#               append(data)
#               insert(index, data)
#           
#           DEL delete_first()
#               delete_last()
#               delete(data) + 2 other options
#               delete_at(index)
#           
#           REV reverse()
#           
#           OUT print_list()
#
# Used by:  [CLASS] LinkedList
#           [CLASS] Stack
#           [CLASS] Deque
##################################################
class LinkedList:
    head = None
    tail = None
    length = 0 # length is updated via method calls
    
    def __init__(self):
        self.length = 0
    
    def get_head(self): return self.head
    def get_tail(self): return self.tail
    def get_length(self): return self.length
    
    # Update the head attribute of the LinkedList object
    # Default option for update_tail is True
    # i.e. Finite calls of get_next() on head will reach tail
    # U/C:
    # self.set_head(new_head, False) -> Call self.length += 1
    # self.set_head(new_head, True) -> self.length is updated
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
    
    def prepend(self, head_data):
        new_head = ListNode(head_data)
        if self.get_head() == None:
            self.set_head(new_head, True) # update tail as itself
        else:
            self.get_head().set_prev(new_head)
            new_head.set_next(self.head)
            self.set_head(new_head, False)
            self.length += 1 # direct reference
    
    def append(self, tail_data):
        new_tail = ListNode(tail_data)
        if self.get_head() == None:
            self.set_head(new_tail, True) # update tail as itself
        else:
            self.get_tail().set_next(new_tail) # set next of curr tail
            new_tail.set_prev(self.get_tail()) # set prev of new tail
            self.tail = new_tail    # direct reference
            self.length += 1        # direct reference
    
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
                while iteration > last_index:
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
    def delete_first(self):
        popped = self.get_head()
        if popped == None:
            return popped
        self.set_head(popped.get_next(), False)
        self.length -= 1 # direct reference
        return popped.get_data()

    # Similar to poll last
    def delete_last(self):
        popped = self.get_tail()
        if popped == None:
            return popped
        self.tail = self.get_tail().get_prev() # direct reference
        self.get_tail().set_next(None)  # remove ptr to old tail node
        self.length -= 1                # direct reference
        return popped.get_data()

    # Deletes the first node with the same value as data
    #
    # Comes with 2 additional options
    # delete_all:   Every ListNode.data == data will be deleted
    # from_tail:    LinkedList will be parsed from the back
    def delete(self, data, delete_all = False, from_tail = False):
        if not delete_all:
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
            
class Stack(LinkedList):
    def __init__(self):
        pass
    
    def push(self, data):
        return self.prepend(data)
    
    def pop(self):
        return self.delete_first()
    
    def peek(self):
        return self.get_head().get_data()
    
    def print_stack(self):
        self.print_list()
