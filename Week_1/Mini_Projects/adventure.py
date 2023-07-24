name = input("Enter your name: ")

print(f"Welcome {name}! This adventure is a fight between two masterminds Light Yagami and L. Lawliet. both of them "
      f"claim to be on justice, but only one of them is on the right path. You have to carefully analyse your journey "
      f"and take out the unjust one.")

role = input("Choose your role. (Light, L): ")

if role == 'Light':
    ans = input("You have chosen to be Light Yagami, you have been given a Death Note through which you can kill any "
                "person in the world just by knowing their name and the face. What will you do with the book?\n"
                "a) Hand it over to the police.\n"
                "b) Use it to remove crime from the world.\nChoice: ")
    if ans == 'a':
        print("You made the right choices and are on the right path.")
    elif ans == 'b':
        print("To be continued ...")
    else:
        print("Invalid choice, you lose.")
elif role == 'L':
    ans = input("You have chosen to be L. Lawliet, you are teamed up with the police to solve the mystery of unknown "
                "deaths in prison cells. What will you do in this scenario knowing that you may die yourself?\n"
                "a) Leave it to the police and run away.\n"
                "b) Help police in solving this mystery.\nChoice: ")
    if ans == 'a':
        print("You survived but did not win.")
    elif ans == 'b':
        print("To be continued ...")
    else:
        print("Invalid choice, you lose.")
else:
    print("Invalid choice, you lose.")
