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
