class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)

    def add(self,data):
        if self.head == '':
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

    def delete(self,data):
# 헤드가 없을 시
        if self.head == '':
            print("해당 값을 가진 노드가 없습니다")
            return

# 헤드를 지우는 경우
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
# 중간 또는 마지막에 있는 노드를 지우는 경우
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node=node.next

linkedlist1 = NodeMgmt(0)
for data in range(1,10):
    linkedlist1.add(data)
linkedlist1.desc()
