#Nested Pattern that prints a new space each line for 5 lines after the first

for x in range (0,6):
    if x < 1:
        print ("#""#")
    if x >= 1:
        print ("#",(" " * (x -1)), "#")
        