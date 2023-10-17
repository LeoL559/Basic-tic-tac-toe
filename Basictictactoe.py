board = [ ["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"] ]

for li in board:
    print(li)
col=0
row=0
playerTurn = "X"
for counter in range(1,10):
   while True:
     col = 0
     row = 0
     while (col < 1 or col > 3):
       col = int(input(playerTurn + " player, select a column 1-3: "))
       if (col < 1 or col > 3):
         print("The column must be between 1 and 3.")
     while (row < 1 or row > 3):
       row = int(input(playerTurn + " player, select a row 1-3: "))
       if (row < 1 or row > 3):
         print("The row must be between 1 and 3.")
     col -= 1
     row -= 1
     if board[row][col] == '-':
       board[row][col] = playerTurn
       break #here is the break statement that addresses Item 2
     else:
       print("Oops, that spot was already taken. Please select another spot.")
   print(board[0])
   print(board[1])
   print(board[2])
   if playerTurn =="X":
     playerTurn="O"
   else:
     playerTurn="X"