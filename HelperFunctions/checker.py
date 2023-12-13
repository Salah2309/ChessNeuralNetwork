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
