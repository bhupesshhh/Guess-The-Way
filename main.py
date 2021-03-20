import random


# Set The Initial Game Values
game_on = False

# Stage Jungle
def jungle():
  global game_on
  print("Welcome to Jungle")
  jun = ["pass","jump"]
  ans = input("Would you pass through or jump around the jungle? (pass/jump) ")
  jungle_answer = random.choice(jun)

  # Check for the answer
  if ans.lower() == jungle_answer:
    game_on = True
    print("Right guess, your choice is correct!")
  else:
    game_on = False
    print("Wrong guess, your choice is incorrect!")

# Stage Hill
def hill():
  global game_on
  print("Welcome to Hill")
  hil = ["pass","jump"]
  ans = input("Would you pass through or jump around the hill? (pass/jump) ")
  hill_answer = random.choice(hil)

  # Check for the answer
  if ans.lower() == hill_answer:
    game_on = True
    print("Right guess, your choice is correct!")
  else:
    game_on = False
    print("Wrong guess, your choice is incorrect!")

# Stage River
def river():
  global game_on
  print("Welcome to River")
  riv = ["swim","ride"]
  ans = input("Would you swim through or ride across the river? (swim/ride) ")
  river_answer = random.choice(riv)

  # Check for the answer
  if ans.lower() == river_answer:
    game_on = True
    print("Right guess, your choice is correct!")
  else:
    game_on = False
    print("Wrong guess, your choice is incorrect!")

# Stage Lake 
def lake():
  global game_on
  print("Welcome to lake")
  lak = ["swim","pass"]
  ans = input("Would you pass through or swim across the lake? (pass/swim) ")
  lake_answer = random.choice(lak)

  #Check for the answer
  if ans.lower() == lake_answer:
    game_on = True
    print("Right guess, your choice is correct!") 
  else:
    game_on = False
    print("Wrong guess, your choice is incorrect!")

# Gameplay 
print("Welcome to this word game called..\n")
print("GUESS THE WAY!!!\n")
name = input("What is your name? ")
age = int(input("What is your age? "))
print(f"\nHello {name}, you are {age} years old.")

# Start the Game
if age > 10:
  print("You are eligible to play the game.\n")
  gameplay = input("Do you wanna play the game? (yes/no) ")

  # Check for the answer
  if gameplay.lower() == 'yes':
    print("Let's start the game.\n")
    game_on = True
    gameplay = True
  else:
    print("We hope to see you soon.") 
else:
	print("You are not eligible to play the game.")


# Game Initiation Measures
stage = [lake,jungle,river,hill]

# Gameplay
while gameplay:

  points = 0
  round = 0

  while game_on:
    print(f"Round: {round}")

    stage_play = random.choice(stage)
    stage_play()

    if game_on == False:
      break
    else:
      points += 10

    print(f"Score:{points}\n")
    round += 1

    if round == 20:
      game_on = False
      print("You won the game!")
      break

  # Final Gameplay Scores
  print("\n")
  print(f"Thanks for joining {name}.")
  if round < 20:
    print(f"You comepletd {round} rounds.")
  else:
    print("You comepleted all rounds.")
  print(f"Your final score is {points}\n")

  replay = input("Do you want to play again? (yes/no) ")
  if replay == "yes":
    gameplay = True
    game_on = True
    print("\n")
  else:
    gameplay = False

print("Thanks for playing the game!")