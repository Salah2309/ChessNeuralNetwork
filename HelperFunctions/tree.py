class MyTree:
    def __init__(self, data, parent, layer, check, turn):
        #data: [8][8]
        self.data = data
        #parent: MyTree()
        self.parent = parent
        #check: True / False
        self.check = check
        #turn: "W" / "B"
        self.turn = turn
        #layer = number
        self.layer = layer
        #children: [] of MyTree()
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