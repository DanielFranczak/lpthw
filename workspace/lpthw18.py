def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_first(arg1):
    print(f"arg1 {arg1}")


def print_second(arg2):
    print(f"arg2: {arg2}")


def print_none():
    print("I got nothin")


arg1 = "daniel"
arg2 = "franczak"

print_two("daniel", "franczak")
print_two_again("daniel", "franczak")
print_two_again(arg1, arg2)
print_first("daniel")
print_second("franczak")
print_none()


