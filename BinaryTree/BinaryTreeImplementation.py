class Node:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

    def PrintTree(self):
        print(self.data)

class Driverclass:
    if __name__=='__main__':
        node_instance=Node(7)
        node_instance.leftChild=Node(10)
        node_instance.rightChild=Node(15)
        print(node_instance.leftChild.PrintTree())



