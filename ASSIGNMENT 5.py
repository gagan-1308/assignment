#TASK_1
#Create a dictionary of student names and marks
student_marks = {
        "Alice": 85,
        "Carol": 78,
        "Gagan": 92,
        "Harsh": 67,
        "Jatin": 90}
name = input("Enter the student's name: ") #Ask the user for a student's name
if name in student_marks:   #Retrieve marks or show error message
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Error: Student '{name}' not found in the records.")

#TASK_2
#Create a list of numbers from 1 to 10
numbers = list(range(1, 11))
extracted = numbers[:5] #Extract the first five elements using slicing
reversed_list = extracted[::-1] #Reverse the extracted elements using slicing
print("Original list:", numbers)
print("Extracted first five elements:", extracted)
print("Reversed extracted list:", reversed_list)
