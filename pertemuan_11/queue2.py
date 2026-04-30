class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, data):
        new_node = node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        removed_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return removed_data

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data
        
    def display(self):
        if self.is_empty():
            return None
        current = self.head
        value = []
        while current:
            value.append(current.data)
            current = current.next
        return value