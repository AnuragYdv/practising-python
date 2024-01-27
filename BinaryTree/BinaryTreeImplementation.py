class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if data < self.data:
            if self.leftChild:
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return
        else:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return

    def search(self, val):
        if val == self.data:
            return str(val) + "is found "
        elif val < self.data:
            if self.leftChild:
                return self.leftChild.search(val)
            else:
                return "no " + val + " found in BST"
        else:
            if self.rightChild:
                return self.rightChild.search(val)
            else:
                return "no " + val + " found in BST"

    def print_tree(self):

        if self.leftChild:
            self.leftChild.print_tree()
        print(self.data)
        if self.rightChild:
            self.rightChild.print_tree()




class DriverClass:
    if __name__ == '__main__':
        root = Node(100)
        root.insert(10)
        root.insert(20)
        root.insert(30)
        root.insert(40)
        root.insert(50)
        root.insert(60)
        root.insert(110)
        root.insert(120)
        root.insert(130)
        root.insert(125)
        root.insert(115)
        print(root.print_tree())
        # print(root.search(115))
