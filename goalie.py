import random

def goalie():
  playerscore = 0
  computerscore = 0
  
  print("     ________________________________     ")
  print("     |                              |     ")
  print("     |                              |     ")
  print("     |       Penalty Shootout       |     ")
  print("     |                              |     ")
  print("_____|______________________________|_____")
  print("")
  print("")
  save = input("Where would you like to save?: (TL, BL, M, TR, BR)")
  options=["TL","BL","M","TR","BR"]
  computerOption = random.choice(options)

  #Then we can check if the goal blocked the ball or not
  if save == computerOption:
    print("The shot was blocked!")
    playerscore += 1
  else:
    print("The striker shoots to the " + str(computerOption))
    print("GOAL!")
    computerscore += 1
  
  print("     ________________________________     ")
  print("     |                              |     ")
  print("     |                              |     ")
  print("     |       Penalty Shootout       |     ")
  print("     |                              |     ")
  print("_____|______________________________|_____")
  print("")
  print("")
  #Let the computer decides where it wants the goal to dive
  options=["TL","BL","M","TR","BR"]
  computerOption = random.choice(options)

  #Now let's ask the user where they want to shoot
  shot = input("Where would you like to shoot?: (TL, BL, M, TR, BR)")

  #Then we can check if the goal blocked the ball or not
  if shot == computerOption:
    print("The shot was blocked!")
    computerscore += 1
  else:
    print("The goalie dives to the " + str(computerOption))
    print("GOAL!")
    playerscore += 1
    
  print("     ________________________________     ")
  print("     |                              |     ")
  print("     |                              |     ")
  print("     |       Penalty Shootout       |     ")
  print("     |                              |     ")
  print("_____|______________________________|_____")
  print("")
  print("")
  save = input("Where would you like to save?: (TL, BL, M, TR, BR)")
  options=["TL","BL","M","TR","BR"]
  computerOption = random.choice(options)

  #Then we can check if the goal blocked the ball or not
  if save == computerOption:
    print("The shot was blocked!")
    playerscore += 1
  else:
    print("The striker shoots to the " + str(computerOption))
    print("GOAL!")
    computerscore += 1
  
  print("     ________________________________     ")
  print("     |                              |     ")
  print("     |                              |     ")
  print("     |       Penalty Shootout       |     ")
  print("     |                              |     ")
  print("_____|______________________________|_____")
  print("")
  print("")
  #Let the computer decides where it wants the goal to dive
  options=["TL","BL","M","TR","BR"]
  computerOption = random.choice(options)

  #Now let's ask the user where they want to shoot
  shot = input("Where would you like to shoot?: (TL, BL, M, TR, BR)")

  #Then we can check if the goal blocked the ball or not
  if shot == computerOption:
    print("The shot was blocked!")
    computerscore += 1
  else:
    print("The goalie dives to the " + str(computerOption))
    print("GOAL!")
    playerscore += 1
  
  print("     ________________________________     ")
  print("     |                              |     ")
  print("     |                              |     ")
  print("     |       Penalty Shootout       |     ")
  print("     |                              |     ")
  print("_____|______________________________|_____")
  print("")
  print("")
  save = input("Where would you like to save?: (TL, BL, M, TR, BR)")
  options=["TL","BL","M","TR","BR"]
  computerOption = random.choice(options)

  #Then we can check if the goal blocked the ball or not
  if save == computerOption:
    print("The shot was blocked!")
    playerscore += 1
  else:
    print("The striker shoots to the " + str(computerOption))
    print("GOAL!")
    computerscore += 1
    print("The final score is " + str(playerscore) + " to " + str(computerscore))
  if playerscore > computerscore:
    print("The Player Wins!")
  else:
    print("You Lost :(")