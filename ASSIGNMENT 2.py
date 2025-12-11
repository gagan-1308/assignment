#TASK_1

num=int(input("Enter Your Number: "))
if num % 2==0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

#TASK_2

total=0
for i in range(51):
    total=total+i
print (f"The sum of numbers from 1 to 50 is: {total}")