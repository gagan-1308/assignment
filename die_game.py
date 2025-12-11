import random

print("Welcome to the Dice Rolling Game.")


while True:
    choice = input("Press 'Enter' to roll a dice or Press 'q' to quit: ")
    choice = choice.strip()
    if choice == "q":
        print("Thanks for Playing the Game. Goodbye")
        break
    elif choice == "":
        choice = random.randint(1, 6)
        print(f"Your Rolling number is {choice}")
    else:
        print("invalid input!!")
print("GAME OVER!!!")