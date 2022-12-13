rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player = int(input("Rock = 0, Paper = 1, Scissors = 2.\nType Selection: "))
rps = [0, 1, 2]
computer = random.choice(rps)



if player == 0 and computer == 0:
  print(f'\nPlayer\n{rock}\nComputer\n{rock}\nDRAW!')
elif player == 1 and computer == 1:
  print(f'\nPlayer\n{paper}\nComputer\n{paper}\DRAW!')
elif player == 2 and computer == 2:
  print(f'\nPlayer\n{scissors}\nComputer\n{scissors}\nDRAW!')
elif player == 0 and computer == 2:
  print(f'\nPlayer\n{rock}\nComputer\n{scissors}\nYou Win!')
elif player == 1 and computer == 0:
  print(f'\nPlayer\n{paper}\nComputer\n{rock}\nYou Win!')
elif player == 2 and computer == 1:
  print(f'\nPlayer\n{scissors}\nComputer\n{paper}\nYou Win!')
elif player == 0 and computer == 1:
  print(f'\nPlayer\n{rock}\nComputer\n{paper}\nYou Loose!')
elif player == 1 and computer == 2:
  print(f'\nPlayer\n{paper}\nComputer\n{scissors}\nYou Loose!')
elif player == 2 and computer == 0:
  print(f'\nPlayer\n{scissors}\nComputer\n{rock}\nYou Loose!')
else:
  print("Invalid Choice")