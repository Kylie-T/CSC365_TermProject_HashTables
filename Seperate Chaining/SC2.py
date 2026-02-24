import enum


#class for hash table using seperate chaining for collisions
class collisionType(enum.Enum):
    LINEAR_PROBING = 0
    QUADRATIC_PORBING = 1
    SEPERATE_CHAINING = 2

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

class table:
    def __init__(self, initial_length = 5, collision_method=collisionType.SEPERATE_CHAINING):
        self._table = []
        self._collision_method = collision_method
        
        #fill table with initial_length amount of empty spaces (space used to represent None)
        for i in range(initial_length):
            self._table.append(node(f'b{i}'))
        
        #set max length
        self._length = initial_length
        self._count = 0

    def insert(self, item):

        if not isinstance(item, list):
            self._check_resize()

            slot = item % self._length
            self._separate_chaining(slot, item)
            self._count += 1

        else:
            for val in item:
                #check if size is > load factor then resize
                self._check_resize()

                slot = val % self._length
                self._separate_chaining(slot, val)
                self._count += 1
    
    def _separate_chaining(self, slot, item):
        
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

myTable = table()
values = [12, 22, 15, 25, 16, 18, 23, 33]
myTable.insert(values)
print(f'inserting values: {values}')
print(myTable)