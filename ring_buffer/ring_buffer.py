from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.current.value = item
            self.current = self.current.prev
        else:
            self.storage.add_to_head(item)
        
        self.current = (self.current + 1) % self.capacity

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        #The get method, which is provided, 
        # returns all of the elements in the buffer in a list in their given order. 
        # It should not return any None values in the list even if they are present in the ring buffer
        # go the through each element with a while list < the length of the storage length
        # TODO: Your code here

   

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
