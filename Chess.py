from pathlib import Path

class Tree:
    def __init__(self, data, layer):
        self.data = data
        self.layer = layer
        self.children = []

    def addChild(self, data):
        self.children.append(Tree(data, self.layer + 1))

    def print(self):
        for row in self.data:
            for item in row:
                print(f'{item:3}', end=' ')
            print()

    def printChildren(self):
        for i in range(len(self.children)):
            print("child: " +str(i))
            self.children[i].print()
            print()
            
    def printAll(self):
        #this is a pre-order print
        if self:
            self.print()
            for child in self.children:
                child.printAll()
        else:
            return

# Helper Functions: # 

def correctData(data):
    if data and len(data) == 8:
        for i in data:
            if len(i) != 8:
                return False
        return True
    return False


#old

def itemLocation(position, item):
    location = [2]
    for y in range(8):
        for x in range(8):
            if(item in position[x][y]):
                location.append(x)
                location.append(y)
                return location
    return False

def itemExisting(position, item):
    for y in range(8):
        for x in range(8):
            if(item in position[x][y]):
                return True
    return False


def isOnBoard(x,y):
    if(x >= 0 and x < 8 and y >= 0 and y < 8):
        return True
    return False

def isPawn(x):
    if ('p' in x):
        return True
    return False

def isWhite(x):
    if('w' in x):
        return True
    return False

def isBlack(x):
    if('b' in x):
        return True
    return False


# Main: #
p = [   [ 'br1' , 'bn1' , 'bb1' , 'bq' , 'bk' , 'bb2' , 'bn2' , 'br2'],
                    [ 'bp1' , 'bp2' , 'bp3' , 'bp4' , 'bp5' , 'bp6' , 'bp7' , 'bp8' ],
                    [ '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' ],
                    [ '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' ],
                    [ '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' ],
                    [ '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' ],
                    [ 'wp1' , 'wp2' , 'wp3' , 'wp4' , 'wp5' , 'wp6' , 'wp7' , 'wp8' ],
                    [ 'wr1' , 'wn1' , 'wb1' , 'wq' , 'wk' , 'wb2' , 'wn2' , 'wr2' ]
                ]


root = Tree(p, 0)
root.addChild(p)
root.addChild(p)
root.addChild(p)
root.addChild(p)
root.addChild(p)
root.addChild(p)
root.children[0].addChild(p)
root.children[0].addChild(p)
root.children[0].addChild(p)
root.children[1].addChild(p)
root.children[2].addChild(p)
root.children[2].addChild(p)
root.children[2].addChild(p)
root.children[2].addChild(p)
root.children[2].addChild(p)
root.children[2].children[0].addChild(p)
root.children[2].children[0].addChild(p)
root.children[2].children[1].addChild(p)
root.children[2].children[2].addChild(p)
root.children[2].children[2].addChild(p)
root.printAll()


