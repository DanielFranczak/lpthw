from sys import argv #import library from sys
script, filename = argv #type script and give argument variable

txt = open(filename) #responsible for open the file

print(f"Here's your file {filename}:") #write on the screen name of opened file
print(txt.read()) #write on the screen content of the file

print("Type the filename again:") #shows another possibility to open the file
file_again = input("> ") #ask us for write file name

txt_again = open(file_again) # open the file

print(txt_again.read()) #write content of the opened file on the screen

txt_again.close()
