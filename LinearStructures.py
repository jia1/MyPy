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

class LinkedList:
    head = None
    tail = None
    length = 0
    
    def __init__(self):
        self.length = 0
    
    def get_head(self): return self.head
    def get_tail(self): return self.tail
    def get_length(self): return self.length
    
    def set_head(self, head, update_tail = True):
        self.head = head                # direct reference
        new_length = 0
        if head == None:
            self.tail = head            # direct reference
            self.length = new_length    # direct reference
        else:
            pointer = head
            if update_tail:
                while pointer.get_next() != None:
                    new_length += 1
                    pointer = pointer.get_next()
                self.tail = pointer             # direct reference
                self.length = new_length + 1    # direct reference
    
    def prepend(self, head_data):
        new_head = ListNode(head_data)
        if self.get_head() == None:
            self.set_head(new_head, True)
        else:
            self.get_head().set_prev(new_head)
            new_head.set_next(self.head)
            self.set_head(new_head, False)
        self.length += 1
    
    def append(self, tail_data):
        tail = ListNode(tail_data)
        if self.get_head() == None:
            self.set_head(tail, True)
        else:
            pointer = self.get_head()
            while pointer.get_next() != None:
                pointer = pointer.get_next()
            tail.set_prev(pointer)
            pointer.set_next(tail)
            self.tail = tail # direct reference
            self.length += 1 # direct reference
    
    def insert(self, index, data): 
        last_index = self.get_length() - 1
        if index > last_index:
            return False
        if index == 0:
            self.prepend(data)
            return True
        elif index == last_index:
            self.append(data)
            return True
        else:
            if index <= last_index // 2:
                iteration = 0
                pointer = self.get_head()
                while iteration < index:
                    pointer = pointer.get_next()
                    iteration += 1
            else:
                iteration = last_index
                pointer = self.get_tail()
                while iteration >= last_index:
                    pointer = pointer.get_prev()
                    iteration -= 1
            node = ListNode(data)
            node.set_prev(pointer.get_prev())
            node.set_next(pointer)
            pointer.get_prev().set_next(node)
            pointer.set_prev(node)
            self.length += 1
            return True
    
    def delete_first(self):
        if self.get_head() == None:
            return False
        self.set_head(self.get_head().get_next(), False)
        self.length -= 1
        return True
    
    def delete_last(self):
        if self.get_tail() == None:
            return False
        self.tail = self.tail.get_prev()
        self.tail.set_next(None)
        self.length -= 1
        return True
    
    def delete(self, data, delete_all = False, from_back = False):
        if from_back:
            pointer = self.get_tail()
            if delete_all:
                deleted = False
                while pointer != None:
                    if pointer.get_data() == data:
                        pointer.get_next().set_prev(pointer.get_next())
                        if pointer.get_prev() != None:
                            pointer.get_prev().set_next(pointer.get_next())
                        deleted = True
                    pointer = pointer.get_prev()
                return deleted
            else:
                while pointer != None:
                    if pointer.get_data() == data:
                        pointer.get_next().set_prev(pointer.get_next())
                        if pointer.get_prev() != None:
                            pointer.get_prev().set_next(pointer.get_next())
                        return True
                    pointer = pointer.get_prev()
        else:
            pointer = self.get_head()
            if delete_all:
                deleted = False
                while pointer != None:
                    if pointer.get_data() == data:
                        pointer.get_prev().set_next(pointer.get_next())
                        if pointer.get_next() != None:
                            pointer.get_next().set_prev(pointer.get_prev())
                        deleted = True
                    pointer = pointer.get_next()
                return deleted
            else:
                while pointer != None:
                    if pointer.get_data() == data:
                        pointer.get_prev().set_next(pointer.get_next())
                        if pointer.get_next() != None:
                            pointer.get_next().set_prev(pointer.get_prev())
                        return True
                    pointer = pointer.get_next()
    
    def delete_at(self, index):
        # incomplete
        pass
    
    def reverse(self):
        pointer = self.get_head()
        
        old_next = pointer.get_next()
        pointer.set_next(pointer.get_prev())
        pointer.set_prev(old_next)
        self.tail = self.get_head() # direct reference
        pointer = old_next
        
        for i in xrange(self.get_length() - 2):
            old_next = pointer.get_next()
            pointer.set_next(pointer.get_prev())
            pointer.set_prev(old_next)
            pointer = old_next
        
        old_next = pointer.get_next()
        pointer.set_next(pointer.get_prev())
        pointer.set_prev(old_next)
        self.set_head(pointer, False)
    
    def print_list(self):
        pointer = self.get_head()
        while pointer != None:
            print pointer.get_data(),
            pointer = pointer.get_next()
        print None,
        print self.get_length(),
        if self.get_length() > 0:
            print self.get_head().get_data(),
            print self.get_tail().get_data()
        else:
            print
        
