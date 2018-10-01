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
        if self.tail is None:
            self.tail = self.head


    def insert_last(self, value):
            oldtail = self.head
            while oldtail.next is not None:
                oldtail = oldtail.next
            node = Node(value)
            oldtail.next = node
            self._size += 1


    def insert_at_position(self,value,position):
        if position >= self._size:
            self.insert_last(value)
            return
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
        self._size += 1

    def delete(self, value):
        temp = self.head
        if (temp is not None):
            if temp.value == value:
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.value == value:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next
        temp = None
        self._size -= 1

    def printnodes(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def search(self, value):
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return True
            else:
                temp = temp.next
        return False

    def removeDuplicate(self):
        temp = self.head
        if self.head is None:
            return

        while temp.next is not None:
            if temp.value == temp.next.value:
                next_node = temp.next.next
                temp.next = None
                temp.next = next_node
            else:
                temp = temp.next
        self._size -= 1        
    @property
    def size(self):
        return f"size is: {self._size}"



nodeC = SinglyLL()
nodeC.insert_first(5)
nodeC.insert_first(7)
nodeC.insert_first(8)
nodeC.insert_at_position("omar",4)
print(nodeC.search(8))
nodeC.insert_at_position(5,1)
nodeC.removeDuplicate()
nodeC.printnodes()
print(nodeC.size)
