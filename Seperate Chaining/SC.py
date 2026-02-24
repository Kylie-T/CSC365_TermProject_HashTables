import enum

#class for hash table using seperate chaining for collisions
class collisionType(enum.Enum):
    LINEAR_PROBING = 0
    QUADRATIC_PORBING = 1
    SEPERATE_CHAINING = 2

class table:
    





    def __init__(self, initial_length = 5, collision_method=collisionType.LINEAR_PROBING):
        self._table = []
        self._collision_method = collision_method
        
        #fill table with initial_length amount of empty spaces (space used to represent None)
        for i in range(initial_length):
            self._table.append([' '])
        
        #set max length
        self._length = initial_length
        self._count = 0

    def insert(self, item):

        if (not isinstance(item, list)):
            #get index by using mod
            slot = item % self._length
            
            #checks for collision handling type requested
            match (self._collision_method):
                case (collisionType.LINEAR_PROBING):
                    self._linear_probing(slot, item)
                case (collisionType.QUADRATIC_PORBING):
                    self._quadratic_probing(slot, item)
                case (collisionType.SEPERATE_CHAINING):
                    self._separate_chaining(slot, item)

            self._count += 1


        else:
            for val in item:
                #get index by using mod
                slot = val % self._length
                
                #checks for collision handling type requested
                match (self._collision_method):
                    case (collisionType.LINEAR_PROBING):
                        self._linear_probing(slot, val)
                    case (collisionType.QUADRATIC_PORBING):
                        self._quadratic_probing(slot, val)
                    case (collisionType.SEPERATE_CHAINING):
                        self._separate_chaining(slot, val)
                self._count += 1

       
        

    def setCollisionMode(self, type):
        if (isinstance(type, collisionType)):
            self._collision_method = type
        else:
            self._collision_method = collisionType.LINEAR_PROBING

    def clearTable(self):
        del self._table
        self._table = []
        self._count = 0
        for i in range(self._length):
            self._table.append([' '])
        
    
    #Linear Probing
    # _ used to indicate private method*
    def _linear_probing(self, slot, item):
        pass
        
    #Quadratic Probing
    # _ used to indicate private method*
    def _quadratic_probing(self, slot, item):

        org_slot = slot
        i = 0
        #checks if the index has a value assigned, if so, quadratic probing occurs
        while True:
            if (self._table[slot][0] == ' '):
                self._table[slot][0] = item
                return
            i+=1
            slot = (org_slot + i**2) % self._length

            #resizes the table once all indices are checked
            self._check_resize()
        
        #loop provides viable index to set value
        self._table[slot][0] = item

    #Separate Chaining
    # _ used to indicate private method*
    def _separate_chaining(self, slot, item):
        #fill first spot if empty or add a new item to the list
        if (self._table[slot][0] == ' '):
            self._table[slot][0] = item
        else:
            self._table[slot].append(item)
        self._check_resize()


    #check if a resize is needed based on a threshold (75% by default)
    # _ used to indicate private method*
    def _check_resize(self, threshold=0.75):
        load_factor = self._count / self._length
        if load_factor > threshold:
            self._resize()
            
    #handles resizing (doubles previous size)
    # _ used to indicate private method*
    def _resize(self):
        old_table = self._table
        old_length = self._length

        self._length *= 2
        self._table = [[' '] for _ in range(self._length)]
        self._count = 0  # will reinsert everything

        for bucket in old_table:
            for value in bucket:
                if isinstance(value, int):
                    self.insert(value)
    
    #returns a easy to read string representation of the hash table
    def __str__(self):
        string = ''
        num = 0
        for item in self._table:
            index = 0
            for inner_item in item:
                string += '['
                string += str(inner_item)
                string += ']'
                if (index < len(item) - 1):
                   string += ' => '

                index += 1
            if (num < self._length - 1):   
                string += '\n'
            num += 1
        return string

if __name__ == "__main__": 

    #create a new hash table
    MyTable = table()


    #LINEAR PROBING
    #insert some values into the table
    
    print("\nLinear Probing")
    MyTable.setCollisionMode(collisionType.LINEAR_PROBING)
    MyTable.insert([12,22,15,25,16,18,23,33])
    print(MyTable)
    MyTable.clearTable()
    

    

    #QUADRATIC PROBING
    #insert some values into the table
    
    print("\nQuadratic Probing")
    MyTable.setCollisionMode(collisionType.QUADRATIC_PORBING)
    MyTable.insert([12,22,15,25,16,18,23,33])
    print(MyTable)
    MyTable.clearTable()
    


    #SEPARATE CHAINING 
    #insert some values into the table
    
    print("\nSeparate Chaining")
    MyTable.setCollisionMode(collisionType.SEPERATE_CHAINING)
    MyTable.insert([12,22,15,25,16,18,23,33])
    print(MyTable)
    MyTable.clearTable()
    