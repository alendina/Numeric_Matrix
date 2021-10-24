import math


def factorial_control(n):
    print("Don't cheat!")


math.factorial = factorial_control


# don't delete this line, please
math.factorial(23)
