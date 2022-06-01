# Penalty Shootout - www.101computing.net/penalty-shootout/
import random

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
else:
  print("The goalie dives to the " + str(computerOption))
  print("GOAL!")
