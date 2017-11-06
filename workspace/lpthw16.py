from sys import argv #import feature
script, filename = argv
print(f"We're going to erase {filename}.") #printing
print("If you don't want that, hit ctrl-C ")
print("If you want that, hit return")
#target = open(filename)
input("?") #wait for push

print("Opening the file...")
target = open(filename, 'w') #assign open function to  the target variable

print("I'm going to ask you about three lines of text, write whatever you want") #printing

line1 = input("Line 1: ") #ask user about new line of text
line2 = input("Line 2: ") #ask user about 2 line of text
line3 = input("Line 3: ") #ask user about 3 line of text

print("I'm going to write these to the file")

target.write(line1) #writing new lines of text
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it:")
target.close() # close the file
