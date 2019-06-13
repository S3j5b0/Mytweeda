

class Node:

    def __init__(self, ID):
        self.ID = ID
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        self.visited = False




class BinarySearchTree:

    def __init__(self, root= None, List= None):
        self.root = None
        self.size = 0

    def insert(self, data):
        self.size = self.size +1
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    """
    insertion metoder til alm insertion der er incremental
    """
    def insertNode(self, ID, node):

        if ID < node.ID:
            if node.leftChild:
                self.insertNode(ID, node.leftChild)
            else:
                node.leftChild = Node(ID)
                node.leftChild.parent = node
        else:
            if node.rightChild:
                self.insertNode(ID, node.rightChild)
            else:
                node.rightChild = Node(ID)
                node.rightChild.parent = node
            # O(N)

    def traverseInSortedOrder(self, node):

        if node.leftChild:
            self.traverseInSortedOrder(node.leftChild)

        print("%s " % node.ID)

        if node.rightChild:
            self.traverseInSortedOrder(node.rightChild)
    def traverse(self):
        if self.root:
            self.traverseInSortedOrder(self.root)

    # looking through tree in dumb order, depthfirst-search style

    def dfs(self):
        current = self.root
        calls = 0
        empty = []
        self.traversedfs(current, calls)


    def traversedfs(self, current, calls):

        if current.visited == False:
            print(current.ID)
            calls = calls + 1

        if calls >= self.size:
            return
        current.visited = True


        if current.leftChild is not None and current.leftChild.visited is False:
            self.traversedfs(current.leftChild, calls)
        elif current.rightChild is not None and current.rightChild.visited is False:
            self.traversedfs(current.rightChild, calls)
        else:
            self.traversedfs(current.parent, calls)


    def search(self, ID):

        current = self.root

        return self.traverseSearch(ID, current)

    def traverseSearch(self, ID, current):

        if current == None: # if we have not found our goal, the current node is null
            return False

        if current.ID == ID: # succes statement
            return True
        if ID > current.ID: # call recursive on left children if data is bigger
            return self.traverseSearch(ID, current.rightChild)

        if ID < current.ID: # call recursive on Right children if data is smaller
            return self.traverseSearch(ID, current.leftChild)










newtree = BinarySearchTree()

newtree.insert(10)
newtree.insert(3)
newtree.insert(0)
newtree.insert(5)
newtree.insert(20)
newtree.insert(10000)
newtree.insert(100)

print(newtree.search(10))


