import math
import random

class Minesweeper:
   def marker(self, dimension):
    if (random.randrange(1000) % dimension) == 0:
        return '*'
    else:
        return ' '
   def __init__(self, dim):
      self.board = []
      for x in range(dim):
         tmp = []
         for y in range(dim):
            tmp.append(self.marker(dim))
         self.board.append(tmp)
   def displayLine(self, board):
      dim = len(board)
      print("----|", end = "")
      for x in range(dim):
         print("---|", end="")
      print()
   def displayBoard(self, hide = False):
      dim = len(self.board)
      print("      ", end = "")
      for y in range(dim):
         print(chr(ord('A')+y), end =" | ")
      print()
      self.displayLine(self.board)
      for x in range(dim):
         print("%3d |" % x, end=" ")
         for y in range(dim):
            if hide and self.board[x][y] == '*':
               print(' ', end = " | ")
            else:
               print(self.board[x][y], end = ' | ')
         print()
         self.displayLine(self.board)
   def makeMove(self,move):
      dim = len(self.board)
      moves = move.split(",")
      x = ord(moves[0])-ord('A')
      if x<0 or x >= dim:
         print("Move \"%s\" is out of range" % move)
         return True
      y = int(moves[1])
      if y<0 or y >= dim:
         print("Move \"%s\" is out of range" % move)
         return True
      if self.board[y][x] == "*":
         print("*****************************")
         print("******** B O O M ! **********")
         print("*****************************")
         return False
      self.setValue(y, x)
      return True
   def winner(self):
      dim = len(self.board)
      for x in range(dim):
         for y in range(dim):
            if self.board[x][y] == ' ':
               return False
      print("***********************************")
      print("********** W I N N E R ! **********")
      print("***********************************")
      return True
   def setValue(self, y, x):
      dim = len(self.board)
      count = 0
      if y-1 >= 0:
         if self.board[y-1][x] == '*':
            count += 1
      if y+1 < dim:
         if self.board[y+1][x] == '*':
            count += 1
      if x-1 >= 0:
         if self.board[y][x-1] == "*":
            count += 1
      if x+1 < dim:
         if self.board[y][x+1] == '*':
            count += 1
      if y-1 >= 0 and x-1 >= 0:
         if self.board[y-1][x-1] == '*':
            count += 1
      if y+1 < dim and x+1 < dim:
         if self.board[y+1][x+1] == '*':
            count += 1
      if y-1 >= 0 and x+1 < dim:
         if self.board[y-1][x+1] == '*':
            count += 1
      if y+1 < dim and x-1 >= 0:
         if self.board[y+1][x-1] == '*':
            count += 1
      self.board[y][x] = str(count)

def main():
    random.seed(0)
    size = 99999
    while size > 0:
        size = int(input("What size board do you want (3-15, enter 0 to stop)? "))
        print(size)
        if (size > 2) and (size < 16):
            game = Minesweeper(size)
            game.displayBoard(hide=True)
            move = "not empty"
            while move != "":
                move = input("Enter coordinate (e.g. \"A,15\") or empty string to stop: ")
                print(move)
                if len(move) > 0:
                    if game.makeMove(move):
                        if game.winner():
                            game.displayBoard(hide=False)
                            break
                        else:
                            game.displayBoard(hide=True)
                    else:
                        game.displayBoard(hide=False)
                        break
            for x in range(10):
               print()
            print("*****************************")
            print("******** NEW GAME! **********")
            print("*****************************")
        elif (size < 0) or (size in [1,2]) or (size > 15):
            print("Please pay attention!")
            size = 999999
if __name__ == "__main__":
    main()
