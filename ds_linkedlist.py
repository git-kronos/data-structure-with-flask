class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_list(self):
        l = []
        if self.head is None:
            return l
        node = self.head
        while node:
            l.append(node.data)
            node = node.next_node
        return l

    def print_ll(self):
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node
        ll_string += " None"
        print(ll_string)

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
            return

        # if self.last_node is None:
        #     print("last node is none")
        #     node = self.head
        #     # while node.next_node:
        #     #     print('iter', node.data)
        #     #     node = node.next_node
        #     node.next_node = Node(data, Node)
        #     self.last_node = node.next_node
        # else:
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node


ll = LinkedList()
# node5 = Node('data 5', None)
# node4 = Node('data 4', node5)
# node3 = Node('data 3', node4)
# node2 = Node('data 2', node3)
# node1 = Node('data 1', node2)
# ll.head = node1
# ll.print_ll()


# ll.insert_beginning('data 1')
# ll.insert_beginning('data 2')
# ll.insert_beginning('data 3')
# ll.insert_beginning('data 4')
# ll.insert_beginning('data 5')
# ll.print_ll()

# ll.insert_beginning('data 5')
# ll.insert_beginning('data 4')
# ll.insert_beginning('data 3')
# ll.insert_beginning('data 2')
# ll.insert_beginning('data 1')

# ll.insert_at_end('end')
# ll.insert_at_end('end2')
# ll.print_ll()
