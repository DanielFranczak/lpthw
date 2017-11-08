def cheese_and_crackers(cheese_count, boxes_of_crackers): #function which describe smth
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) #assign arguments

print("OR, we can use variables from our script:")
amount_of_cheese = 10 #assign arguments
amount_of_crackers = 50 #assign arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers) #assign arguments

print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6) #assign arguments

print("And we can combine the two, variables and math: ")
cheese_and_crackers(amount_of_cheese+10, amount_of_crackers*2) #assign arguments

print(f"Please write how many cheese do you have?")
try:
    amount_of_crackers = int(input("Amount of crackers: "))
    amount_of_cheese = int(input("Amount of cheese: "))
except ValueError:
    print("Please write number not word")
cheese_and_crackers(amount_of_cheese, amount_of_crackers)




