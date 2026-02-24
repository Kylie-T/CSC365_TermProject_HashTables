from Utils.node import node
from Utils.table import table


class chainingTable(table):
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

myTable = chainingTable()
values = [12, 22, 15, 25, 16, 18, 23, 33, 22]
myTable.insert(values)
print(f'inserting values: {values}')
print(myTable)