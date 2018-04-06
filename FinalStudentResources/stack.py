class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def isEmpty(self):
        if self.top.next == None:
            return True
        else:
            return False

    def push(self, data):
        new_node = Node(data, self.top)
        self.top = new_node
        self.length += 1


    def pop(self):
        item = self.top.data
        self.top = self.top.next
        self.length -= 1
        return item

    def peek(self):
        return self.top.data

    def size(self):
        return self.length

    def __str__(self):
        str_ret = ""
        current = self.top
        while current:
            curr = str(current.data)
            str_ret += curr
            if current.next:
                str_ret += '\n'
            current = current.next
        return str_ret

s = Stack()
# s.push(1)
# print(s.isEmpty())
# s.push(2)
# s.push(3)
# print(s)
# print("Popped: ", s.pop())
# print(s)
# print("The size is:",s.size())
# print("The top is: ", s.peek())
