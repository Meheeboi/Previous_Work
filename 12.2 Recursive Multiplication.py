# Design a recursive function that accepts two arguments into the parameters x and y. The
# function should return the value of x times y. Remember, multiplication can be performed
# as repeated addition as follows:
# 7 x 4 = 4 + 4 + 4 + 4 + 4 + 4 + 4
# (To keep the function simple, assume x and y will always hold positive nonzero integers.)

#12.2 Recursive Multiplication

x = 7
y = 4

def recursive_multiply(x, y):
    if x < y:
        return recursive_multiply(y,x)
    if y == 0:
        return 0
    return x + recursive_multiply(x,  y-1)

print(x * y)
print(recursive_multiply(x, y))
