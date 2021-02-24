# Design a function that uses recursion to raise a number to a power. The function should
# accept two arguments: the number to be raised, and the exponent. Assume the exponent is
# a nonnegative integer.

# 12.7 Recursive Power

x = int(input("Enter a number; "))
y = int(input("Enter the power to raise the number to; "))

def power_recursion(x, y):
    if y == 0:
        return 1
    else:
        return x * pow(x, y-1)
p = power_recursion(x,y)

print(p)