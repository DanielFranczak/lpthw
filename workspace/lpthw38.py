ten_things = "Apples Oranges Crows Telephone Light Sugar" #simple list
print(ten_things)
print("Wait there are not 10 tings in that list. Let's fix that.")

stuff = ten_things.split(' ')# splits list ten_things
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"] #new lists

while len(stuff) != 10: #when length of stuff is not equal 10 then:
    next_one = more_stuff.pop() #it takes the last item from more_stuff
    print("Adding ", next_one) #it shows what it take
    stuff.append(next_one) #it adds popped item to the stuff
    print(f"There are {len(stuff)} items now.") #it shows length of stuff


print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1]) #shows item form the lists with index 1
print(stuff[0]) #showsh first item from the list
print(stuff[-1]) #shows last item from the list
print(stuff[9])
print(stuff.pop())#remove the last thing from the list and return it
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
