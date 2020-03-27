from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if len(self.storage) == self.capacity:
        #     self.current.value = item
        #     self.current = self.current.prev
        # else:
        #     self.storage.add_to_head(item)
        #     self.current = self.storage.tail
        
        #start point for the ring
        if self.storage == 0:
            self.storage.add_to_head(item)
            self.current = self.storage(head)
        
        #overwrite when at cap.
        if self.storage.length == self.capacity:
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        # add when not at cap. 
        else:
            self.storage.add_to_tail(item)
                   
        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        #The get method, which is provided, 
        # returns all of the elements in the buffer in a list in their given order. 
        # It should not return any None values in the list even if they are present in the ring buffer
       
        # TODO: Your code here
        
        # go the through each element with a while list current_bode is n
        current_item = self.storage.tail
        while current_item is not self.storage.head:
            list_buffer_contents.append(current_item.value)
            current_item = current_item.prev
        list_buffer_contents.append(self.storage.head.value)
# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
