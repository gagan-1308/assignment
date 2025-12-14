""""
# NUMBER CLASSIFIER

print("---Number Classifier---")
i=int(input("Enter an integer: "))
if i > 0:
    print(f"{i} is a positive number.")
    if i%2==0:
        print(f"{i} is an even number.")
    else:
        print(f"{i} is an odd number.")
elif i < 0:
    print(f"{i} is negative number.")
    if i%2==0:
        print(f"{i} is an even number.")
    else:
        print(f"{i} is an odd number.")
else:
    print(f"{i} is zero number.")
"""

""""
# COUNTDOWN TIMER

print("---Countdown Timer---")
i=int(input("Enter a starting number: "))
for num in range(i, 0, -1):     #for loop
    print(num)
print("BLAST OFF!")

while i>0:                      #while loop
    print(i)
    i=i-1
print("BLAST OFF!")
"""

""""
#VOWEL COUNTER:

print("-----VOWELS COUNTER-----")
v=str(input("Enter a word: ")).lower()
vowel_count=0
vowels="aeiou"
for char in v:
    if char in vowels:
        vowel_count=vowel_count+1
print(f"The word '{v}' has {vowel_count} vowels.")
"""

#SIMPLE CALCULATOR MENU

print("---SIMPLE CALCULATOR---")
while True:
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("5. EXIT")
    choice=int(input("Enter your choice: "))
    if choice in [1, 2, 3, 4]:
        num1=float(input("Enter a first number: "))
        num2=float(input("Enter a second number: "))
        if choice==1:
            result=num1+num2
            print(f"Result: {result}")
        elif choice==2:
            result=num1-num2
            print(f"Result: {result}")
        elif choice==3:
            result=num1*num2
            print(f"Result: {result}")
        elif choice==4:
            if num2==0:
                print("Error: Division by zero is not allowed.")
            else:
                result=num1/num2
                print(f"Result: {result}")
    elif choice==5:
        print("Goodbye! Thank you for using the calculator.")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")