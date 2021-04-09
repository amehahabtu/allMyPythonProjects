
nums=[1,2,3,4,5,6]
new_nums=[]
for num in nums:
    new_nums.append(num*num)
print(new_nums)

new_numstwo=[num*num for num in nums]
print(new_numstwo)

new_numthree=list(map(lambda num :num*num,nums))
print(new_numthree)

squares =[ i**2 for i in range(1,11)] # to create new list with squared value of original list using list comprehension method. 
print(squares)

square = list(map(lambda x : x**2 , [i for i in range(1,11)]))
print(square)

twos = [ 2**i for i in range(1,11)]
print(twos)
get odd numbers from squares 
odds= [num for num in squares if num%2 ==1]  # or if num%2 !=0 to get odd number
print(odds)
#The chess board skeleton 
from pprint import pprint
chess_board =[]
for i in range(1,9):
    row =[i for i in range(1,9)]
    chess_board.append(row)
pprint(chess_board)
# nested list comprehension 
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
board=[[i for i in range(1,9)] for i in range(1,5)]
pprint(board)
# The chess game starts here --------------------------------------------------------------
from pprint import pprint
EMPTY='_'
Chess_Board = []
ROOK='ROOK'
# for i in range (8):
#     row = [EMPTY for i in range(8)]
#     Chess_Board.append(row)
Chess_Board=[[EMPTY for i in range(8)] for i in range(8)]
Chess_Board[0][0]=ROOK
Chess_Board[0][7]=ROOK
Chess_Board[7][0]=ROOK
Chess_Board[7][7]=ROOK
Chess_Board[4][4]='Eldana'
Chess_Board[6][3]='Daniela'
Chess_Board[0][6]='Mida'
Chess_Board[2][5]='Ameha'
print('Welcome to chess game !!!\n')
pprint(Chess_Board)
    

