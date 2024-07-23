# type: ignore
"""
Copyright © Jason Yang 2024   All right reserved.
<Python: Tic-Tac-Toe VS Computer>
Copyright © 2024 by Jason Yang is licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
"""
import random
TicTacToe_Table = []
for index in range(9):
  TicTacToe_Table.append(index + 1)
ValidInput = list(TicTacToe_Table)
UserInput = []
ComputerInput = []
Entered_ValidInput = False
while Entered_ValidInput is False:
  Difficulty = input("Choice Difficulty of the game (\033[1;32mNORMAL\033[0m / \033[1;31mEXTREME\033[0m): ")
  if Difficulty == "NORMAL" or Difficulty == "EXTREME": Entered_ValidInput = True
  else: print("\033[1;31mPlease enter a valid input! \033[0m(\033[1;32mNORMAL\033[0m / \033[1;31mEXTREME\033[0m)")
while True:
  print(TicTacToe_Table)
  print(ValidInput)
  Entered_ValidInput = False
  while Entered_ValidInput == False:
    UserMove = input("\033[0mTake your move: ")
    if not UserMove.isdigit():
      print("\033[1;31mPlease enter a valid input! You should only enter number instead of other characters. The number represent the the move that is available in the table! ", end = "")
      print(ValidInput)
    elif int(UserMove) not in ValidInput:
      print("\033[1;31mPlease enter a valid input! You should only take the move that is available in the table! ", end = "")
      print(ValidInput)
    else: Entered_ValidInput = True
  TicTacToe_Table[int(UserMove) - 1] = "X"
  ValidInput.remove(int(UserMove))
  UserInput.append(int(UserMove))
  Dict_WinCondition = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],\
                       [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
  if len(ValidInput) == 0:
    print(TicTacToe_Table)
    print("DRAW!!!")
    exit()
  for index in range(len(Dict_WinCondition)):
    if len([x for x in UserInput if x in Dict_WinCondition[index]]) == 3:
      print(TicTacToe_Table)
      print("YOU WIN!!!")
      exit()
  def ComputerMove(number):
    TicTacToe_Table[number - 1] = "○"
    ValidInput.remove(number)
    ComputerInput.append(number)
    for index in range(len(Dict_WinCondition)):
      if len([x for x in ComputerInput if x in Dict_WinCondition[index]]) == 3:
        print(TicTacToe_Table)
        print("COMPUTER WIN!!!")
        exit()
  if len(ValidInput) == 8 and Difficulty == "NORMAL": ComputerMove(random.choice([x for x in [2, 4, 6, 8] if x not in UserInput]))
  elif len(ValidInput) == 8 and 5 in ValidInput and Difficulty == "EXTREME": ComputerMove(5)
  elif len(ValidInput) == 8 and 5 not in ValidInput and Difficulty == "EXTREME": ComputerMove(random.choice([1, 3, 7, 9]))
  else:  
    for index in range(8):
      CheckList = [len([x for x in UserInput if x in Dict_WinCondition[index]]),
                   len([x for x in ComputerInput if x in Dict_WinCondition[index]])]
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
