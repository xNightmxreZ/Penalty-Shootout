#Isiah Williams
#Coding For All-P6
#Mr. Burns

import random
import striker
import goalie

computerscore = 0
playerscore = 0

position = input("Would you like to play as the goalie first or the striker first?: ")

if position == "striker":
  striker.striker()
else:
  goalie.goalie()