from abc import ABC, abstractmethod

TABLE_LENGTH = 5

class node:
    def __init__(self, value, ptr=None):
        self._value = value
        self._ptr=ptr

    @property
    def ptr(self):
        return self._ptr

    @ptr.setter
    def ptr(self, nd):
        self._ptr = nd

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    def __str__(self):
        return f"[{self._value} | {self._ptr}]"

    def __repr__(self):
        return f"[{self._value} | {self._ptr}]"
    
class table(ABC):
    def __init__(self, initial_length = TABLE_LENGTH):
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

        #double table size
        self._length *= 2

        #create new empty table
        self._table = [node(f"b{i}") for i in range(self._length)]

        #reset count
        self._count = 0

        #reinsert all old values
        for bucket in old_table:
            if bucket.ptr is not None:
                self.insert(bucket.ptr.value)

    def __str__(self):
        string = ""
        for item in self._table:
            item_node = item
            while True:
                string += f"[ {item_node.value} | {' ' if item_node.ptr is not None else 'X'} ]"
                if (item_node.ptr == None):
                    string += "\n"
                    break
                else:
                    string += " => "
                    item_node = item_node.ptr


        return "\n" + string + "\n"
    




class linearTable(table):

    def _collision_method(self, slot, item):
        
        # keeps going until the current bucket is empty
        while (self._table[slot].ptr is not None):
            slot = (slot + 1) % self._length
        
        # inserts new node
        self._table[slot].ptr = node(item)



class quadTable(table):

    def _collision_method(self, slot, item):
        new_node = node(item)
        i = 0

        #checks if the index has a value assigned, if so, quadratic probing occurs
        while True:
            if (self._table[slot].ptr == None):
                self._table[slot].ptr = new_node
                break
            i += 1
            slot = (slot + i**2) % self._length


class chainingTable(table):

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

    def _collision_method(self, slot, item):
        #create a new node to add
        new_node = node(item)

        #set a temporary "next node"
        next_node = self._table[slot]
        while (True):
            #set next node's pointer to added node or get next node
            if (next_node.ptr == None):
                next_node.ptr = new_node
                break
            else:
                next_node = next_node.ptr


values = [12, 22, 15, 25, 16]
print(f"initial table size is {TABLE_LENGTH}")

myTable = linearTable()

myTable.insert(values)
print(f'linear probing: inserting values: {values}')
print(myTable)

myTable = quadTable()

myTable.insert(values)
print(f'quadratic probing: inserting values: {values}')
print(myTable)

myTable = chainingTable()

myTable.insert(values)
print(f'separate chaining: inserting values: {values}')
print(myTable)