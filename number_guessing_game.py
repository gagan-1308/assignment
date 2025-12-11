import random
print("Welcome to the number guessing game. We have a number that needs to be guessed. You have 10 chances.")
print("The secret number is between 1 and 100.")
secret_number = random.randint(1,100)
attempts = 10
num=1
guess_number = False
while num<=10:
    print(f"You have {attempts} attempts to guess the number.")
    user_number=int(input("enter correct number to guess: "))
    if user_number==secret_number:
        print("Congrats, your guess is correct!.")
        guess_number=True
        break
    else:
        if user_number<secret_number:
            higher_or_lower= "higher"
        else:
            higher_or_lower= "lower"
        print(f"Your guess is wrong. Try {higher_or_lower}.")
    num+=1
    attempts-=1
if not guess_number:
    print("Bad Luck, Your exhausted all attempts and couldn't guess the number.")
print(f"The Secret Number is, {secret_number}")