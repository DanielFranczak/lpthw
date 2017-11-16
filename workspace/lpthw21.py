def add(a, b): #function
    print(f"ADDING {a} + {b}") #what it'll do
    return a + b #what it return


def subtract(a, b):
    print(f"SUBTRACT {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"MULTIPLY {a} * {b}")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


def modulo(a, b):
    print(f"MODULO {a} % {b}")
    return a % b


print("Let's do some math with just functions")

age = add(20, 5)
height = subtract(180, float(input("Please write your length of hair")))
weight = multiply(12, 7)
iq = divide(280, 2)
mod = modulo(5, 2)
print(f"Age = {age}, Height = {height}, Weight = {weight}, IQ= {iq}, modulo = {mod}")
what = add(age, subtract(height, multiply(weight, divide(iq, mod))))
print(f"What equals = {what}")
str="000000000abcdefg000000"
print(str.strip('0'))

