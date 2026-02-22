#class for hash table using seperate chaining for collisions
class table:
    def __init__(self, initial_length = 5, collision_method='linear_probing'):
        self._table = []
        self._collision_method = collision_method
        
        #fill table with initial_length amount of empty spaces (space used to represent None)
        for i in range(initial_length):
            self._table.append([' '])
        
        #set max length
        self._length = initial_length

    def insert(self, item):
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
        while (self._table[slot][0] != ' '):
            slot = (org_slot + i**2) % self._length
            i+=1

            #resizes the table once all indices are checked
            if (i > self._length):
                self._resize()
                break
        
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
        new_size = self._length * 2
        for i in range(self._length, new_size):
            self._table.append([' '])
       
        self._length = new_size
    
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
    # print("Linear Probing")
    # MyTable = table(collision_method='linear_probing')
    # MyTable.insert(12)
    # print(str(MyTable) + "\n")
    # MyTable.insert(22)
    # print(str(MyTable) + "\n")
    # MyTable.insert(15)
    # print(str(MyTable) + "\n")
    # MyTable.insert(25)
    # print(str(MyTable) + "\n")
    # MyTable.insert(16)
    # print(str(MyTable) + "\n")
    # MyTable.insert(18)
    # print(str(MyTable) + "\n")
    # MyTable.insert(23)
    # print(str(MyTable) + "\n")
    # MyTable.insert(33)
    # print(MyTable)

    #QUADRATIC PROBING
    #insert some values into the table
    print("\nQuadratic Probing")
    MyTable = table(collision_method='quadratic_probing')
    MyTable.insert(12)
    print(str(MyTable) + "\n")
    MyTable.insert(22)
    print(str(MyTable) + "\n")
    MyTable.insert(15)
    print(str(MyTable) + "\n")
    MyTable.insert(25)
    print(str(MyTable) + "\n")
    MyTable.insert(16)
    print(str(MyTable) + "\n")
    MyTable.insert(18)
    print(str(MyTable) + "\n")
    MyTable.insert(23)
    print(str(MyTable) + "\n")
    MyTable.insert(33)
    print(MyTable)

    #SEPARATE CHAINING 
    #insert some values into the table
    # print("\nSeparate Chaining")
    # MyTable = table(collision_method='separate_chaining')
    # MyTable.insert(12)
    # print(str(MyTable) + "\n")
    # MyTable.insert(22)
    # print(str(MyTable) + "\n")
    # MyTable.insert(15)
    # print(str(MyTable) + "\n")
    # MyTable.insert(25)
    # print(str(MyTable) + "\n")
    # MyTable.insert(16)
    # print(str(MyTable) + "\n")
    # MyTable.insert(18)
    # print(str(MyTable) + "\n")
    # MyTable.insert(23)
    # print(str(MyTable) + "\n")
    # MyTable.insert(33)
    # print(MyTable)


