i = 0  #var
numbers = []  #lists

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    i = i + 1
    print("Numbers now:", numbers)
    print(f"At the bottom i is {i}")



def appendable(k, g):
    while k < g:
        print(f"At the top k is {k}")
        numbers.append(k)
        k = k + 1
        print("Numbers now:", numbers)
        print(f"At the bottom k is {k}")

def appendable_beta(g, h):
    while i < g:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + h
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")

def apependable_gamma(g, h):
    while i in range (g, h):
        print(f"At the top i is {i}")
        numbers.append(i)
        print("numbers now: ", numbers)
        print(f" At the bottom i is {i}")

print("the numbers: ")

for num in numbers:
    print(num)

ap1 = appendable(0, 8)
ap2 = appendable_beta(6, 2)
#ap3 = apependable_gamma(3,8)

print(ap1)

