#class for hash table using seperate chaining for collisions
class table:
    def __init__(self, initial_length = 5, collision_method='linear_probing', auto_resize=True):
        self._table = []
        self._do_resize = auto_resize
        self._collision_method = collision_method
        
        #fill table with initial_length amount of empty spaces (space used to represent None)
        for i in range(initial_length):
            self._table.append([' '])
        
        #set max length
        self._length = initial_length

    def insert(self, item):

        if (not isinstance(item, list)):
            #get index by using mod
            slot = item % self._length
            
            #checks for collision handling type requested
            if self._collision_method == 'linear_probing':
                self._linear_probing(slot, item)
            if self._collision_method == 'quadratic_probing':
                self._quadratic_probing(slot, item)
            if self._collision_method == 'separate_chaining':
                self._separate_chaining(slot, item)

            #extra: resize table if 75% full on both axes
            if (self._do_resize):
                self._check_resize()
        else:
            for val in item:
                #get index by using mod
                slot = val % self._length
                
                #checks for collision handling type requested
                if self._collision_method == 'linear_probing':
                    self._linear_probing(slot, val)
                if self._collision_method == 'quadratic_probing':
                    self._quadratic_probing(slot, val)
                if self._collision_method == 'separate_chaining':
                    self._separate_chaining(slot, val)

                #extra: resize table if 75% full on both axes
                if (self._do_resize):
                    self._check_resize()


    
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
            if (i >= self._length):
                self._resize()
                self.insert(item)
                return

    #Separate Chaining
    # _ used to indicate private method*
    def _separate_chaining(self, slot, item):
        #fill first spot if empty or add a new item to the list
        if (self._table[slot][0] == ' '):
            self._table[slot][0] = item
        else:
            self._table[slot].append(item)


    #check if a resize is needed based on a threshold (75% by default)
    # _ used to indicate private method*
    def _check_resize(self, threshold: float = 0.75):

        max_fill = int(threshold * self._length)
        y_full = 0
        for y in self._table:
            x_full = 0
            for x in y:
                if (isinstance(x, int)):
                    x_full += 1
                
                if (x_full > max_fill):
                    self._resize()
                    break
            if (isinstance(y, int)):
                y_full += 1
        
            if (y_full > max_fill):
                self._resize()
                break
        
    #handles resizing (doubles previous size)
    # _ used to indicate private method*
    def _resize(self):

        #copies old table
        old_table = self._table.copy()
        self._length *= 2

        #resets table instead of keeping old values, needs to be rehashed
        self._table = [[' '] for i in range(self._length)]

        #linear and quadratic probing cases
        if self._collision_method == 'linear_probing' or self._collision_method == 'quadratic_probing':
            #re-inserts each value to the new, resized table; rehashing
            for row in old_table:
                if row[0] != ' ':
                    self.insert(row[0])

        #separate chaining case
        elif (self._collision_method == 'separate_chaining'):
            #re-inserts each value in each linked list
            for bucket in old_table:
                for item in bucket:
                    self.insert(item)
            
       
    
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
    print("Linear Probing")
    MyTable = table(collision_method='linear_probing', auto_resize=False)

    MyTable.insert([12,22,15,25,16,18,23,33])
    print(MyTable)
    

    #QUADRATIC PROBING
    #insert some values into the table
    
    print("\nQuadratic Probing")
    MyTable = table(collision_method='quadratic_probing', auto_resize=False)

    MyTable.insert([12,22,15,25,16,18,23,33])
    print(MyTable)
    
    

    #SEPARATE CHAINING 
    #insert some values into the table
    print("\nSeparate Chaining")
    MyTable = table(collision_method='separate_chaining', auto_resize=False)

    MyTable.insert([12,22,15,25,16,18,23,33])
    print(MyTable)
    
    