class MyTree:
    def __init__(self, data, parent, layer, check, turn):
        self.data = data
        self.parent = parent
        self.check = check
        self.turn = turn
        self.layer = layer
        self.children = []

    def addChild(self, data, check, turn):
        self.children.append(MyTree(data, self, self.layer + 1, check, turn))

    def print(self):
        for row in self.data:
            for item in row:
                print(f'{item:3}', end=' ')
            print()
            
    def printAll(self):
        #this is a pre-order print
        if self:
            self.print()
            for child in self.children:
                child.printAll()
        else:
            return