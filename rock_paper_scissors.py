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
#User Choice
data=[rock,paper,scissors]  #vul korsilam:variable k str hisabe use korsi 'rock'
number1=int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors.\n"))
if number1>=1 and number1<=3:
    print(data[number1-1])

#PC Choice
number2=random.randint(1,3)
computer_choice=data[number2-1]
print(f"Computer Choose:\n{computer_choice}")
if number1==number2:
    print('It\'s a draw')
elif number1<1 or number1>2:
    print("Please enter a valid number between 1 to 3")
elif number1==3 and number2==1 :
    print("💥 You Lost!")
elif number1==1 and number2==3:
    print("🎉 You Win!")
elif number1<number2:
    print("💥 You Lost!")
elif number1>number2:
    print("🎉 You Win!")
