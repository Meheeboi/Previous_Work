# Write a recursive function that accepts an integer argument, n. 
# The function should display
# n lines of asterisks on the screen, with the first line showing 1 asterisk, 
# the second line
# showing 2 asterisks, up to the nth line which shows n asterisks.

#12.3 Recursive Lines

m = 3
n = 6

def ackermann(m,n):
    if m == 0:
        return n+1
    elif n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))

print (ackermann(m,n))