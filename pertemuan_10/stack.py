#membuat stack dengan linked list
#1. kelas Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#2. kelas Stack
class Stack:
    def __init__(self):
        self.head = None
    #method untuk menambahkan data ke stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    #method untuk menghapus data dari stack
    def pop(self):
        if not self.head:
            return None
        temp = self.head
        self.head = self.head.next
        return temp.data
    #method untuk mengecek apakah stack kosong
    def is_empty(self):
        return self.head is None
    #method untuk melhat stack teratas
    def peek(self):
        if not self.head:
            return None
        return self.head.data
    #method untuk menampilkan seluruh isi stack
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
    
#penggunaan
mystack = Stack()
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.display()
mystack.pop()
mystack.display()
print(mystack.is_empty())
print(mystack.peek())    