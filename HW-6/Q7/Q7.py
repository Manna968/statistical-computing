class Node:
    def __init__(self, data):
        self.tooBig = None 
        self.big = None 
        self.small = None
        self.data = data
     
    def insert(self, data):
        if self.data:
            if data - self.data >=10:
                if self.tooBig:
                    self.tooBig.insert(data)
                else:
                    self.tooBig = Node(data)
            elif (data < self.data):
                if self.small:
                    self.small.insert(data)
                else:
                    self.small = Node(data)
            else:
                if self.big:
                    self.big.insert(data)
                else:
                    self.big = Node(data)
        else: 
            self.data = data
    
    def delete(self, data):
        new_list = []
        self.traversal_list(new_list)
        self.tooBig = None
        self.big = None
        self.small = None
        self.data = None
        for node in new_list:
            if node == data:
                continue
            if not self.data:
                self.data = node
            else:
                self.insert(node)
    
    def traversal_list(self, list = None):
        if self.small:
            self.small.traversal_list(list)
        if list is not None:
            list.append(self.data)
        if self.big:
            self.big.traversal_list(list)
        if self.tooBig:
            self.tooBig.traversal_list(list)


    def traversal(self):
        if self.small:
            self.small.traversal()
        print(self.data)
        if self.big: 
            self.big.traversal()
        if self.tooBig:
            self.tooBig.traversal()        



root = Node(20)
root.insert(40)
root.insert(45)
root.insert(32)

print("Tree contents after insertion using the traversal():")
root.traversal()

root.delete(45)

print("Tree contents after deleting 45 using the traversal():")

root.traversal()