class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


# Class to create a Linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Print the linked list
    def print_list(self):
        if self.head == None:
            raise ValueError("List is empty")

        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
        print("\n")

    # Find length of Linked List
    def size(self):
        if self.head == None:
            return 0

        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next

        return size

    # Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.head
        if not current:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node

    # Delete a node in a linked list
    def delete(self, data):
        if not self.head:
            return

        temp = self.head

        # Check if head node is to be deleted
        if self.head.data == data:
            head = temp.next
            print("Deleted node is " + str(self.head.data))
            return

        while temp.next:
            if temp.next.data == data:
                print("Node deleted is " + str(temp.next.data))
                temp.next = temp.next.next
                return
            temp = temp.next
        print("Node not found")
        return
    
    def sort(self):
        
        current = self.head
        a = [current.data]
        while (current.next):
            current = current.next
            a.append(current.data)

        for i in range(len(a)-1):
            exchange = False
            for j in range(len(a)-i-1):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
                    exchange = True
                if not exchange:
                    break
        k = 0
        temp = self.head
        while k < (len(a)):
            temp.data = a[k]
            temp = temp.next
            k = k + 1
        return self
    
    def remove_dups(self):
        current = self.head
        while (current):
            temp = current
            while (temp.next):
                if (current.data == temp.next.data):
                    temp.next = temp.next.next
                else:
                    temp = temp.next
            current = current.next

    


first_node = Node(11)
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(3)
linked_list.insert(11)
linked_list.insert(6)
linked_list.insert(5)
linked_list.insert(7)
linked_list.insert(5)
print("The Linked List is:")
linked_list.print_list()

linked_list.remove_dups()
print("After removing the duplications, the linked List is:")
linked_list.print_list()