import random

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
decision = int(input("Rock(0), Paper(1) or Scissors(2)? Choose wisely!\n"))
 
# rock > scissors 
# rock < paper
# paper > rock
# paper > scissors
# scissors < rock
# scissors > paper

if decision == 0:
  print(rock)
  compare = rock
if decision == 1:
  print(paper)
  compare = paper
if decision == 2:
  print(scissors)
  compare = scissors

print("Computer chose: ")
comp_decision = random.randint(0,2)

if comp_decision == 0:
  print(rock)
  cs_compare = rock
if comp_decision == 1:
  print(paper)
  cs_compare = paper
if comp_decision == 2:
  print(scissors)
  cs_compare = scissors


if cs_compare == rock and compare == scissors or cs_compare == paper and compare == rock or cs_compare == scissors and compare == paper:
  print("You suck.. I mean lose")
elif cs_compare == compare:
  print("Draw. This is intense")
else:
  print("Yay! You won!!!")