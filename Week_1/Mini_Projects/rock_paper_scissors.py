from random import choice

options = ['rock', 'paper', 'scissors']
dominant = {'scissors': 'paper', 'paper': 'rock', 'rock': 'scissors'}

while True:
    user = input("Enter one of the following:\nrock\npaper\nscissors\nOR\nq to quit.\n").lower()

    if user == 'q':
        break
    elif user not in options:
        continue

    computer_pick = choice(options)
    if dominant[computer_pick] == user:
        print("\nComputer Won.\n")
    elif dominant[user] == computer_pick:
        print("\nYou Won.\n")
    else:
        print("\nIt was a tie.\n")

print("Terminated!")