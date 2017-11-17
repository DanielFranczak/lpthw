people = 31#variables
cars = 6
trucks = 30

if cars > people: #if statement
    print("We should take cars")
elif cars < people:  # ==else if
    print("We should not take the cars.")
else: #other situation
    print("We can't decide")

if trucks > cars: #if I use more than one elif block, and the first and other block will be True, python chooses the first one true statement
    print("That's too many trucks")
elif trucks < cars:
    print("Maybe we could take the trucks")
else:
    print("We can't decide")

if people > trucks:
    print("Allright, let's just take the trucks")
else:
    print("Fine, lety's stay at home then")

if people == trucks:
    print ("There's equal number of people and trucks")
elif people != trucks and trucks > cars:
    print ("TRUCKS POWER")
else:
    print("Other possibility")