from random import randint


bound = input("Enter a number: ")
while not bound.isdigit():
    bound = input("[INVALID] Enter a number: ")

number = randint(int(bound)-10, int(bound)+10)

guess = input("Enter a guess: ")
while not guess.isdigit():
    guess = input("[ENTER INTEGER] Enter a guess: ")

guess = int(guess)

tries = 0
while number != guess:
    tries += 1
    if guess < number:
        print(f"Number is greater than {guess}")
    elif guess > number:
        print(f"Number is less than {guess}")

    guess = input("Enter another guess: ")
    while not guess.isdigit():
        guess = input("[ENTER INTEGER] Enter guess: ")
    guess = int(guess)

print(f"You got it correct in {tries} number of tries.")
