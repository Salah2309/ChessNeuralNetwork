from HelperFunctions.tree import MyTree
from HelperFunctions.checker import Checker


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


root = MyTree(p, None, 0, False, "W")
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

def Creater(Node, Turn):
    childTurn = "B" if Turn == "W" else "W"
    
    if Node.check:
        pass
    else:
        pass
    
    
    return

x = Checker(root, "BP", 1, 1)


#Creater(root, 'W')
#root.printAll()