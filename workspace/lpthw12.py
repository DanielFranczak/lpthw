
try:
    age = int(input("How old are you?"))
except ValueError:
    print("please enter correct type of data")
try:
    height = str(input("How tall are you"))
except ValueError:
    print("please enter correct type of data")
try:
    weight = float(input("How much do you weigh?"))
except ValueError:
    print("please enter correct type of data")
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
