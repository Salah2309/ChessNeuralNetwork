def Checker(Node, piece, y, x):
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
                s = Node.data[temp][x] if axis == 'y' else Node.data[y][temp]
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
                s = Node.data[ye][ex]
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
                s = Node.data[tY][tX]
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
                s = Node.data[ye][ex]
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
    def Pawn(color):
        #Pos Moves: corner take, empeson
        #One Up:
        ye = y-1 if color == "W" else y+1
        if 0 <= ye <= 7:
            s = Node.data[ye][x]
            if color == "W":
                if not any(sub in s for sub in ["WR", "WN", "WB", "WQ", "WK", "WP"]):
                    Ypos.append(ye)
                    Xpos.append(x)
            if color == "B": 
                if not any(sub in s for sub in ["BR", "BN", "BB", "BQ", "BK", "BP"]):
                    Ypos.append(ye)
                    Xpos.append(x)
        #Two Up:
        if color == "W" and y == 6:
            s = Node.data[y-2][x]
            if not any(sub in s for sub in ["WR", "WN", "WB", "WQ", "WK", "WP"]):
                Ypos.append(y-2)
                Xpos.append(x)
        if color == "B" and y == 1:
            s = Node.data[y+2][x]
            if not any(sub in s for sub in ["BR", "BN", "BB", "BQ", "BK", "BP"]):
                Ypos.append(y+2)
                Xpos.append(x)
        


    #Main Functions
    if piece == "BR":
        Rook("B")
    elif piece == "BN":
        Knight("B")
    elif piece == "BB":
       Bischop("B")
    elif piece == "BQ":
        Rook("B")
        Bischop("B")
    elif piece == "BK":
        King("B")
    elif piece == "BP":
        Pawn("B")
    
    
    elif piece == "WR":
        Rook("W")
    elif piece == "WN": 
        Knight("W")
    elif piece == "WB":
        Bischop("W")
    elif piece == "WQ":
        Rook("W")
        Bischop("W")
    elif piece == "WK":
        King("W")
    elif piece == "WP":
        Pawn("W")


    else:
        raise Exception("Wrong piece passed to Checker()")
    
    for i in range(len(Ypos)):
        print(Ypos[i], Xpos[i])
    return (Ypos, Xpos)
