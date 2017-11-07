from sys import argv #library import
from os.path import exists#library import

script, from_file, to_file = argv #add new arguments

print(f"Copying from {from_file} to {to_file}") #printing
# we could do these two on one line, how?

in_file = open(from_file) #opening file
indata = in_file.read() #read file
print(indata)
print(f"the input file is {len(indata)} bytes long")#shows length 

print(f"Does the output file exist? {exists(to_file)}") #returns True if a file exists
print("Ready, hit Return to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w') #erase file and writing mode on
out_file.write(indata) #copy data from indata to out_file

print("Alright, all done, you can see below what've changed in both files.")
#print(from_file)
print(indata)


out_file.close() #closing both documents
in_file.close()