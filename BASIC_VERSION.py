# type: ignore
"""
Copyright © Jason Yang 2024   All right reserved.
<Python: Tic-Tac-Toe VS Computer>
Copyright © 2024 by Jason Yang is licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
"""
## Step 1: Game Board Initialization
import random, time

TicTacToe_Table = []
for index in range(9):
  TicTacToe_Table.append(index + 1)
# ValidInput = TicTacToe_Table
ValidInput = list(TicTacToe_Table)
UserInput = []
ComputerInput = []

print("\033[1m╔════════════════════════════════════════════════╗")
print("\033[1m║          Welcome to Tic Tac Toe Game!          ║")
print("\033[1m║\033[1;32m  Let's play Tic-Tac-Toe against the computer!  \033[1;37m║")
print("\033[1m╚════════════════════════════════════════════════╝\n")

print("\033[0m┌────────────────────────────────────────────────┐")
print("│ \033[1mIntroduction of the game:\033[0m                      │")
print("│ You probably already know how to play Tic-Tac- │")
print("│ Toe. It's a really simple game, right? That's  │")
print("│ what most people think.                        │")
print("│                                                │")
print("│ But if you really wrap your brain around it,   │")
print("│ you'll discover that Tic-Tac-Toe isn't quite   │") 
print("│ as simple as you think!                        │")
print("│                                                │")
print("│ \033[1mRules of the Games:\033[0m                            │")
print("│ 1. The game is played on a grid that's 3       │")
print("│    squares.                                    │")
print("│ 2. \033[1;34mYou are X, \033[1;31mThe computer is ○. \033[0mPlayers take  │")
print("│    turns putting their marks in empty squares. │")
print("│ 3. The first player to get 3 of her marks in a │")
print("│    row (up, down, across, or diagonally) is    │")
print("│    the winner.                                 │")
print("│ 4. When all 9 squares are full, the game is    │")
print("│    over. If no player has 3 marks in a row,    │")
print("│    the game ends in a draw.                    │")
print("└────────────────────────────────────────────────┘\n")

print("┌────────────────────────────────────────────────┐")
print("│ \033[1mDifficulty of the game:\033[0m                        │")
print("│ 1. \033[1;32mNORMAL\033[0;32m: The Logic of Computer has mistakes,\033[0m │")
print("│    \033[0;32mit is not that hard to beat computer!\033[0m       │")
print("│ 2. \033[1;31mEXTREME\033[0;31m: The Logic of Computer Move is\033[0m      │")
print("│    \033[0;31mperfect. player cannot win under this mode,\033[0m │")
print("│    \033[0;31mplayer can try to get DRAW in the mode.\033[0m     │")
print("└────────────────────────────────────────────────┘\n")

Entered_ValidInput = False
while Entered_ValidInput is False:
  Difficulty = input("Choice Difficulty of the game (\033[1;32mNORMAL\033[0m / \033[1;31mEXTREME\033[0m): ")
  if Difficulty == "NORMAL" or Difficulty == "EXTREME": Entered_ValidInput = True
  else: print("\033[1;31mPlease enter a valid input! \033[0m(\033[1;32mNORMAL\033[0m / \033[1;31mEXTREME\033[0m)")

print("\033[1;31m\n                PREPARE TO START!                 ", end="")
time.sleep(1)
print("\r                       3...                       ", end="")
time.sleep(1)
print("\r                       2...                       ", end="")
time.sleep(1)
print("\r                       1...                       ", end="")
time.sleep(1)
print("\r                  STARTING GAME!                  ")
print("══════════════════════════════════════════════════\033[0m")

def DisplayGameBoard():
  global TicTacToe_Table
  print("\n┌───┬───┬───┐")
  print("│", TicTacToe_Table[0], "│", TicTacToe_Table[1], "│", TicTacToe_Table[2], "│")
  print("├───┼───┼───┤")
  print("│", TicTacToe_Table[3], "│", TicTacToe_Table[4], "│", TicTacToe_Table[5], "│")
  print("├───┼───┼───┤")
  print("│", TicTacToe_Table[6], "│", TicTacToe_Table[7], "│", TicTacToe_Table[8], "│")
  print("└───┴───┴───┘")

def DisplayValidInput():
  global ValidInput
  print("Your Valid Move: ", end="")
  for index in range(len(ValidInput)):
    if index != len(ValidInput) - 1: print(str(ValidInput[index]) + ", ", end="")
    else: print(ValidInput[index])

while True:
  ## Step 2: Game Board Display
  # print(TicTacToe_Table)
  DisplayGameBoard()
  ## Step 3: Check all valid moves
  DisplayValidInput()

  ## Step 4: Player Move "X"
  Entered_ValidInput = False
  while Entered_ValidInput == False:
    UserMove = input("\033[0mTake your move: ")
    if not UserMove.isdigit():
      print("\033[1;31mPlease enter a valid input! You should only enter number instead of other characters. The number represent the the move that is available in the table! ", end = "")
      DisplayValidInput()
    elif int(UserMove) not in ValidInput:
      print("\033[1;31mPlease enter a valid input! You should only take the move that is available in the table! ", end = "")
      DisplayValidInput()
    else: Entered_ValidInput = True

  TicTacToe_Table[int(UserMove) - 1] = "X"
  ValidInput.remove(int(UserMove))
  UserInput.append(int(UserMove))

  ## Check Win Condition
  Dict_WinCondition = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],\
                       [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

  if len(ValidInput) == 0:
    DisplayGameBoard()
    print("DRAW!!!")
    exit()
  for index in range(len(Dict_WinCondition)):
    if len([x for x in UserInput if x in Dict_WinCondition[index]]) == 3:
      DisplayGameBoard()
      print("YOU WIN!!!")
      exit()

  ## Step 5: Computer Move & Logic Process "O"
  def ComputerMove(number):
    TicTacToe_Table[number - 1] = "○"
    ValidInput.remove(number)
    ComputerInput.append(number)
    for index in range(len(Dict_WinCondition)):
      if len([x for x in ComputerInput if x in Dict_WinCondition[index]]) == 3:
        DisplayGameBoard()
        print("COMPUTER WIN!!!")
        exit()
  
  if len(ValidInput) == 8 and Difficulty == "NORMAL":
    ComputerMove(random.choice([x for x in [2, 4, 6, 8] if x not in UserInput]))
  elif len(ValidInput) == 8 and 5 in ValidInput and Difficulty == "EXTREME":
    ComputerMove(5)
  elif len(ValidInput) == 8 and 5 not in ValidInput and Difficulty == "EXTREME":
    ComputerMove(random.choice([1, 3, 7, 9]))
  else:  
    for index in range(8):
      CheckList = [len([x for x in UserInput if x in Dict_WinCondition[index]]), len([x for x in ComputerInput if x in Dict_WinCondition[index]])]
      PriorityMove = [x for x in Dict_WinCondition[index] if x not in ComputerInput and x not in [1, 3, 7, 9]]
      if CheckList == [0, 2]:
        ComputerMove([x for x in Dict_WinCondition[index] if x not in ComputerInput][0])
        break
      elif CheckList == [2, 0]:
        ComputerMove([x for x in Dict_WinCondition[index] if x not in UserInput][0])
        break
      elif CheckList == [0, 1] and PriorityMove:
        ComputerMove(random.choice(PriorityMove))
        break
      elif index == 7: ComputerMove(random.choice(ValidInput))
