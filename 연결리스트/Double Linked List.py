class Node:
    def __init__(self,data,prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def insert_before(self,data,before_data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.head
            while node.data != before_data:
                node = node.next
                if node == None:
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.next = node
            new.prev = before_new
            node.prev = new
            return True
    def insert_after(self,data,after_data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.head
            while node.data != after_data:
                node = node.next
                if node == None:
                    return False
            new = Node(data)
            after_new = node.next
            node.next = new
            new.prev = node
            new.next = after_new
            after_new.prev = new
            return True
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_from_head(self,data):
        if self.head == None:
            return False
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def search_from_tail(self,data):
        if self.head == None:
            return False
        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False


double_linked_list = NodeMgmt(0)
for data in range(1,10):
    double_linked_list.insert(data)

double_linked_list.insert_before(22,3)
double_linked_list.insert_after(33,4)
double_linked_list.desc()