from sys import argv #import feratures from library
script, input_file = argv #assign args


def print_all(f): #function prints variable f
    print(f.read())


def rewind(f): #rewind file to the beginning
    f.seek(0)


def print_a_line(line_count, f): #print the  particularly line
    print(line_count, f.readline(), end="")


current_file = open(input_file) #open the file

print("First let's print the whole file:\n")

print_all(current_file) #use function print_all to show what've got in the file

print("Now let's rewind, kind of like a tape")

rewind(current_file) #rewind current file to the beginning

print("Let's print three lines:")

current_line = 1 #help to count the lines
print_a_line(current_line, current_file) #print the particularly line

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

