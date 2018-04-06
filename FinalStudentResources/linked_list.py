class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_tail(self, list_head, val):
        new_node = Node(val)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, list_head, val):
        prev = None
        curr = self.head
        while curr:
            if curr.data == val:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
            elif curr.data != val and curr.next == None:
                print("Could not find the value")
            prev = curr
            curr = curr.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

list1 = LinkedList()
# list1.add_tail(1, "First")
# list1.add_tail(2, "Second")
# list1.add_tail(3, "Third")
#
# list1.print_list()
# list1.remove(1, "Second")
# print ("After removal")
# list1.print_list()
