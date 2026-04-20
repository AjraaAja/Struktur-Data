class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_list(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

    def delete_list(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                if temp == self.head:
                    self.head = temp.next
                else:
                    temp.next = temp.next.next
                print("Data berhasil dihapus")
                break
            temp = temp.next
        print("Data tidak ditemukan")

    def search_list(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                print("Data ditemukan")
                break
            temp = temp.next
        print("Data tidak ditemukan")


ll = LinkedList()
ll.add_list(30)
print("Print LinkedList")
ll.display()

ll.add_list(20)
ll.add_list(10)
print("\nPrint LinkedList")
ll.display()

ll.delete_list(10)
print("\nPrint LinkedList")
ll.display()