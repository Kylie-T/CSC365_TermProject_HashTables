from Utils.node import node
from Utils.table import table


class linearTable(table):
    def _collision_method(self, slot, item):
        new_node = node(item)
        i = 0

        #checks if the index has a value assigned, if so, quadratic probing occurs
        while True:
            if (self._table[slot].ptr == None):
                self._table[slot].ptr = new_node
                break
            i += 1
            slot = (slot + i) % self._length



myTable = linearTable()
values = [12, 22, 15, 25, 16, 18, 23, 33, 22]
myTable.insert(values)
print(f'inserting values: {values}')
print(myTable)