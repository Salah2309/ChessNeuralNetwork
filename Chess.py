

class Tree:
    def __init__(self, data, parent, layer, check, turn):
        self.data = data
        self.parent = parent
        self.check = check
        self.turn = turn
        self.layer = layer
        self.children = []

    def addChild(self, data, check, turn):
        self.children.append(Tree(data, self, self.layer + 1, check, turn))

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

# Helper Functions: # 



# def correctData(data):
#     if data and len(data) == 8:
#         for i in data:
#             if len(i) != 8:
#                 return False
#         return True
#     return False


# #old

# def itemLocation(position, item):
#     location = [2]
#     for y in range(8):
#         for x in range(8):
#             if(item in position[x][y]):
#                 location.append(x)
#                 location.append(y)
#                 return location
#     return None

# def itemExisting(position, item):
#     for y in range(8):
#         for x in range(8):
#             if(item in position[x][y]):
#                 return True
#     return False


# def isOnBoard(x,y):
#     if(x >= 0 and x < 8 and y >= 0 and y < 8):
#         return True
#     return False

# def isPawn(x):
#     if ('p' in x):
#         return True
#     return False

# def isWhite(x):
#     if('w' in x):
#         return True
#     return False

# def isBlack(x):
#     if('b' in x):
#         return True
#     return False


# Main: #
p = [   [ 'BR1' , 'BN1' , 'BB1' , 'BQ' , 'BK' , 'BB2' , 'BN2' , 'BR2'],
                    [ 'BP1' , 'BP2' , 'BP3' , 'BP4' , 'BP5' , 'BP6' , 'BP7' , 'BP8' ],
                    [ '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' ],
                    [ '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' ],
                    [ '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' ],
                    [ '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' ],
                    [ 'WP1' , 'WP2' , 'WP3' , 'WP4' , 'WP5' , 'WP6' , 'WP7' , 'WP8' ],
                    [ 'WR1' , 'WN1' , 'WB1' , 'WQ' , 'WK' , 'WB2' , 'WN2' , 'WR2' ]
                ]


root = Tree(p, None, 0, False, "W")
root.addChild(p, False, "B")
root.addChild(p, False, "B")
root.addChild(p, False, "B")
root.addChild(p, False, "B")
root.addChild(p, False, "B")
root.addChild(p, False, "B")
root.children[0].addChild(p, False, "W")


# To move, we have a function that takes in the Turn and Node
# It goes through until it finds a piece with that color
# It checks if there are legal moves for that piece
# It creates children for the node given with for each legal move, child has played move
# color switch
# return Node

# we can add multi-threding for faster creation. 

# Another Function is a runner that takes in Node after creating it's children
# It creates threads for each child
# It also checks if we are in checkmate or no more children or looped position Node to terminate


def Checker(data, type, y, x):
    Ypos = []
    Xpos = []
    
    #Helper Functions for Checker:
    def Rook(color):
        def ro(axis, postv):
            temp = y if axis == 'y' else x
            while (0 <= temp <= 7):
                temp += 1 if postv else -1
                #out of board
                if temp < 0 or temp > 7:
                    break
                s = data[temp][x] if axis == 'y' else data[y][temp]
                if any(sub in s for sub in ["BR", "BN", "BB", "BQ", "BK", "BP"]):
                    if color == "W":
                        Ypos.append(temp) if axis == 'y' else Ypos.append(y)
                        Xpos.append(x) if axis == 'y' else Xpos.append(temp)
                    break
                if any(sub in s for sub in ["WR", "WN", "WB", "WQ", "WK", "WP"]):
                    if color == "B":
                        Ypos.append(temp) if axis == 'y' else Ypos.append(y)
                        Xpos.append(x) if axis == 'y' else Xpos.append(temp)
                    break
                Ypos.append(temp) if axis == 'y' else Ypos.append(y)
                Xpos.append(x) if axis == 'y' else Xpos.append(temp)
        ro('y', True)
        ro('y', False)
        ro('x', True)
        ro('x', False)
    def Knight(color):
        def ni(ye, ex):
            if 0 <= ye <= 7 and 0 <= ex <= 7:
                s = data[ye][ex]
                if color == "W":
                    if not any(sub in s for sub in ["WR", "WN", "WB", "WQ", "WK", "WP"]):
                        Ypos.append(ye)
                        Xpos.append(ex)
                if color == "B":
                    if not any(sub in s for sub in ["BR", "BN", "BB", "BQ", "BK", "BP"]):
                        Ypos.append(ye)
                        Xpos.append(ex)
        ni(y+2, x+1)
        ni(y+2, x-1)
        ni(y+1, x+2)
        ni(y+1, x-2)
        ni(y-1, x+2)
        ni(y-1, x-2)
        ni(y-2, x+1)
        ni(y-2, x-1)
    def Bischop(color):
        def bi(isY, isX):
            tY = y
            tX = x
            while(0 <= tY <= 7 and 0 <= tX <= 7):
                tY += 1 if isY else -1
                tX += 1 if isX else -1
                #out of board
                if tY < 0 or tY > 7 or tX < 0 or tX > 7:
                    break
                s = data[tY][tX]
                if any(sub in s for sub in ["BR", "BN", "BB", "BQ", "BK", "BP"]):
                    if color == "W":
                        Ypos.append(tY)
                        Xpos.append(tX)
                    break
                if any(sub in s for sub in ["WR", "WN", "WB", "WQ", "WK", "WP"]):
                    if color == "B":
                        Ypos.append(tY)
                        Xpos.append(tX)
                    break
                Ypos.append(tY)
                Xpos.append(tX)
        bi(True, True)
        bi(True, False)
        bi(False, True)
        bi(False, False)
    def King(color):
        def ki(ye, ex):
            if 0 <= ye <= 7 and 0 <= ex <= 7:
                s = data[ye][ex]
                if color == "W":
                    if not any(sub in s for sub in ["WR", "WN", "WB", "WQ", "WK", "WP"]):
                        Ypos.append(ye)
                        Xpos.append(ex)
                if color == "B":
                    if not any(sub in s for sub in ["BR", "BN", "BB", "BQ", "BK", "BP"]):
                        Ypos.append(ye)
                        Xpos.append(ex)
        ki(y+1, x+1)
        ki(y+1, x)
        ki(y+1, x-1)
        ki(y, x+1)
        ki(y, x-1)
        ki(y-1, x+1)
        ki(y-1, x)
        ki(y-1, x-1)        
    
    #Main Functions
    if type == "BR":
        Rook("B")
    elif type == "BN":
        Knight("B")
    elif type == "BB":
       Bischop("B")
    elif type == "BQ":
        Rook("B")
        Bischop("B")
    elif type == "BK":
        King("B")
    elif type == "BP":
        pass
    
    
    elif type == "WR":
        Rook("W")
    elif type == "WN": 
        Knight("W")
    elif type == "WB":
        Bischop("W")
    elif type == "WQ":
        Rook("W")
        Bischop("W")
    elif type == "WK":
        King("W")
    elif type == "WP":
        pass
    
    
    else:
        raise Exception("Wrong type passed to Checker()")
    
    for i in range(len(Ypos)):
        print(Ypos[i], Xpos[i])
    return (Ypos, Xpos)


def Creater(Node, Turn):
    childTurn = "B" if Turn == "W" else "W"
    
    if Node.check:
        pass
    else:
        pass
    
    
    return
x = Checker(root.data, "BK", 3, 3)


#Creater(root, 'W')
#root.printAll()