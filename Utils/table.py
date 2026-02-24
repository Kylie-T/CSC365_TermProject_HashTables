from abc import ABC, abstractmethod
from Utils.node import node

class table(ABC):
    def __init__(self, initial_length = 7):
        self._table = []
        
        #fill table with initial_length amount of empty nodes
        for i in range(initial_length):
            self._table.append(node(f'b{i}'))
        
        #set max length
        self._length = initial_length
        self._count = 0

    def insert(self, item):

        #used for inserting evey value in a list or not
        if not isinstance(item, list):

            #check if size is > load factor then resize
            self._check_resize()

            slot = item % self._length
            self._collision_method(slot, item)
            self._count += 1

        else:
            for val in item:
                #check if size is > load factor then resize
                self._check_resize()

                slot = val % self._length
                self._collision_method(slot, val)
                self._count += 1

    @abstractmethod
    def _collision_method(self, slot, item):
        '''Must be implemented by child class'''
        print("child method not implemented")
        exit(-1)

    #check if a resize is needed based on a threshold (75% by default)
    # _ used to indicate private method*
    def _check_resize(self, threshold=0.75):
        if (self._count + 1) / self._length > 0.75:
            self._resize()
            
    #handles resizing (doubles previous size)
    # _ used to indicate private method*
    def _resize(self):
        old_table = self._table
        self._length *= 2

        #rebuild table with empty bucket nodes
        self._table = [node(f'b{i}') for i in range(self._length)]
        self._count = 0  

        #rehash all existing values
        for bucket in old_table:
            current = bucket.ptr  
            while current is not None:
                self.insert(current.value)
                current = current.ptr

    def __str__(self):
        string = ""
        for item in self._table:
            item_node = item
            while True:
                string += f"[ {str(item_node.value)} | {" " if item_node.ptr != None else "X"} ]"
                if (item_node.ptr == None):
                    string += "\n"
                    break
                else:
                    string += " => "
                    item_node = item_node.ptr


        return "\n" + string + "\n"
    

