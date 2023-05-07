
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
        for row in self.position:
            for item in row:
                pass



root = Tree()
root.position = [   [ 'br' , 'bn' , 'bb' , 'bq' , 'bk' , 'bb' , 'bn' , 'br'],
                    [ 'bp' , 'bp' , 'bp' , 'bp' , 'bp' , 'bp' , 'bp' , 'bp' ],
                    [ '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' ],
                    [ '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' ],
                    [ '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' ],
                    [ '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' ],
                    [ 'wp' , 'wp' , 'wp' , 'wp' , 'wp' , 'wp' , 'wp' , 'wp' ],
                    [ 'wr' , 'wn' , 'wb' , 'wq' , 'wk' , 'wb' , 'wn' , 'wr' ]
                ]

root.print()