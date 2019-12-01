#create a linked list: 2 classes: Node and LinkedList
#operations: insert item
#delete item
#print

class Node:
    def __init__(self, value = None, next = None):
        self._value = value
        self._next = next

    def value(self, value = None):
        if value: self._value = value
        return self._value
    
    def get_next(self):
        return self._next

    def set_next(self, next = None):
        self._next = next

class LinkedList():
    def __init__(self, head = None, length = None):
        self._head = head
        self._length = 0

    def head(self, head = None):
        if head: self._head = head
        return self._head
    
    def length(self, length = None):  # we should define how to calculate length
        if length: self._length = length
        return self._length

    def insertItem(self, value):
        newNode = Node(value)
        if (self.head() == None):
            self.head(newNode)
        else:
            newNode.set_next(self.head())
            self.head(newNode)
        self.length(self.length() + 1)

    def find(self, val): # find the first item with a given value
        item = self.head()
        i = 0
        while (item != None):
            if item.value() == val:
                return (i, item, item.value())
            else: 
                i +=1
                item = item.get_next()
        else: 
            print('Value {val} not found.')

    def deleteItem(self, index):   # delete an item at given index
        print(f'Delete item with index {index}.')
        if index < self.length():
            if index == 0:
                self.head(self.head().get_next())
            else:
                item = self.head()
                i = 0
                while (i < index):
                    prevItem = item
                    item = item.get_next()
                    i += 1
                prevItem.set_next(item.get_next())
            self.length(self.length() - 1)
        else:
            print(f'Index out of rage: expected values are between 0 and {self.length()-1}')

    def printList(self):
        item = self.head()
        while (item != None):
            print(f'Node: {item.value()}')
            item = item.get_next()
        print(f'Length: {self.length()}')

def main():
    list = LinkedList()
    list.insertItem(10)
    list.insertItem(20)
    list.insertItem(30)
    list.insertItem(40)
    list.printList()
    list.deleteItem(2)
    list.printList()
    print(list.find(30))


if __name__ == '__main__': main()