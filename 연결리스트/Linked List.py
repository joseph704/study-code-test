class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)

    def add(self,data):
        if self.head == "":
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

linkedlist1 = NodeMgmt(0)
for data in range(1,10):
    linkedlist1.add(data)
linkedlist1.desc()