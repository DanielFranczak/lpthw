print("How old are you", end = '')
age = int(input())
print("How high are you (cm)", end='')

try:
    height = int(input())
except ValueError:
    print("Error - wrong type of data")

print("Do you like bananas?")
like = input()
lik2 = input("Podaj liczbe naturalna")

print(f"So you're {age}, you are {height} tall, and you {like} banans")
print("So you are {0}, and you are{1} tall and you {2} bananas".format(age, height, like))
print("So you are {0}, and you are{1} tall and you {2} bananas", age, height, like)
print('lik2 {0}'.format(lik2))
print(type(lik2))
print(type(age))

age3 = type(float(age))
print(age3)


