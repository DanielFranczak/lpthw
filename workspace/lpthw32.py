#The best way to storage the results of loops are lists
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list

for number in the_count:
    print(f"this is count {number}")

#same as above

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#also we can go through mixed lists too
#notice we have to use {} since we don't know what's in

for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one

elements = []

#then use the range function to do 0 t0 5 counts

for i in range(0, 10, 2):
    print(f"Adding {i} to the list elements")
    elements.append(i)

#now i can print them out too

for i in elements:
    print(f"Elements inside elements list {i}")

