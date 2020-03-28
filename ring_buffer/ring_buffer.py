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


        #almost working

        # #start point for the ring
        # if self.storage == 0:
        #     self.storage.add_to_head(item)
        #     self.current = self.storage(head)
        
        # #overwrite when at cap.
        # if self.storage.length == self.capacity:
        #     self.storage.remove_from_head()
        #     self.storage.add_to_tail(item)
        #     self.current = self.storage.tail
        # # add when not at cap. 
        # else:
        #     self.storage.add_to_tail(item)
                   
          #start point for the ring
        # if self.storage == 0:
        #     self.storage.add_to_head(item)
        #     self.current = self.storage(head)
        
       
        # elif self.storage.length == self.capacity and not self.storage.head:
           
        #     self.storage.remove_from_head()
        #     self.current.add_to_tail(item)
        # #overwrite when at cap.
        # elif self.storage.length == self.capacity:
        #     self.storage.remove_from_head()
        #     self.storage.add_to_head(item)
        #     self.current = self.storage.tail
        # # add when not at cap. 
        # else:
        #     self.storage.add_to_tail(item)
        # try number 4
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            if self.storage.length == self.capacity:
                self.current = self.storage.head
        
        else: 
            self.current.value = item
            if self.current.next != None:
                self.current = self. current.next

            else: 
                self.current = self.storage.head
        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        #The get method, which is provided, 
        # returns all of the elements in the buffer in a list in their given order. 
        # It should not return any None values in the list even if they are present in the ring buffer
       
        # TODO: Your code here
        
       
        current = self.storage.head
        while len(list_buffer_contents) < self.storage.length:
            print(current.value, "324432")
            list_buffer_contents.append(current.value)
         
            if current.next: 
                current = current.next
        else: 
            current = self.storage.tail

        
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
