#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
from art import logo
print(logo)

def selected_num():
  num = random.randrange(1,101)
  return num
comp_num = selected_num()
print(comp_num)
chance = 0
def diff_on():
  global chance
  dif = input("Please enter Difficulty 'Hard' or 'Easy' : ").lower()
  if dif == "hard":
    chance = 5
  elif dif == "easy":
    chance = 10
  else:
    print("Please enter proper input")
    diff_on()
def game_on():
  # Allow the player to submit a guess for a number between 1 and 100.
  global chance
  guessed_num = int(input("Enter Number between 1 to 100: "))
  # print(selected_num())
  
  
  # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
  if chance == 0:
    print("You have exausted your chances")
  elif comp_num > guessed_num:
    print(f"Too Low")
    print(f"Guess Again")
    chance -= 1
    print(f"You have {chance} attempts.")
    game_on()
  elif comp_num == guessed_num:
    print(f"You predicted right . Number is {comp_num}")
  elif comp_num < guessed_num:
    print(f"Too High")
    print(f"Guess Again")
    chance -= 1
    print(f"You have {chance} attempts.")
    game_on()
  # If they got the answer correct, show the actual answer to the player.
  # Track the number of turns remaining.
  # If they run out of turns, provide feedback to the player. 
  # Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
diff_on()
game_on()