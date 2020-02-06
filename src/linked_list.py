class Node:
    def __init__(self, data):
        self.data = data
        self.next_item = None

class LinkedList:
    def __init__(self, list = None):
        self.list = self.create_list(list) if list else []
        self.head = self.list[-1] if list else None

    def create_list(self, list):
        result = []
        if isinstance(list, int) == False:
            for element in list:
                result.append(Node(element))
        else:
            result.append(Node(list))
        return result

    def push(self, data):
        self.list.append(Node(data))
        self.head = self.list[-1]
        self.head.next_item = self.list[-2] if self.size() > 1 else None

    def size(self):
        return len(self.list)

    def pop(self):
        return self.list.pop().data

    def search(self, query):
        for node in self.list:
            if node.data == query:
                return node
        return None

    def remove(self, node):
        self.list.remove(node)

    def display(self):
        return tuple(node.data for node in self.list)[::-1]
