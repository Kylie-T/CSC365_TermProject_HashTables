from Utils.node import node
from Utils.table import table


class linearTable(table):
    def _collision_method(self, slot, item):
        start = slot
        # keeps going until the current bucket is empty
        while (self._table[slot].ptr is not None):
            slot = (slot + 1) % self._length
        
        # inserts new node
        self._table[slot].ptr = node(item)




myTable = linearTable()
values = [12, 22, 15, 25, 16, 18, 23, 33, 22]
myTable.insert(values)
print(f'inserting values: {values}')
print(myTable)
