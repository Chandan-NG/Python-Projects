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
elements=[rock,paper,scissors]
computer_choice = random.choice(elements)

my_ip = int(input("Enter your choice. Type 0 for Rock, 1 for Paper and 2 for Scissors: \n"))

if my_ip == 0 or my_ip ==1 or my_ip ==2:
    print("Computer Chose:")
    print(computer_choice)

    print("\n")

    my_choice = elements[my_ip]
    print("You Chose:")
    print(my_choice)

    if my_choice == rock and computer_choice == paper:
        print("Computer Won...!")
    elif my_choice == rock and computer_choice == scissors:
        print("You Won...!")
    elif my_choice == paper and computer_choice == rock:
        print("You Won...!")
    elif my_choice == paper and computer_choice ==scissors:
        print("Computer Won...!")
    elif my_choice == scissors and computer_choice == rock:
        print("Computer Won...!")
    elif my_choice == scissors and computer_choice == paper:
        print("You Won...!")
    elif my_choice == computer_choice:
        print("It's a Draw...Play Again!")

else:
    print("Invalid Choice!")