#TASK_1
import os
#Here We Create a File
with open("sample.txt", 'xt') as fh:
    fh.write("Hello World.\n")
    fh.write("This is a Sample text File.\n")
    fh.write("It Contains Multiple Lines.")

# Here I Try as shown in given task that print Line_1: Line_2 and so on... as shown as in output.

file_name='sample.txt'
with open(file_name, 'rt') as fh:
    Line_1=fh.readline()
    Line_2=fh.readline()
    Line_3=fh.readline()
    if os.path.exists(file_name):
        print("Reading file content:")
        print(f"Line 1: {Line_1.rstrip('\n')}")
        print(f"Line 2: {Line_2.rstrip('\n')}")
        print(f"Line 3: {Line_3.rstrip('\n')}")
    else:
        print(f"ERROR: The file {file_name} does not exist.")

# let's suppose I don't know how many lines there are in file, so I create a for loop here

file_name='sample.txt'
with open(file_name, 'rt') as fh:
    lines=fh.readlines()
for line in lines:
    print(line.rstrip('\n'))


#TASK_2
'''Here I use wt instead of x because in case anyone run this file twice it gives error and as we know if file
doesn't exists 'w' also create it if we run it. '''
file_name2='output.txt'
with open(file_name2, 'wt') as hh:
    ask=str(input("Enter text to write to the file: "))
    hh.write(ask)
    print(f"Data successfully written to the {file_name2}.")
    hh.write("\n")
    ask_2=str(input("Enter additional text to append: "))
    hh.write(ask_2)
    print(f"Data successfully appended.")

with open("output.txt", 'rt') as gh:
    lines=gh.readlines()

print(f"Final Content of {file_name2}:")
for line in lines:
    print(line.rstrip('\n'))