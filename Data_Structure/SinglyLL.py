class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class SinglyLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    def insert_first(self,value):
        oldnode = self.head
        self.head = Node(value)
        self.head.next = oldnode
        self._size += 1


    def __repr__(self):
        return f"{self.head.next.value}"


    def insert_at_position(self,value,position):
        if position == 0:
            insert_first(value)
            self._size += 1
        temp = self.head
        prev =  None
        i = 0
        while temp.next  != None and i <= position-1:
                prev = temp
                temp = temp.next
                i += 1
        node = Node(value)
        node.next = temp
        prev.next = node
    def delete(self):
        self.head = self.head.next
        self._size -= 1
    def printnodes(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    @property
    def size(self):
        return f"size is: {self._size}"
nodeC = SinglyLL()
nodeC.insert_first(5)
nodeC.insert_first(7)
nodeC.insert_first(8)
nodeC.insert_at_position("omar",4)
nodeC.printnodes()
print(nodeC.size)
