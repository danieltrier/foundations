import random

while True:
  player_number = int(input("Whats your number?"))
  random_number = random.randint(1,100)
  if player_number == random_number:
    print("it is a tie")
  elif player_number > random_number:
    print("You win")
  elif player_number < random_number:
    print("You loose")
  user_input =input("Do you want to play again? (YES o NO): ")
  if user_input == "NO":
    break
  else:
    continue
  

  a = "b"
  

