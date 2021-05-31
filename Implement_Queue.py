class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self,data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last.next.prev = self.last
            self.last = self.last.next

    def dequeue(self,data):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    def first(self):
        return self.head.data

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def printqueue(self):
        temp = self.head
        while temp is not None:
            print("temp.data")
            temp = temp.next
