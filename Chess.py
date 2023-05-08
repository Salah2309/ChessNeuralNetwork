
class Tree:
    def __init__(self):
        self.position = [[8]*8]
        self.children = []

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

    def print(self):
        for row in self.position:
            for item in row:
                print(f'{item:3}', end=' ')
            print()
            
    def NumPossibleMoves(self, color):
        inCheck(self.position, "w")
        


# Helper Functions: # 

def inCheck(position, color):
    king = color + 'k'
    if(not itemExisting(position, king)):
        raise Exception("Check on King's existance OR Color Passed to inCheck Function")
    else:
        # in check deal with here
        pass


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

root = Tree()
root.position = [   [ 'br1' , 'bn1' , 'bb1' , 'bq' , 'bk' , 'bb2' , 'bn2' , 'br2'],
                    [ 'bp1' , 'bp2' , 'bp3' , 'bp4' , 'bp5' , 'bp6' , 'bp7' , 'bp8' ],
                    [ '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' ],
                    [ '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' ],
                    [ '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' ],
                    [ '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' ],
                    [ 'wp1' , 'wp2' , 'wp3' , 'wp4' , 'wp5' , 'wp6' , 'wp7' , 'wp8' ],
                    [ 'wr1' , 'wn1' , 'wb1' , 'wq' , 'wk' , 'wb2' , 'wn2' , 'wr2' ]
                ]
root.NumPossibleMoves('white')


