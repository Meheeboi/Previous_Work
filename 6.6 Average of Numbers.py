# Assume a file containing a series of integers is named 
# numbers.txt and exists on the computer's disk. Write a program 
# that calculates the average of all the numbers stored in the file.

def main():
    myfile = open("numbers.txt", 'r')

    total = 0
    numLines = 0
    lineCount = myfile.readline()

    while lineCount != "":
        numLines += 1
        total += int(lineCount)
        lineCount = myfile.readline()

    average = total / numLines

    myfile.close()

    print( "Average of numbers in file is:", average)

main ()


